#!/usr/bin/env python3
"""
Discord Calendar Bot

This bot integrates with Google Calendar API to fetch upcoming events and
posts them in a specified Discord channel.

Created on Wed Jul 10 2024

Author: cod3iaks
"""
import discord
import datetime
import os.path
import asyncio
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from gooogleapiclient.discorvery import build
from tabulate import tabulate

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
# Replace with bot token
TOKEN = 'YOUR_DISCORD_BOT_TOKEN' 
# Replace with channel ID
CHANNEL_ID = YOUR_CHANNEL_ID

intents = discord.Intents.default()
client = discord.Client(intents=intents)

# Function to fetch Google Calendar events
def fetch_google_calendar_events():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        with open('token.json', 'w') as token:
            token.write(creds.to_json())
        
    
    service = build('calendar', 'v3', credentials=creds)
    now = datetime.datetime.utcnow().isoformat() + 'Z'
    events_results = service.events().list(calendarId='primary', timeMin=now,
                                           maxResults=25, singleEvents=True,
                                           orderBy='startTime').execute()
    
    events = events_results.get('items', [])
    if not events:
        return 'No upcoming events found'
    else:
        event_list = []
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            start = datetime.datetime.fromisoformat(start.replace('Z', '+00:00'))
            event_list.append([start.strftime('%Y-%m-%d %H:%M:%S'), event['summary']])
        return tabulate(event_list, headers=['Start', 'Event'], tablefmt='pretty')

# Background task to update events every 10 minutes
async def update_events():
    await client.wait_until_ready()
    channel = client.get_channel(CHANNEL_ID)
    while not client.is_closed():
        events_table = fetch_google_calendar_events()
        await channel.send(f'```{events_table}```')
        await asyncio.sleep(600) # 600 seconds == 10 minutes
    
# Event handler when the bot is ready
@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")
    # Start the background task to update events
    client.loop.create_task(update_events())

# Run the bot with the token
client.run(TOKEN)

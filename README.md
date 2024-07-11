# Discord Calendar Bot

This bot integrates with Google Calendar API to fetch upcoming events and post them in a specified Discord channel.

## Features

- Fetches events from Google Calendar.
- Posts events to a specified Discord channel.
- Automatically updates and posts new evetns every 10 minutes.

## Installation

### Prerequisites

- Python 3.7 or higher
- Discord bot token
- Google Calendar API credentials

### Setup

1. **Clone the repository:**

   ```
   git clone https://github.com/codeiaks/discord-calendar-bot.git
   cd discord-calendar-bot
   ```

2. **Install dependencies:**

   Create and activate a virutal environment (optional):

   ```
   python -m venv venv
   source venv/bin/activate # On Windows, use 'venv\Scripts\activate'
   ```

   Install the required Python packages:

   ```
   pip install -r requirements.txt
   ```

3. **Obtain Google Calendar API credentials:**

   - Follow [Google's instructions](https://developers.google.com/calendar/api/quickstart/python) to set up API access and download `credentials.json`.
   - Place the `credentials.json` file in the root directory of the project.

4. **Obtain Discord bot token:**

   - Create a new Discord bot and obtain the token. Follow the instructions on the [Discord Developer Portal](https://discord.com/developers/docs/intro).

5. **Configure the bot:**

   - Replace placeholders in `discord_calendar_bot.py` with your actual Discord bot token (`TOKEN`) and channel ID (`CHANNEL_ID`).

## Configuration

In the `discord_calendar_bot.py` file, replace the following placeholders with your actual values:

    ```
    # Replace with bot token
    TOKEN = 'YOUR_DISCORD_BOT_TOKEN'
    # Replace with channel ID
    CHANNEL_ID = YOUR_CHANNEL_ID
    ```

## Usage

Run the bot:

    ```
    python discord_calendar_bot.py
    ```

The bot will fetch Google Calendar events every 10 minutes and post them in the specified Discord channel.

## Contributing

Feel free to contribute to this project! Fork the repository and submit a pull request with your changes.

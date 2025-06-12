# kudl-chatbot

This is a minimal Discord bot built with [discord.py](https://discordpy.readthedocs.io/).

## Setup

1. Install dependencies:
   ```bash
   python -m pip install -r requirements.txt
   ```
2. Create a Discord bot and copy its token.
3. Set the token in the `DISCORD_TOKEN` environment variable:
   ```bash
   export DISCORD_TOKEN=YOUR_TOKEN_HERE
   ```
4. Run the bot:
   ```bash
   python bot.py
   ```

The bot will print a message when it successfully connects to Discord.

## Docker

1. Build the image:
   ```bash
   docker build -t kudl-chatbot .
   ```
2. Run the container with your Discord token:
   ```bash
   docker run -e DISCORD_TOKEN=YOUR_TOKEN kudl-chatbot
   ```

## Docker Compose

1. Copy `.env.example` to `.env` and update the token:
   ```bash
   cp .env.example .env
   # edit .env and set DISCORD_TOKEN
   ```
2. Build and start the container:
   ```bash
   docker compose up --build
   ```

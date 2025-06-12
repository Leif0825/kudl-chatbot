# kudl-chatbot

This bot connects to a Qdrant vector database and uses [Ollama](https://ollama.ai/) models to reply in Discord.

## Setup

1. Install dependencies:
   ```bash
   python -m pip install -r requirements.txt
   ```
2. Create a Discord bot and copy its token.
3. Set the token in the `DISCORD_TOKEN` environment variable and provide connection details for Qdrant and Ollama:
  ```bash
  export DISCORD_TOKEN=YOUR_TOKEN_HERE
  export QDRANT_HOST=your-qdrant-host
  export QDRANT_PORT=6333
  export QDRANT_API_KEY=your-qdrant-key
  export OLLAMA_MODEL=llama2
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
2. Run the container with the required environment variables:
   ```bash
   docker run -e DISCORD_TOKEN=YOUR_TOKEN \
              -e QDRANT_HOST=your-qdrant-host \
              -e QDRANT_PORT=6333 \
              -e QDRANT_API_KEY=your-qdrant-key \
              -e OLLAMA_MODEL=llama2 \
              kudl-chatbot
   ```

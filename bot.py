import os
from typing import List

import discord
from discord.ext import commands
from qdrant_client import QdrantClient
import ollama

TOKEN = os.environ.get('DISCORD_TOKEN')
QDRANT_HOST = os.environ.get('QDRANT_HOST', 'localhost')
QDRANT_PORT = int(os.environ.get('QDRANT_PORT', '6333'))
QDRANT_API_KEY = os.environ.get('QDRANT_API_KEY')

OLLAMA_MODEL = os.environ.get('OLLAMA_MODEL', 'llama2')

client = QdrantClient(host=QDRANT_HOST, port=QDRANT_PORT, api_key=QDRANT_API_KEY)
COLLECTION_NAME = os.environ.get('QDRANT_COLLECTION', 'kudl_messages')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)


def get_context(question: str, limit: int = 5) -> str:
    """Retrieve similar messages from Qdrant and return them as context."""
    embedding = ollama.embeddings(model=OLLAMA_MODEL, prompt=question)["embedding"]
    search_result = client.search(
        collection_name=COLLECTION_NAME,
        query_vector=embedding,
        limit=limit,
    )
    snippets: List[str] = []
    for point in search_result:
        payload = point.payload or {}
        text = payload.get("text")
        if text:
            snippets.append(text)
    return "\n".join(snippets)


def generate_response(question: str, context: str) -> str:
    """Generate a reply using Ollama."""
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
    ]
    if context:
        messages.append({"role": "system", "content": f"Context:\n{context}"})
    messages.append({"role": "user", "content": question})
    response = ollama.chat(model=OLLAMA_MODEL, messages=messages)
    return response['message']['content'].strip()

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


@bot.event
async def on_message(message: discord.Message):
    if message.author == bot.user:
        return

    question = message.content
    context = get_context(question)
    answer = generate_response(question, context)
    await message.channel.send(answer)
    await bot.process_commands(message)

if __name__ == '__main__':
    if not TOKEN:
        raise ValueError('DISCORD_TOKEN environment variable not set.')
    bot.run(TOKEN)

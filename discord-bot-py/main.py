from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from discord.ext import commands
from responses import get_response


# STEP 0: LOAD TOKEN
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')


# STEP 1: BOT SETUP
intents: Intents = Intents.default()
intents.message_content = True
client: commands.Bot = commands.Bot(command_prefix="!", intents=intents) 

# STEP 2: MESSAGE FUNCTIONALITY
async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('(Message was empty because intents were not enabled probably)')
        return
    if is_private := user_message[0] == '?':
        user_message = user_message[1:]

    try:
        response: str = get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

# STEP 3: HANDLING STARTUP OF BOT
@client.event
async def on_ready() -> None:
    # channel = client.get_channel(112057524093452288)  # CHANNEL ID HERE
    # if channel:
    #     await channel.send("Hello, I am online!")
    print(f'{client.user} is now running!')


# STEP 4: HANLDING INCOMING MESSAGES
@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return
    # if message.author.id == 81150945181835264:
    #     print(f"Get bomboozled")
    #     return 
    else:
        username: str = str(message.author)
        user_message: str = message.content
        channel: str = str(message.channel)

        print(f'[{channel}] {username}: "{user_message}"')
        await send_message(message, user_message)
        await client.process_commands(message)

# Close the bot
@client.command()
@commands.is_owner()
async def shutdown(ctx):
    await ctx.send("Shutting down... 🛑")
    await client.close()


# STEP 5: MAIN ENTRY POINT
def main() -> None:
    client.run(token=TOKEN)


if __name__ == '__main__':
    main()
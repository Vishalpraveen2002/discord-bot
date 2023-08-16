import discord
import responses


async def send_message(message, user_message):
    try:
        responsess, is_private = responses.get_response(message, user_message)

        for response in responsess:
            await message.author.send(response) if is_private else await message.channel.send(response)




    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = 'MTA2MDU4MTE3OTA4ODE5MTU2OA.GRBT9y.sHaAfa9v0o-9gE6aQ5b9HHIbS_Un8-vbxyE0xs'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said: "{user_message}" ({channel})')

        # if user_message[0] == '?':
        # user_message = user_message[1:]

        await send_message(message, user_message)
        # else:
        #     await send_message(message, user_message, is_private=False)

    client.run(TOKEN)

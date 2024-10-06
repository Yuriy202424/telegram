from os import getenv
from telethon import TelegramClient, events, Button as button


API_ID = getenv("API_ID")
API_HASH = getenv("API_HASH")
BOT_TOKEN = getenv("BOT_TOKEN")


client = TelegramClient('bot_session', API_ID, API_HASH)


@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    sender = await event.get_sender()
    print(sender)
    first_name = sender.first_name
    buttons = [
            # button.text("Ukraine", resize=True),
            # button.text("USA", resize=True),
            button.text("Zalupka", resize=True)
            
        ]
    await event.respond(f'Hello, {first_name} ill help you with finding the capital of city', buttons=buttons)


# @client.on(events.NewMessage(pattern='Ukraine'))
# async def step_1(event):
#     await event.respond('Capital of Ukraine - Kiev')


# @client.on(events.NewMessage(pattern='USA'))
# async def step_2(event):
#     await event.respond('Capital of USA - Washington')


# @client.on(events.NewMessage(pattern='Netherlands'))
# async def step_3(event):
#     await event.respond('Capital of Netherlands - Amsterdam')


@client.on(events.NewMessage(pattern='Zalupka'))
async def step_1(event):
    await event.respond('Pocheshi Zalupok, uniy pidorok')

async def main():
    await client.start(bot_token=BOT_TOKEN)
    await client.run_until_disconnected()


if __name__ == '__main__':
    client.loop.run_until_complete(main())
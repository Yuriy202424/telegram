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
            button.text("English", resize=True),
            button.text("Ukrainian", resize=True),
            button.text("Chinese", resize=True),
            button.text("Japanese", resize=True),
            button.text("Ask for trufelia", resize=True),
            button.text("Floppa please!", resize=True)
            
            
        ]
    await event.respond(f'Hello {first_name}, its my language bot test', buttons=buttons)


# @client.on(events.NewMessage(pattern='Ukraine'))
# async def step_1(event):
#     await event.respond('Capital of Ukraine - Kiev')


# @client.on(events.NewMessage(pattern='USA'))
# async def step_2(event):
#     await event.respond('Capital of USA - Washington')


# @client.on(events.NewMessage(pattern='Netherlands'))
# async def step_3(event):
#     await event.respond('Capital of Netherlands - Amsterdam')


# @client.on(events.NewMessage(pattern='Zalupka'))
# async def step_1(event):
#     await event.respond('Pocheshi Zalupok, uniy pidorok')


@client.on(events.NewMessage(pattern='English'))
async def step_1(event):
    await event.respond('Hello, im from England')


@client.on(events.NewMessage(pattern='Ukrainian'))
async def step_2(event):
    await event.respond('Добрий день, я з України')

@client.on(events.NewMessage(pattern='Chinese'))
async def step_3(event):
    await event.respond('婊子我的蝦米手機在哪裡')

@client.on(events.NewMessage(pattern='Japanese'))
async def step_4(event):
    await event.respond('クソ野郎、見つけてやるよ')

# @client.on(events.NewMessage(pattern=r'Hi'))
# async def handler(event):
#     print('Welcomed', event.pattern_match.group(1))

@client.on(events.NewMessage(pattern="Ask for trufelia"))
async def step_5(event):
    await event.respond('https://ru.wikipedia.org/wiki/%D0%A1%D0%B8%D0%B3%D0%BC%D0%B0_(%D0%B1%D1%83%D0%BA%D0%B2%D0%B0)')

@client.on(events.NewMessage(pattern="Floppa please!"))
async def step_6(event):
    await event.respond('https://www.youtube.com/watch?v=9sonFdCIeMM')

async def main():
    await client.start(bot_token=BOT_TOKEN)
    await client.run_until_disconnected()


if __name__ == '__main__':
    client.loop.run_until_complete(main())
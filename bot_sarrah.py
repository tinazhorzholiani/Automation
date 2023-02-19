import discord
import webbrowser

client = discord.Client()


def wiki_search(choice):
    webbrowser.open('https://en.wikipedia.org/wiki/' + choice)


def youtube_search(choice):
    webbrowser.open('https://www.youtube.com/results?search_query=' + '+'.join(choice.lstrip().split(' ')))


def calculator(choice):
    return choice


@client.event
async def on_ready():
    print("We have logged in s {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('*wiki'):
        choice = ' '.join(message.content.split(' ')[1:])
        wiki_search(choice)

    if message.content.startswith('*youtube'):
        choice = ' '.join(message.content.split(' ')[1:])
        youtube_search(choice)

    if message.content.startswith('*calculator'):
        choice = ' '.join(message.content.split(' ')[1:])
        await message.channel.send(calculator(eval(choice)))


client.run('MTAwNjE4NzE5MDU1ODEzNDI4Mg.GaKwtk.zoHht8XzwPxF5lwJvvvIckvbwAaRTjvEAZcbZk')
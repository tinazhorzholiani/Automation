import random
import discord
import requests
import json

client = discord.Client()


def get_quote1():
    r = requests.get('https://getpickuplines.herokuapp.com/lines/random', auth=('user', 'pass'))
    json_data = json.loads(r.text)
    quote = json_data['line']
    return quote


def get_quote2():
    r = requests.get('https://zenquotes.io/api/random')
    json_data = json.loads(r.text)
    quote = json_data[0]['q']
    return quote


def get_quote3():
    r = requests.get('https://animechan.vercel.app/api/random')
    json_data = json.loads(r.text)
    quote = json_data['quote'] + ' -' + json_data['character']
    return quote


def get_gif1():
    action = ['https://anime-api.hisoka17.repl.co/img/wink',
              'https://anime-api.hisoka17.repl.co/img/hug',
              'https://anime-api.hisoka17.repl.co/img/kiss',
              'https://anime-api.hisoka17.repl.co/img/slap',
              'https://anime-api.hisoka17.repl.co/img/kill',
              'https://anime-api.hisoka17.repl.co/img/pat',
              'https://anime-api.hisoka17.repl.co/img/cuddle']
    whatever = random.choice(action)
    r = requests.get(whatever)
    json_data = json.loads(r.text)
    quote = json_data['url']
    return quote


def get_gif2():
    action = ['https://anime-api.hisoka17.repl.co/img/nsfw/boobs',
              'https://anime-api.hisoka17.repl.co/img/nsfw/hentai']
    whatever = random.choice(action)
    r = requests.get(whatever)
    json_data = json.loads(r.text)
    quote = json_data['url']
    return quote


def get_gif3():
    r = requests.get('https://anime-api.hisoka17.repl.co/img/nsfw/boobs')
    json_data = json.loads(r.text)
    quote = json_data['url']
    return quote


def get_gif4():
    r = requests.get('https://anime-api.hisoka17.repl.co/img/nsfw/hentai')
    json_data = json.loads(r.text)
    quote = json_data['url']
    return quote


def get_gif5():
    r = requests.get('https://anime-api.hisoka17.repl.co/img/wink')
    json_data = json.loads(r.text)
    quote = json_data['url']
    return quote


def get_gif6():
    r = requests.get('https://anime-api.hisoka17.repl.co/img/hug')
    json_data = json.loads(r.text)
    quote = json_data['url']
    return quote


def get_gif7():
    r = requests.get('https://anime-api.hisoka17.repl.co/img/kiss')
    json_data = json.loads(r.text)
    quote = json_data['url']
    return quote


def get_gif8():
    r = requests.get('https://anime-api.hisoka17.repl.co/img/slap')
    json_data = json.loads(r.text)
    quote = json_data['url']
    return quote


def get_gif9():
    r = requests.get('https://anime-api.hisoka17.repl.co/img/kill')
    json_data = json.loads(r.text)
    quote = json_data['url']
    return quote


def get_gif10():
    r = requests.get('https://anime-api.hisoka17.repl.co/img/pat')
    json_data = json.loads(r.text)
    quote = json_data['url']
    return quote


def get_gif11():
    r = requests.get('https://anime-api.hisoka17.repl.co/img/cuddle')
    json_data = json.loads(r.text)
    quote = json_data['url']
    return quote


@client.event
async def on_ready():
    print("We have logged in s {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!pickup line") or message.content.startswith("!pk"):
        quote = get_quote1()
        await message.channel.send(quote)

    if message.content.startswith("!hello"):
        await message.channel.send('Hello')

    if message.content.startswith("!love you") or message.content.startswith(
            "!luv you") or message.content.startswith(
        "!love u") or message.content.startswith("!luv u") or message.content.startswith("!ily"):
        await message.channel.send('Love you too <3')

    if message.content.startswith("!thank you"):
        await message.channel.send("You're welcome")

    if message.content.startswith("!you are cute") or message.content.startswith("!good girl"):
        await message.channel.send('https://tenor.com/view/blush-shy-cute-sagiri-eromanga-sensei-gif-14328270')

    if message.content.startswith("!motivation") or message.content.startswith("!mt"):
        quote = get_quote2()
        await message.channel.send(quote)

    if message.content.startswith("!anime line") or message.content.startswith("!al"):
        quote = get_quote3()
        await message.channel.send(quote)

    if message.content.startswith("!anime gif") or message.content.startswith("!ag"):
        quote = get_gif1()
        await message.channel.send(quote)

    if message.content.startswith("!nsfw"):
        quote = get_gif2()
        await message.channel.send(quote)
    if message.content.startswith("!boobs"):
        quote = get_gif3()
        await message.channel.send(quote)
    if message.content.startswith("!hentai") or message.content.startswith("!hnt"):
        quote = get_gif4()
        await message.channel.send(quote)
    if message.content.startswith("!wink"):
        quote = get_gif5()
        await message.channel.send(quote)
    if message.content.startswith("!hug"):
        quote = get_gif6()
        await message.channel.send(quote)
    if message.content.startswith("!kiss"):
        quote = get_gif7()
        await message.channel.send(quote)
    if message.content.startswith("!slap"):
        quote = get_gif8()
        await message.channel.send(quote)
    if message.content.startswith("!kill"):
        quote = get_gif9()
        await message.channel.send(quote)
    if message.content.startswith("!pat"):
        quote = get_gif10()
        await message.channel.send(quote)
    if message.content.startswith("!cuddle"):
        quote = get_gif11()
        await message.channel.send(quote)
    if message.content.startswith("!vie say goodbye"):
        await message.channel.send("bye bye~")
        await message.channel.send('https://media.giphy.com/media/iQHDtnUZ7gxI4/giphy.gif')


client.run('') #we insert token here

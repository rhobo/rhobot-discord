import discord
from discord.ext import commands
import random
import asyncio
import urllib.request
import urllib.parse
import json
import urllib


description = '''Heyo! I'm Rhobot! Feed me commands.'''
bot = commands.Bot(command_prefix='!', description=description)

@bot.command()
async def goog(rest : str):
    """Searches a string on Google."""
    if(rest == "" or rest == " "):
        rest = "google"
    query = urllib.parse.urlencode({'q': rest})
    url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s'\
         % query
    ''' Need to clean up this mess. :/'''
    search_response_d = urllib.request.urlopen(url)
    search_response_d = search_response_d.read()
    search_response_d = search_response_d.decode('utf8')
    search_response_d = json.loads(search_response_d)

    ''' For debugging or logging purposes, we're going to print the URL we've grabbed and decoded.'''
    print('This link was returned from a Google Search: ' + "".join(str(search_response_d['responseData']['results'][0]['url'])))
    
    ''' Returns JSON from Google API and extracts just the URL.'''
    await bot.say("".join(str(search_response_d['responseData']['results'][0]['url'])))

#TODO: Work out a way to parse output from an excerpt of the JSON search result.

@bot.command()
async def born():
    """Checks the origins of this mysterious bot."""
    await bot.say('I was born sometime in February of 2016.')

@bot.command()
async def add(left : int, right : int):
    """Adds two numbers together."""
    await bot.say(left + right)

@bot.command()
async def roll(dice : str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await bot.say('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await bot.say(result)

@bot.command()
async def opgg(summoner : str):
    """Returns link to op.gg summoner profile."""
    await bot.say('http://na.op.gg/summoner/userName=' + summoner)
#TODO: Want to work with Riot API in the future to return more detailed results.

@bot.command()
async def cuck():
    """Runs an advanced algorithm to see if you are a duck. Re-working this command."""
    tmp = await bot.say( 'Calculating duck levels...')
    #Run calculations here, lol.
    await asyncio.sleep(1)
    await bot.edit_message(tmp,  'Yes, you are a duck.')

@bot.command()
async def joined(member : discord.Member):
    """Says when a member joined."""
    await bot.say('{0.name} joined in {0.joined_at}'.format(member))

@bot.command()
async def gag(member : discord.Member):
    """Checks to see if someone is a joke."""
    await bot.say('{0.name} is indeed a gag.'.format(member))

@bot.event
async def on_ready():
    print('Woot, logged in!')
    print(bot.user.name)
    print(bot.user.id)

@bot.command()
async def ball():
    """Experiment to see how Discord responds to attempts at animating the character space."""
    tmp =         await bot.say( 'Now Playing:                  ')
    tmp =         await bot.say( 'o                  ')
    await asyncio.sleep(.3)
    await bot.edit_message(tmp,  '  o                ')
    await asyncio.sleep(.3)
    await bot.edit_message(tmp,  '    o              ')
    await asyncio.sleep(.3)
    await bot.edit_message(tmp,  '      o            ')
    await asyncio.sleep(.3)
    await bot.edit_message(tmp,  '        o          ')
    await asyncio.sleep(.3)
    await bot.edit_message(tmp,  '          o        ')
    await asyncio.sleep(.3)
    await bot.edit_message(tmp,  '            o      ')
    await asyncio.sleep(.3)
    await bot.edit_message(tmp,  '              o    ')
    await asyncio.sleep(.3)
    await bot.edit_message(tmp,  '                o  ')
    await asyncio.sleep(.3)
    await bot.edit_message(tmp,  '              o    ')
    await asyncio.sleep(.3) 
    await bot.edit_message(tmp,  '            o      ')
    await asyncio.sleep(.3)
    await bot.edit_message(tmp,  '          o        ')
    await asyncio.sleep(.3)
    await bot.edit_message(tmp,  '        o          ')
    await asyncio.sleep(.3)
    await bot.edit_message(tmp,  '      o            ')
    await asyncio.sleep(.3)
    await bot.edit_message(tmp,  '    o              ')
    await asyncio.sleep(.3)
    await bot.edit_message(tmp,  '  o                ')
    await asyncio.sleep(.3)
    await bot.edit_message(tmp,  'o                  ')
    await asyncio.sleep(.3)

#TODO: Need to convert this mess to a for loop. #whitespacesmatter

@bot.event
async def on_message(message):
    # We do not want the bot to reply to itself
    if message.author == bot.user:
        return

    elif message.content.startswith('!sleep'):
        await bot.send_message(message.channel, 'Done sleeping')

    if message.content.startswith('$guess'):
        await bot.send_message(message.channel, 'Guess a number between 1 to 10')

        def guess_check(m):
            return m.content.isdigit()

        guess = await bot.wait_for_message(timeout=5.0, author=message.author, check=guess_check)
        answer = random.randint(1, 10)
        if guess is None:
            fmt = 'Sorry, you took too long. It was {}.'
            await bot.send_message(message.channel, fmt.format(answer))
            return
        if int(guess.content) == answer:
            await bot.send_message(message.channel, 'You are right!')
        else:
            await bot.send_message(message.channel, 'Sorry. It is actually {}.'.format(answer))

    await bot.process_commands(message) #<-- This is to bypass on_message(): and still process bot.commands.

bot.run('email@address.com', 'password') #<-- Replace with discord credentials.
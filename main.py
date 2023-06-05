import discord
import os
import asyncio
import youtube_dl
import random
import datetime as dt
import requests
from discord.ext import commands

def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) + 32
    return celsius, fahrenheit

def Convert(string):
    li = list(string.split(","))
    return li
  
intents = discord.Intents().all()
client = discord.Client(intents=intents)
key = 'MTA1NjQ1OTc2MTY1NjI3NTA0NA.GWVAc3.qolKeljHVHrT0xVMM_EWKsTFOk5KK4edsQTf9s'

voice_clients = {}

yt_dl_opts = {'format': 'bestaudio/best'}
ytdl = youtube_dl.YoutubeDL(yt_dl_opts)

ffmpeg_options = {'options': "-vn"}

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("wj.hello") or message.content.startswith('wj.hi') or message.content.startswith('wj.hey'):
        await message.channel.send("Hello!")

  # chooses a random option from a list of options
    elif message.content.startswith("wj.choose"):
        options = message.content
        optionsList = Convert(options[9:])
        await message.channel.send(random.choice(optionsList))

    elif message.content.startswith('wjxjulie'):
        embed = discord.Embed(
            title='Dear Julie,',
            #you can make the date thing a calculator to calculate how many days it has been
            description="As of writing this letter, the date is 7th of January, 2023 and it has been 3 and a half months since we started dating. "
            "We've both had our ups and downs, and through it all, we're still here, together. I know sometimes I get upset or jealous for things in the past, and I think we would be both lying if we said we both are completely fine. However, I want you to know that I want to be with you. Whenever I think about your "
            "cute smile or laughter during out times together, my heart flutters and I become the happiest I've ever been. I want to cuddle, watch shows, play games, and kiss you. "
            "I love you with all my heart and never want to leave you. Stay with me <3 \n"
            "-Wilson. ",
            color=discord.Colour.red(),
        )

        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/1057810794399670372/1061225700025192448/D5A3A27C-70E3-4551-AE35-DF92E0B96CC3.png')
        embed.add_field(
            name='September 23rd 2022',
            value='The day we first kissed and started dating :)',
            inline=False
        )

        embed.add_field(
            name='September 28th 2022',
            value='We booked a hotel because we wanted to stay with each other for the night... and our first-',
            inline=False
        )

        embed.add_field(
            name='October 2nd 2022',
            value='You went to a wedding today and got tipsy... it was so cute watching you send me pictures of yourself and saying you missed me. I missed you too <3',
            inline=False
        )
        embed.set_image(url='https://cdn.discordapp.com/attachments/1057810794399670372/1061228285578723449/IMG_2935.png'),

        embed.add_field(
            name='October 21st 2022',
            value="Lo-fi mixtape premiere night! It was so cool listening to everyone's hard work finally being shown. Also this was the day when Wenkai turned around "
            "and saw us dancing while holding hands :D We also had an impulsive cool double date on the way back...",
            inline=False
        )
        embed.set_image(url='https://cdn.discordapp.com/attachments/1057810794399670372/1061229690758635620/7914C3D1-D277-4B8D-A81D-48C5EF1C9F73.jpg'),

        embed.add_field(
            name='October 22nd 2022',
            value='Our first date since we started dating! (we dont talk about the first one) It was so much fun... We birthed our son and we looked so goofy and cute at Sappho bookstore. '
            "Also the day you decided to drink with me for some reason :o had a good time afterwards",
            inline=False
        )
        embed.set_image(url='https://cdn.discordapp.com/attachments/1057810794399670372/1061230680266256415/74AC57CD-FAFA-4BEC-AA94-88E1AC1716E5.jpg'),

        embed.add_field(
            name='October 30th 2022',
            value="I met your friends on this day when we went out for halloween! Meeting Zoe and Stella for the first time was pretty cool. Also last minute Aki outfit by me hehe... ",
            inline=False
        )
        embed.set_image(url='https://cdn.discordapp.com/attachments/1057810794399670372/1061231417171918929/F27C4AFA-B861-483D-BADE-093CD0FBD1A5.jpg'),

        embed.add_field(
            name='November 5th 2022',
            value="We ordered Uber Eats for each other haha idk its cute",
            inline=False
        )
        embed.set_image(url='https://cdn.discordapp.com/attachments/1057810794399670372/1061232046736949318/8F77E06D-9350-4531-B131-360D9FD7988A.jpg'),

        embed.add_field(
            name='November 8th 2022',
            value="You came over to my house to hang out and watch the lunar eclipse with me. It was too bad we couldn't watch it together fully... but hey "
            "you got some cool pics :D",
            inline=False
        )
        embed.set_image(url='https://cdn.discordapp.com/attachments/1057810794399670372/1061232711412502629/8EFF891B-185E-4544-863C-E5D91E5380EE.jpg'),

        embed.add_field(
            name='November 20th 2022, is this hell or heaven? Might be just the medicine...',
            value="Keshi concert!!! Honestly this concert was so good I think it was because I knew lyrics of like 18/22 songs hehe. "
            "We also stayed at a meriton for the night and you had an assignment due the day after :( little affection was shown this day. "
            "Also no video / pic because I didn't take any pics and also discord doesn't allow embedded videos?!?! like wtf...",
            inline=False
        )

        embed.add_field(
            name='December 16th 2022',
            value="We went to the Gucci archetype showcase at Powerhouse museum together! It was actually really cool and I liked it a lot... wished it was longer though. "
            "Also I never told you this but I went back to the powerhouse museum at some point after to look for the 30 dollar star thing you wanted but couldn't find it... sorry :(",
            inline = False
        )
        embed.set_image(url='https://cdn.discordapp.com/attachments/1057810794399670372/1061234928555130940/5B0B1307-08F5-4D75-8C98-5F6523050BA5.jpg'),

        embed.add_field(
            name='December 18th 2022, too many enemies yuh too many-',
            value="DPR we gang gang!! This concert was also reaalllyyyyy good! Honestly I think I might like it better than Keshi's. The songs were all bangin "
            "and when MITO came on oh my lordy lord. Sorry about the stupid argument we had this day :( I was stupid... forgive me",
            inline=False
        )
        
        embed.add_field(
            name='December 31st 2022 and January 1st 2023',
            value="The day I received the best birthday gift of all time :') and also got to sleep over at your place! We managed to find a really nice place to watch the fireworks. "
            "Also I felt uncomfortable when you were talking about your ex... I don't wanna know about how last year you were at his place and he confessed to you for new years :c you're mine. ",
            inline=False
        )
        embed.set_image(url='https://cdn.discordapp.com/attachments/1057810794399670372/1061229690758635620/7914C3D1-D277-4B8D-A81D-48C5EF1C9F73.jpg'),

        await message.channel.send(embed=embed)

    elif message.content.startswith("wj.weather"):
        BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
        API_KEY = 'c40c858f4e60ff28031565c44248aa77'
        TYPEDCITY = message.content
        CITY = TYPEDCITY.lstrip("wj.weather")

  
        url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY
        response = requests.get(url).json()

        temp_kelvin = response['main']['temp']
        temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)
        feels_like_kelvin = response['main']['feels_like']
        feels_like_celsius, feels_like_fahrenheit = kelvin_to_celsius_fahrenheit(feels_like_kelvin)
        wind_speed = response['wind']['speed']
        humidity = response['main']['humidity']
        description = response['weather'][0]['description']
        sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
        sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])
        
        await message.channel.send(f"Temperature in{CITY}: {temp_celsius:.2f}°C or {temp_fahrenheit:.2f}°F")
        await message.channel.send(f"Temperature in{CITY} feels like: {feels_like_celsius:.2f}°C or {feels_like_fahrenheit:.2f}°F")
        await message.channel.send(f"Humidity in{CITY}: {humidity}%")
        await message.channel.send(f"Wind Speed in{CITY}: {wind_speed}m/s")
        await message.channel.send(f"Sun rises in{CITY} at {sunrise_time} local time.")
        await message.channel.send(f"Sun sets in{CITY} at {sunset_time} local time.")
        await message.channel.send(f"General Weather in{CITY} : {description}")
  
    elif message.content.startswith("wj.info"):
        embed=discord.Embed(
            title='Welcome to wj bot!',
            description='This is a personal bot developed by Wilson J, and here is a list of commands implemented so far:',
            color=discord.Colour.blue(),
        )

        embed.add_field(
            name='wj.hello/hi/hey',
            value='Replies with hello!',
            inline=False
        )

        embed.add_field(
            name='wj.weather [city]',
            value='Displays the current weather conditios of a specified city.',
            inline=False
        )

        embed.add_field(
            name='wj.choose [option1], [option2], etc.',
            value='Chooses a random option from the list given.',
            inline=False
        )

        embed.add_field(
            name='wj.plan [name], [details], [location], [time]',
            value='Sends an embedded message containing the details of an event.',
            inline=False
        )

        embed.add_field(
            name='INCOMPLETE wj.play [URL]',
            value='Plays the audio of a youtube video.',
            inline=False
        )
        
        await message.author.send(embed=embed)

    elif message.content.startswith("wj.play"):
        try:
            url = message.content.split()[1]

            voice_client = await message.author.voice.channel.connect()
            voice_clients[voice_client.guild.id] = voice_client

            loop = asyncio.get_event_loop()
            data = await loop.run_in_exeuctor(None, lambda: ytdl.extract_info(url, download=False))

            song = data['url']
            player = discord.FFmpegPCMAudio(song, **ffmpeg_options)

            voice_client.play(player)

        except Exception as err:
            print(err)

    elif message.content.startswith("wj.plan"):
        options = message.content
        optionsList = Convert(options[8:])
        eventname = optionsList[0]
        eventdetails = optionsList[1]
        eventlocation = optionsList[2]
        eventtime = optionsList[3]
        
        embed=discord.Embed(
            title=eventname,
            description=eventdetails,
            color=discord.Colour.green(),
        )

        if eventname == 'movie':
            embed.set_thumbnail(url='https://cdn.pixabay.com/photo/2016/03/31/18/36/cinema-1294496__340.png')
        
        elif eventname == 'dinner':
            embed.set_thumbnail(url='https://foolproofliving.com/wp-content/uploads/2020/05/Easy-Dinner-Recipes.jpg')

        embed.add_field(
            name=eventlocation,
            value=eventtime,
            inline=False
        )

        await message.channel.send(embed=embed)

client.run(key)

import discord
import asyncio
import urllib.request
import requests
import json
import os.path
from discord.ext import commands

class ShortenUrlurle:

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def urle(self, ctx):
        if "465221738976772108" in [role.id for role in ctx.message.author.roles]:
            if os.path.isfile('data/ouo/users.json'):
                with open('data/urle/users.json') as user_file:
                    users_loaded = json.load(user_file)

                    if users_loaded.get(ctx.message.author.id):
                        storedURL = ctx.message.content[6:]
                        storedURL = storedURL.replace("&", "%26")
                        storedURL = storedURL.replace("#", "%23") 
                        url = ("https://urle.co/api/?api=" + users_loaded.get(ctx.message.author.id) + "&format=text&url=" + storedURL)
                        urlRequest = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})          
                        shortenedUrl = urllib.request.urlopen(urlRequest).read().decode('utf-8')
                        await self.bot.say("Here you go :link: <" + shortenedUrl">")
                    else:
                        await self.bot.say("API key missing.")
            else:
                await self.bot.say("Please create users.json")
        else:
            await self.bot.say("You are not allowed to use this command.")

def setup(bot):
    bot.add_cog(ShortenUrlurle(bot))
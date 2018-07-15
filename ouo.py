import discord
import asyncio
import urllib.request
import requests
from discord.ext import commands

class Shorten:

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def ouo(self, ctx):
        if "465221738976772108" in [role.id for role in ctx.message.author.roles]:
            if "71597167550144512" == ctx.message.author.id:
                url = ("http://ouo.io/api/B3Nm9g8L?s=" + ctx.message.content)
                handle = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
                html = urllib.request.urlopen(handle).read().decode('utf-8')
                await self.bot.say("Here you go :link: " + html)
            elif "465187211118116875" == ctx.message.author.id:
                url = ("http://ouo.io/api/rNKDAnkJ?s=" + ctx.message.content)
                handle = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
                html = urllib.request.urlopen(handle).read().decode('utf-8')
                await self.bot.say("Here you go :link: " + html)
            elif "403892685473185792" == ctx.message.author.id:
                url = ("http://ouo.io/api/oS9w9Nae?s=" + ctx.message.content)
                handle = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
                html = urllib.request.urlopen(handle).read().decode('utf-8')
                await self.bot.say("Here you go :link: " + html)
            else:
                await self.bot.say("API key missing.")   
        else:
            await self.bot.say("You are not allowed to use this command.")

def setup(bot):
    bot.add_cog(Shorten(bot))

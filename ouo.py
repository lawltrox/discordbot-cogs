import discord
import urllib.request
import requests
from discord.ext import commands

class Shorten:

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ouo(self, url):

        url = ("http://ouo.io/api/B3Nm9g8L?s=" + url)
        handle = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        html = urllib.request.urlopen(handle).read()
        await self.bot.say("Shortened: " + html)


def setup(bot):
    bot.add_cog(Shorten(bot))
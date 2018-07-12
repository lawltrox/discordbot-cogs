import discord
import urllib.request
import requests
from discord.ext import commands

class Shorten:

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ouo(self, url):

<<<<<<< HEAD
        url2 = ("http://ouo.io/api/B3Nm9g8L?s=" + url)
        handle = urllib.request.Request(url2, headers={'User-Agent': 'Mozilla/5.0'})
        html = urllib.request.urlopen(handle).read().decode('utf-8')
=======
        url = ("http://ouo.io/api/APIKEY?s=" + url)
        handle = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        html = urllib.request.urlopen(handle).read()
>>>>>>> bc2bd8c05d9f486237a25f7f0c481660e8b39816
        await self.bot.say("Shortened: " + html)

def setup(bot):
    bot.add_cog(Shorten(bot))

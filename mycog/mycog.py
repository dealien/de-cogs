import discord
from discord.ext import commands

try: # Check if BeautifulSoup4 is installed
    from bs4 import BeautifulSoup
    soupAvailable = True
except:
    soupAvailable = False
import aiohttp
import browser_cookie3

def setup(bot):
    if soupAvailable:
        bot.add_cog(Mycog(bot))
    else:
        raise RuntimeError("You need to run `pip3 install beautifulsoup4`")

class Mycog:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def mycom(self):
        """This does stuff!"""

        # Command function
        await self.bot.say("I can do stuff!")

    @commands.command()
    async def punch(self, user : discord.Member):
        """I will puch anyone! >.<"""

        # Command function
        await self.bot.say("ONE PUNCH! And " + user.mention + " is out! ლ(ಠ益ಠლ)")

    # @commands.command()
    # async def gtakd(self):
    #     """Check the kill-death ratio of a player in Grand Theft Auto: Online"""

    #     # Command function
    #     # Build the web address
    #     url = "https://socialclub.rockstargames.com/member/--zephyr--/games/gtav/pc/career/stats/gtaonline/career"
    #     async with aiohttp.get(url) as response:
    #     soupObject = BeautifulSoup(await response.text(), "html.parser")
    #     print soupObject
    #     try:
    #         online = soupObject.find(class_='home-stats').find('li').find('strong').get_text()
    #         await self.bot.say(online + ' players are playing this game at the moment')
    #     except:
    #         await self.bot.say("Couldn't load data.")
    
    @commands.command()
    async def gtakd(self):
        """Check the kill-death ratio of a player in Grand Theft Auto: Online"""

        # Your code will go here
        url = "https://socialclub.rockstargames.com/member/--zephyr--/games/gtav/pc/career/stats/gtaonline/career"
        cookiedata = dict(rockstarweb_lang.prod='en', CSRFToken='nq4_lk7c1Zvq_BAIgXoMzY4hlIExTYcSdAz10UlcOGDTaT9mD0QVKKWaUmfTCkgHtfWBFiV6pe5coQ9s6jmhsep5ha81')
        async with aiohttp.get(url, cookies=cookiedata) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        await self.bot.say(soupObject)
        try:
            ratio = soupObject.find('td', text = re.compile('^(Player vs Player Kill / Death ratio)$')).next.get_text()
            
            await self.bot.say(ratio + ' K/D')
        except:
            await self.bot.say("Couldn't load data.")


def setup(bot):
    bot.add_cog(Mycog(bot))
    
    

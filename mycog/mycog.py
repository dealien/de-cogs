import discord
from discord.ext import commands

try: # check if BeautifulSoup4 is installed
	from bs4 import BeautifulSoup
	soupAvailable = True
except:
	soupAvailable = False
import aiohttp

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

        #Your code will go here
        await self.bot.say("I can do stuff!")
    
    @commands.command()
    async def punch(self, user : discord.Member):
        """I will puch anyone! >.<"""

        #Your code will go here
        await self.bot.say("ONE PUNCH! And " + user.mention + " is out! ლ(ಠ益ಠლ)")
    
    @commands.command()
	async def gtakd(self):
	    """Check the kill-death ratio of a player in Grand Theft Auto: Online"""

	    #Your code will go here
	    url = "https://socialclub.rockstargames.com/member/--zephyr--/games/gtav/pc/career/stats/gtaonline/career" #build the web adress
	    async with aiohttp.get(url) as response:
		soupObject = BeautifulSoup(await response.text(), "html.parser")
		print soupObject
	    try:
		online = soupObject.find(class_='home-stats').find('li').find('strong').get_text()
		await self.bot.say(online + ' players are playing this game at the moment')
	    except:
		await self.bot.say("Couldn't load amount of players. No one is playing this game anymore or there's an error.")

def setup(bot):
    bot.add_cog(Mycog(bot))

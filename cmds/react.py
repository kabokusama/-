import discord
from discord.ext import commands

from doluto.core.classes import Cog_Extension

class React(Cog_Extension):

    @commands.command()
    async def picture(self,ctx):
        pic = discord.File('D:\pic\live2D.png')
        await ctx.send(file=pic)

def setup(bot):
    bot.add_cog(React(bot))
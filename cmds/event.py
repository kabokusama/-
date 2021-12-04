import discord
import json
from discord.ext import commands

from doluto.core.classes import Cog_Extension

with open('setting.json','r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Event(Cog_Extension):
    
    @commands.Cog.listener()
    async def on_member_join(self,member):
        channel = self.bot.get_channel(int(jdata['test_channel']))
        await channel.send(F'{member} join!')

    @commands.Cog.listener()
    async def on_member_remove(self,member):
        channel = self.bot.get_channel(int(jdata['test_channel']))
        await channel.send(F'{member} leave!')
    
    @commands.Cog.listener()
    async def on_message(self,msg):
        if '自我介紹' in msg.content and msg.author != self.bot.user:
            await msg.channel.send("哈囉！大家好，我的名字叫朵爾忒，我是かぼく的女兒！(´∀`)")

def setup(bot):
    bot.add_cog(Event(bot))
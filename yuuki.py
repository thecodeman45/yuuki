import discord
from discord.ext import commands

client = discord.Client()
bot = commands.Bot(command_prefix='!', description="Hey there, I'm Yuuki!")

def sendResponse(text ,aType):
    print(text+" sent.\nAnswer type="+aType)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    sendResponse("Answer", "Text")

@bot.command()
async def sayhii(ctx):
    embeded = discord.Embed(title="Hi, hi!",
                            description="Hi! I'm Yuuki, the Minecraft server Manager. I do all sort of things. From changing the status, to manipulating the map! There are lots of things you can tell me to do. Here are some of my commands:\n\n!get_status\n!set_status\n!open_server\n!close_server\n!help\n\nI'll always be there to help!",
                            footer="Hope you have a nice day!",
                            colour=999)
    await ctx.send(embed=embeded)
    sendResponse("Answer", "Text")

@bot.event
async def on_ready():
    print("Hi, hi! I'm ready!")
    await bot.change_presence(activity=discord.Streaming(name="Yuuki", url="http://"))

bot.run('Nzc3MzQ0NDE4NDk1NzI1NTk4.X7CEZw.njGTw2N3sgLf1Nnktdop6KIpYdo')

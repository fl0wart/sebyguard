import discord
from discord.ext import commands
import asyncio

bot=commands.Bot(command_prefix='p!')
@bot.event
async def on_ready():
    print('Logged in as '+bot.user.name+' (ID:'+bot.user.id+') | Connected to '+str(len(bot.servers))+' servers | Connected to '+str(len(set(bot.get_all_members())))+' users')
    print('--------')
    await bot.change_presence(game=discord.Game(name="the criminals! 👀", type=3))

bot.remove_command('help')

@bot.command(pass_context = True)
@commands.has_permissions(administrator = True)
async def say(ctx, *args):
    mesg = ' '.join(args)
    await bot.delete_message(ctx.message)
    return await bot.say(mesg)

bot.run('NTU4MjA1MDQxOTA3OTkwNTI4.D3Tcig.erxYozqaEr6gZBqZfex-EWJ-7ik')

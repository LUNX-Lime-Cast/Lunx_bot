import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import datetime

load_dotenv()

uptimeVar = None

intents = discord.Intents.default()

intents.message_content = True

bot = commands.Bot(";", intents=intents, help_command=None)
copyright = "©Lunx Studios"

@bot.event
async def on_ready():
    global uptimeVar

    uptimeVar = datetime.datetime.now(datetime.UTC)
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")

    await bot.change_presence(
    status=discord.Status.online,
        activity=discord.Activity(
            type=discord.ActivityType.playing,
            name="Jokes on people"
        )
    )

@bot.event
async def on_command_error(ctx, error):
    embed = discord.Embed(title="❌ Error", color=discord.Color.red())

    if isinstance(error, commands.MemberNotFound):
        embed.description = "Couldn't find that member!"
    elif isinstance(error, commands.MissingRequiredArgument):
        embed.description = f"Missing argument: `{error.param.name}`"
    elif isinstance(error, commands.BadArgument):
        embed.description = "Invalid argument provided!"
    else:
        embed.description = f"An unexpected error occurred: `{error}`"

    embed.set_footer(text=copyright)
    await ctx.reply(embed=embed)



@bot.command()
async def ban(ctx, member: discord.Member, *, reason: str = "No reason provided"):
    embed = discord.Embed(
        title="🔨 User Banned!",
        description=f"**{member.display_name}** has been banned from the server!",
        color=discord.Color.red()
    )
    embed.add_field(name="Banned™ User", value=member.mention, inline=True)
    embed.add_field(name="Banned™ By", value=ctx.author.mention, inline=True)
    embed.add_field(name="Reason", value=reason, inline=False)
    embed.set_thumbnail(url=member.display_avatar.url)
    embed.set_footer(text=copyright)

    await ctx.reply(embed=embed)

@bot.command()
async def about(ctx):
    embed = discord.Embed(color=discord.Color.green(), title="About the Bot")
    embed.add_field(name="About",value=copyright, inline=True)
    embed.add_field(name="Source Code", value="https://github.com/evokerking1/Lunx_bot", inline=True)

    await ctx.reply(embed=embed)

@bot.command()
async def uptime(ctx):
    delta = datetime.datetime.now(datetime.UTC) - uptimeVar
    hours, remainder = divmod(int(delta.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)

    embed = discord.Embed(title="⏱️ Uptime", color=discord.Color.green())
    embed.description = f"`{days}d {hours}h {minutes}m {seconds}s`"
    embed.set_footer(text=copyright)

    await ctx.reply(embed=embed)

    
@bot.command()
async def help(ctx):
    embed = discord.Embed(title="📖 Commands", color=discord.Color.green())
    embed.add_field(name=";ban @user [reason]", value="Joke bans a user", inline=False)
    embed.add_field(name=";about", value="Shows info about the bot", inline=False)
    embed.add_field(name=";uptime", value="Shows how long the bot has been online", inline=False)
    embed.set_footer(text=copyright)
    await ctx.reply(embed=embed)

bot.run(os.getenv("TOKEN"))

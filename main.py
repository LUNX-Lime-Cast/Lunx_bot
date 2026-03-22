import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()

intents = discord.Intents.default()

intents.message_content = True

bot = commands.Bot(";", intents=intents)
copyright = "©Lunx Studios"

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")

    await bot.change_presence(
    status=discord.Status.online,
        activity=discord.Activity(
            type=discord.ActivityType.playing,
            name="Jokes on people"
        )
    )


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

bot.run(os.getenv("TOKEN"))

import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import datetime
import random
import asyncio

load_dotenv()

fake_passwords = [
    "password123",
    "qwerty",
    "iloveyou",
    "123456",
    "letmein",
    "monkey",
    "dragon",
    "sunshine",
    "princess",
    "football",
    "batman",
    "superman",
    "pokemon",
    "pikachu",
    "cheese",
    "burger",
    "pizza123",
    "hello123",
    "abc123",
    "trustno1",
    "starwars",
    "minecraft",
    "roblox123",
    "fortnite",
    "youwillneverguessthis",
    "correcthorsebatterystaple",
    "hunter2",
    "opensesame",
    "secretpassword",
    "iamthebest",
    "mymomisthebest",
    "ihavenoidea",
    "pleasedontban",
    "iliketrains",
]


kdf_firewall: bool = True

evoker_firewall: bool = True

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
    embed.add_field(name="Source Code", value="https://github.com/LUNX-Lime-Cast/Lunx_bot", inline=True)

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
async def explode(ctx, user: discord.Member):
    await ctx.reply(content=f"thine have been explode {user.mention} stupid biatch sucka [blait](https://c.tenor.com/KPr-5NNM3JAAAAAC/tenor.gif)")

    
@bot.command()
async def help(ctx):
    embed = discord.Embed(title="📖 Commands", color=discord.Color.green())
    embed.add_field(name=";ban @user [reason]", value="Joke bans a user", inline=False)
    embed.add_field(name=";about", value="Shows info about the bot", inline=False)
    embed.add_field(name=";uptime", value="Shows how long the bot has been online", inline=False)
    embed.add_field(name="sudo", value=";sudo <heck/steal/virus/poweroff> <user>", inline=False)
    embed.add_field(name=";explode", value="Explodes a user", inline=False)
    embed.set_footer(text=copyright)
    await ctx.reply(embed=embed)

@bot.group()
async def sudo(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.reply("Usage: `;sudo <heck/steal/virus/poweroff>`")

DEFLECT_ROLE_ID = 1480252110217150626

@sudo.command()
async def heck(ctx, member: discord.Member):
    msg = await ctx.reply(f"🔓 Hacking {member.display_name}...")
    await asyncio.sleep(2)
    deflect_role = discord.utils.get(member.roles, id=DEFLECT_ROLE_ID)
    if deflect_role:
        await msg.exit(content=f"User {member.mention} has a firewall and the attack rebounds on you")
        await asyncio.sleep(2)
        await msg.edit(content=f"💾 Downloading {ctx.author.display_name}'s data...")
        await asyncio.sleep(2)
        await msg.edit(content=f"🔑 Cracking password...")
        await asyncio.sleep(random.randint(1, 5))

        if random.random() < 0.4:
            await msg.edit(content=f"❌ Hack failed! {ctx.author.mention} was too powerful... 💀")
            return
        else:
            password = random.choice(fake_passwords)
            await msg.edit(content=f"✅ Successfully hacked {ctx.author.mention}!\nPassword was:    `{password}`")
            return
    if member.id == 1485037805120913608:
        await msg.edit(content="❌ I refuse to hack myself!")
        return
    if member.id == 1188797524111265822:
        await msg.edit(content=f"User {member.mention} has a firewall and the attack rebounds on you")
        await asyncio.sleep(2)
        await msg.edit(content=f"💾 Downloading {ctx.author.display_name}'s data...")
        await asyncio.sleep(2)
        await msg.edit(content=f"🔑 Cracking password...")
        await asyncio.sleep(random.randint(1, 5))

        if random.random() < 0.4:
            await msg.edit(content=f"❌ Hack failed! {ctx.author.mention} was too powerful... 💀")
            return
        else:
            password = random.choice(fake_passwords)
            await msg.edit(content=f"✅ Successfully hacked {ctx.author.mention}!\nPassword was:    `{password}`")
            return
    elif member.id == 692104910229078066:
        await msg.edit(content=f"User {member.mention} has a firewall and the attack rebounds on you")
        await asyncio.sleep(2)
        await msg.edit(content=f"💾 Downloading {ctx.author.display_name}'s data...")
        await asyncio.sleep(2)
        await msg.edit(content=f"🔑 Cracking password...")
        await asyncio.sleep(random.randint(1, 5))

        if random.random() < 0.4:
            await msg.edit(content=f"❌ Hack failed! {ctx.author.mention} was too powerful... 💀")
        else:
            password = random.choice(fake_passwords)
            await msg.edit(content=f"✅ Successfully hacked {ctx.author.mention}!\nPassword was:    `{password}`")
            return
    await msg.edit(content=f"💾 Downloading {member.display_name}'s data...")
    await asyncio.sleep(2)
    await msg.edit(content=f"🔑 Cracking password...")
    await asyncio.sleep(random.randint(1, 5))

    if random.random() < 0.4:
        await msg.edit(content=f"❌ Hack failed! {member.mention} was too powerful... 💀")
    else:
        password = random.choice(fake_passwords)
        await msg.edit(content=f"✅ Successfully hacked {member.mention}!\nPassword was: `{password}`")



@sudo.command()
async def steal(ctx, member: discord.Member):
    fake_ip = f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}"
    embed = discord.Embed(title="🌐 IP Stolen!", color=discord.Color.red())
    embed.add_field(name="Victim", value=member.mention)
    embed.add_field(name="IP Address", value=f"`{fake_ip}`")
    embed.set_footer(text=copyright)
    await ctx.reply(embed=embed)

@sudo.command()
async def virus(ctx, member: discord.Member):
    msg = await ctx.reply(f"📤 Sending virus to {member.mention}...")
    await asyncio.sleep(2)
    await msg.edit(content=f"Starting virus...")
    await asyncio.sleep(2)
    await msg.edit(content=f"⚠️ Virus installed on {member.display_name}'s PC!\n`C:\System32` and `/` has been deleted 💀")

@sudo.command()
async def poweroff(ctx, member: discord.Member):
    msg = await ctx.reply(f"📤 Powering off {member.mention}'s computer...")
    await asyncio.sleep(2)
    await msg.edit(content=f"⚠️ Powered off {member.mention}'s computer...")

@bot.group()
async def admin(ctx):
    if ctx.author.id != 692104910229078066:
        ctx.reply("❌ You cant run this command!!")
        return
    return
        

bot.run(os.getenv("TOKEN"))

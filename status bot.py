import discord
from discord.ext import commands

# Do not remove credits or you will be sued by me bitches :-)
token = 'token here gay ass'

client = commands.Bot(command_prefix=",")
client.remove_command('help')

@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))
    await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game(f",help"))


@client.command()
async def help(ctx):
  embed = discord.Embed(title = "Help Center Public Status BOT by Purge", description = "All commands of this bot is displayed here!")
  embed.add_field(name = "Status Bot", value = "Commands: up and down")
  await ctx.send(embed=embed)

@client.command()
async def up(ctx):
	embed = discord.Embed(title="Status")
	embed.add_field(name = "UP", value = "This does not open the exe or shows online only text.")
	await ctx.send(embed=embed)


@client.command()
async def down(ctx):
	embed = discord.Embed(title="Status")
	embed.add_field(name = "Down", value = "This does not close the exe or shows online only text.")
	await ctx.send(embed=embed)

client.run(token)
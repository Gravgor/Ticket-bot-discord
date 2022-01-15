from asyncio.tasks import current_task
import discord
from discord import Embed
from discord import embeds
from discord import channel
from discord import colour
from discord import message
from discord.ext import commands
from discord.ext.commands import command
from discord.ext.commands.cooldowns import BucketType
from discord.ext.commands import Cog
from discord.utils import get
import datetime

bot = commands.Bot(command_prefix="!",case_insensitive=True)


@bot.command()







async def ticket(ctx):
    guild = ctx.message.guild
    author = ctx.author
    content = ["Ticket"]
    channels = await guild.fetch_channels()
    category = discord.utils.get(channels, name='Tickets')
    default_role = discord.utils.get(guild.roles,name="@everyone")
    embed = discord.Embed(title='Wybierz emotkę na dole, żeby otworzyć ticket. Masz dziesięć sekund, żeby zareagować na emotkę w innym wypadku twoja prośba o ticket zostanie usunięta.',color=0x5cbac4)
    msg = await ctx.send(embed=embed)

    await msg.add_reaction("\N{HEAVY CHECK MARK}")

    def check(reaction,user):
        return user == ctx.author and str(reaction.emoji) in ["\N{HEAVY CHECK MARK}"]


    while True:
      try:
          reaction, user = await bot.wait_for("reaction_add", timeout=10, check=check)

          if str(reaction.emoji) == "\N{HEAVY CHECK MARK}":
              channel = await guild.create_text_channel(f'Ticket uzytkownika-{author}',category=category)
              await channel.set_permissions(author,read_messages=True,send_messages=True)
              await channel.set_permissions(default_role,read_messages=False)





              embed = discord.Embed(title="Wypisz tutaj swoje wszystkie życzenia dotyczące zamówienia, odezwie się do Ciebie ktoś z dev team, żeby ustalić szczegóły.",color=0x5cbac4)
              await channel.send(embed=embed)


            

    

              await msg.remove_reaction(reaction, user)
              await msg.delete()
              await ctx.message.delete()

          else:
              await msg.remove_reaction(reaction,user)

      except:
          await msg.delete()
          break











bot.run("")

import os
from dotenv import load_dotenv
from discord.ext import commands
import datetime

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix="!") #Bot prefix

@bot.command(name="suma")
async def sumar(ctx, n1, n2):
    response = int(n1) + int(n2)
    await ctx.send(response)

@bot.command(name="votacion")
async def sumar(ctx, motivo):
    response = f"""Se procede a votar: {motivo} - {datetime.date.today()}.
                Contestad a este mensaje con:
                 :o: si estais a favor. 
                 :x: si estais en contra. 
                 :white_circle: para absteneros."""
    await ctx.send(response)

@bot.command(name="ayuda")
async def ayuda(ctx):
    response = """Alea_Bot dispone de los siguientes comandos:
    !votacion: Introduce el motivo de la votación para iniciarla y que Alea_Bot lleve el recuento automático.
    !suma: Introduce dos numeros enteros separados por espacio y Alea_Bot los sumará."""
    await ctx.send(response)

bot.run(TOKEN)
import bs4_meal
import station
import disnake
from disnake.ext import commands
import asyncio
import os

BOT_TOKEN = ""
bot = commands.Bot()

@bot.event
async def on_ready():
    print("The bot is ready!")

@bot.slash_command()
async def 열차시간(inter):
    try:
        station()
    except Exception as e:
        await inter.response.send_message(f"오류가 발생했습니다...!: {e}")

@bot.slash_command()
async def 학식(inter):
    try:
        bs4_meal()
    except Exception as e:
        await inter.response.send_message(f"오류가 발생했습니다...!: {e}")


bot.run(BOT_TOKEN)
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
async def 수인분당열차시간(inter):
    try:
        await inter.response.send_message("미완성")



    except Exception as e:
        await inter.response.send_message(f"오류가 발생했습니다...!: {e}")

@bot.slash_command()
async def 수도권4호선열차시간(inter):
    try:
        await inter.response.send_message("미완성")



    except Exception as e:
        await inter.response.send_message(f"오류가 발생했습니다...!: {e}")

@bot.slash_command()
async def tip학식(inter):
    try:
        bs4_meal.get_meal()
        file_path_tip = './0.jpg'
        img_file_tip = disnake.File(file_path_tip)
        await inter.response.send_message(file=img_file_tip)
    except Exception as e:
        await inter.response.send_message(f"오류가 발생했습니다...!: \n {e}")

@bot.slash_command()
async def e동학식(inter):
    try:
        bs4_meal.get_meal()
        file_path_E = "./1.jpg"
        img_file_E = disnake.File(file_path_E)
        await inter.response.send_message(file=img_file_E)
    except Exception as e:
        await inter.response.send_message(f"오류가 발생했습니다...!: \n {e}")


bot.run(BOT_TOKEN)
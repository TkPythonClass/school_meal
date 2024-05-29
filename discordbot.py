import bs4_meal
import station
import disnake
from disnake.ext import commands
from disnake import File
import asyncio
from dotenv import load_dotenv
from cmath import log
from distutils.sysconfig import PREFIX
import os
load_dotenv()

BOT_TOKEN = os.environ["TOKEN"]
bot = commands.Bot()

@bot.event
async def on_ready():
    print("The bot is ready!")

@bot.slash_command()
async def 막차시간(inter, * , line):

    await inter.response.defer()

    try:
        embed = disnake.Embed(title="정왕역 막차", color=0x00ff00)

        real_last_canival = station.station(line)
        for canival in real_last_canival:
            embed.add_field(name="\u200b", value=str(canival), inline=False)


        await inter.edit_original_response(embed=embed)


    except Exception as e:
        await inter.edit_original_response(content=f"오류가 발생했습니다...!: {e}")

@bot.slash_command()
async def tip학식(inter):
    try:
        bs4_meal.get_meal()
        file_path_tip = './0.jpg'
        img_file_tip = disnake.File(file_path_tip)

        await inter.response.send_message("## 금주 TIP 지하 학식입니다!", file=img_file_tip)
    except Exception as e:
        await inter.response.send_message(f"오류가 발생했습니다...!: \n {e}")

@bot.slash_command()
async def e동학식(inter):
    try:
        bs4_meal.get_meal()
        file_path_E = "./1.jpg"
        img_file_E = disnake.File(file_path_E)

        await inter.response.send_message("## 금주 E동 학식입니다!", file=img_file_E)
    except Exception as e:
        await inter.edit_original_response(f"오류가 발생했습니다...!: \n {e}")



bot.run(BOT_TOKEN)
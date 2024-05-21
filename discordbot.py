import bs4_meal
import station
import discord
from discord.ext import commands
import asyncio
import os

BOT_TOKEN = "MTI0MjAyMjI1MzU2NzQxNDM1Mg.GUBmZ6.ebfuOxvX8h5Ope01QsZmd7jjlIafHfz8j7X0co"

intents = discord.Intents.default()
intents.reactions = True
bot = commands.Bot(command_prefix="/", intents=intents)

# 봇 상태 출력
@bot.event
async def on_ready():
    print("The bot is ready!")


# 기본 메세지 출력 코드
@bot.command(name="")
async def 테스트(inter):
    await inter.response.send_message("작동중")

@bot.slash_command()
async def 막차시간(inter):
    emojis = ['1️⃣', '2️⃣']
    route_num = ['1', '2']

    message = await inter.channel.send('원하는 노선을 눌러주세요! (1 = 정왕역4호선막차, 2 = 정왕역수인분당선막차)')
    for emoji in emojis:
        await message.add_reaction(emoji)

    def check(reaction, user):
        return user == inter.author and str(reaction.emoji) in emojis

    try:
        reaction, _ = await bot.wait_for('reaction_add', timeout=30.0, check=check)

        index = emojis.index(str(reaction.emoji))
    except asyncio.TimeoutError:
        await inter.response.send_message('시간이 초과되었습니다. 다시 시도해주세요.')

@bot.slash_command()
async def 학식(inter):
    await inter.response.send_message("a")

# 깃허브 Public에 봇토큰을 올리지 못함. -> Private에 올리면 상관없음
bot.run(BOT_TOKEN)
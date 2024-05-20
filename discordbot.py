import disnake
from disnake.ext import commands

bot = commands.Bot()

# 봇 상태 출력
@bot.event
async def on_ready():
    print("The bot is ready!")


# 기본 메세지 출력 코드
@bot.slash_command()
async def test(inter):
    await inter.response.send_message("작동중")

# 깃허브 Public에 봇토큰을 올리지 못함. -> Private에 올리면 상관없음
bot.run(BOT_TOKEN)
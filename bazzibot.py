import discord
import os


client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("준비완료")
    game = discord.Game("@도움말로 확인")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.content.startswith("@안녕"):
        await message.channel.send("하이")
    if message.content.startswith("@도움말"):
        await message.channel.send("배불룩배찌, 제작, 안녕, 오늘의 날씨, play (현재 개발중)")
    if message.content.startswith("@제작"):
        await message.channel.send("배찌★#8008")
    if message.content.startswith("@오늘의 날씨"):
        await message.channel.send("https://weather.naver.com/")
    if message.content.startswith("@배불룩배찌"):
        await message.channel.send("https://www.youtube.com/channel/UCDuwrfmdvP9e4pcl-Ew1S0w")









access_token = os.environ["BOT_TOKEN"]
client.run(access_token)

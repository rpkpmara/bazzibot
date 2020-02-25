import discord
import os
import asyncio


client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("준비완료")
    await client.change_presense(game=discord.Game(name=봇테스트중, type=1))
   
    


@client.event
async def on_message(message):
    if message.author.bot:
        return None
    if message.content.startswith("@안녕"):
        await client.channel.send(channel, "하이")
    if message.content.startswith("@도움말"):
        await client.channel.send(channel, "안녕, 오늘의 날씨 배불룩배찌")
    if message.content.startswith("@제작"):
        await client.channel.send(channel, "배찌★#8008")
    if message.content.startswith("@오늘의 날씨"):
        await client.channel.send(channel, "weather.naver.com")
    if message.content.startswith("@배불룩배찌"):
        await client.channel.send(channel, "https://www.youtube.com/channel/UCDuwrfmdvP9e4pcl-Ew1S0w")









access_token = os.environ["BOT_TOKEN"]
client.run(access_token)

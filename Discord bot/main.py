import discord
import os
from dotenv import load_dotenv
import pandas_datareader as web


client=discord.Client()
load_dotenv()
TOKEN=os.getenv('TOKEN')

def get_stock_price(ticker):
  data=web.DataReader(ticker,"yahoo")
  return data['Close'].iloc[-1]

@client.event
async def on_message(message):
  if message.author==client.user:
    return
  if message.content.startswith('$hello'):
    await message.channel.send("Hello World! We are currently recording the video")
  if message.content == '$private':
    await message.author.send("Hello in Private DM!")
  if message.content.startswith('$stockprice'):
    if len(message.content.split(" "))==2:
      ticker=message.content.split(" ")[1]
      get_stock_price(ticker)
      await message.channel.send(f"Stock price of {ticker} is {price}!")

@client.event
async def on_connect():
  print("Bot connected to the server!!")
  channel=client.get_channel(172357282682749237482)
  await channel.send("Just connected to bot-commands!")

@client.event
async def on_member_join(member):
  await member.create_dm()
  await member.dm_channel.send(f"Welcome to the server {member}")

client.run(TOKEN)

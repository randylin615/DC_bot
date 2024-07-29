# -*- coding: utf-8 -*-
"""
Created on Fri May  5 19:52:22 2023

@author: randy
"""

#spyder asyncio必須使用
import nest_asyncio
nest_asyncio.apply()

import discord
import edge_tts

# ============================================================================= DC setting
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
# =============================================================================


# ============================================================================= TTS setting
voice = 'zh-CN-YunxiNeural'
output = 'text2voicetest.mp3'
rate = '-8%'
volume = '-5%'
# =============================================================================

bot_channel = ''
voiceclient = ''
@client.event
async def on_ready():
    print('目前登入身份：',client.user)
    game = discord.Game('這個男人太狠了')
    await client.change_presence(status=discord.Status.idle, activity=game)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.channel.name == '史丹利':
# ============================================================================= stock part
        if message.content == '!stock':
            await message.channel.send(file=discord.File('test.png'))
            return
# =============================================================================

# ============================================================================= voice channel & TTS part
        if message.author.voice.channel.name != None:
            voicechannel = message.author.voice.channel
            global bot_channel
            global voiceclient
            if bot_channel == '':
                voicechannel = message.author.voice.channel
                bot_channel = voicechannel.name
                voiceclient = await voicechannel.connect()
            elif bot_channel != voicechannel.name:
                voiceclient = await voiceclient.disconnect()
                voicechannel = message.author.voice.channel
                bot_channel = voicechannel.name
                voiceclient = await voicechannel.connect()
                
            tts = edge_tts.Communicate(text=message.content, voice=voice, rate=rate, volume=volume)
            await tts.save(output)
            await voiceclient.play(discord.FFmpegPCMAudio('text2voicetest.mp3'))
# =============================================================================

client.run('bot_token')




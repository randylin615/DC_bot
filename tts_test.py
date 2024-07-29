# -*- coding: utf-8 -*-
"""
Created on Fri May  5 21:03:40 2023

@author: randy
"""
import nest_asyncio
nest_asyncio.apply()

import edge_tts
import asyncio

TEXT = "阿洧 喵哈囉"
voice = 'zh-CN-XiaoyiNeural'
output = 'text2voicetest.mp3'
rate = '-4%'
volume = '+0%'

async def my_function():
    tts = edge_tts.Communicate(text=TEXT, voice=voice, rate=rate, volume=volume)
    await tts.save(output)
    
if __name__ == '__main__':
    asyncio.run(my_function())
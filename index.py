# -*- coding: utf-8 -*-
from pyrogram import Client, filters
import re

api_id = 14525194
api_hash = "4f07f80f1024e8ddd9938fad93368b24"
app = Client('my_account',api_id=api_id, api_hash=api_hash)
debug = True

with open('chat_id.txt','r') as file:
	chat_id = int(file.read())

@app.on_message(filters.channel|filters.group)
async def forward_message(client,message):
	print(message.text,message.chat.id)
	if int(message.chat.id) == int(chat_id):
		return

	if message.reply_markup or len(re.findall('https://',message.text)) > 2:
		await message.forward(chat_id=chat_id)
		print('done')



app.run()
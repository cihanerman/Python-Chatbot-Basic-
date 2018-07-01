# -*- coding: utf-8 -*-
# encoding=utf8
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')

bot = ChatBot('Deneme')
bot.set_trainer(ListTrainer)

for _file in os.listdir('text'):
    texts = open('text/' + _file, 'r').readlines()
    bot.train(texts)

while True:
    request = raw_input('Sen :')
    response = bot.get_response(request)
    print 'Bot: ', response
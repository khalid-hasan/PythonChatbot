from chatterbot import ChatBot
# from chatterbot.trainers import ListTrainer
import os

bot = ChatBot(
    'Bot',
    trainer='chatterbot.trainers.ListTrainer'
    )


for files in os.listdir('./data/'):
    data= open('./data/' + files, 'r' ).readlines()
    bot.train(data)

def get_response(message):
    while True:
        #message= input('You:')
        if message.strip() != 'Bye' :
            result = bot.get_response(message)
            reply = str(result)
            return reply
            #print('ChatBot :', reply)

        if message.strip() == 'Bye' :
            return ('Bye')
            break

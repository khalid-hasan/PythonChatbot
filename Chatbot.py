from chatterbot import ChatBot
# from chatterbot.trainers import ListTrainer
import os

bot = ChatBot(
    'Bot',
    trainer='chatterbot.trainers.ListTrainer'
    )


for files in os.listdir('H:/Work/Python/PythonChatbot/data/'):
    data= open('H:/Work/Python/PythonChatbot/data/' + files, 'r' ).readlines()
    bot.train(data)

while True:
    message= input('You:')
    if message.strip() != 'Bye' :
        reply= bot.get_response(message)
        print('ChatBot :', reply)

    if message.strip() == 'Bye' :
        print('ChatBot : Bye')
        break



from dotenv import load_dotenv
import os
import telebot
import random

load_dotenv()

bot_token = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(bot_token)

string_array = ["time" , "year" , "people" , "way" , "day" , "man" , "thing" , "woman" , "life" , "child" , "world" , "school" , "state" , "family" , "student" , "group" , "country" , "problem" , "hand" , "part" , "place" , "case" , "week" , "company" , "system" , "program" , "question" , "work" , "government" , "number" , "night" , "point" , "home" , "water" , "room" , "mother" , "area" , "money" , "story" , "fact" , "month" , "lot" , "right" , "study" , "book" , "eye" , "job" , "word" , "business" , "issue" , "side" , "kind" , "head" , "house" , "service" , "friend" , "father" , "power" , "hour" , "game" , "line" , "end" , "member" , "law" , "car" , "city" , "community" , "name" , "president" , "team" , "minute" , "idea" , "kid" , "body" , "information" , "back" , "parent" , "face" , "others" , "level" , "office" , "door" , "health" , "person" , "art" , "war" , "history" , "party" , "result" , "change" , "morning" , "reason" , "research" , "girl" , "guy" , "moment" , "air" , "teacher" , "force" , "education"]

friends_word = string_array[random.randint(0,99)]
friends = 0
user_id = []

@bot.message_handler(commands=['start'])
def partecipate(message):
    bot.reply_to(message, 'Welcome to this game. Use /partecipate for join the lobby and /startgame for start the game.' )
   

@bot.message_handler(commands=['partecipate'])
def partecipate(message):
    global friends
    if message.from_user.id in user_id:
        bot.reply_to(message, 'Your ID is already added to this lobby' )
    else:
        user_id.append(message.from_user.id)
        bot.reply_to(message, f'Hello, @{message.from_user.username}! You are the number {friends+1} in queue. When your other friends joined the lobby with the /partecipate command you can start the game using /startgame command.' )
        friends = friends + 1

@bot.message_handler(commands=['startgame'])
def startgame(message):
    global friends, friends_word, user_id
    if friends == 0:
        bot.reply_to(message, 'Use the /participate command before starting the game.' ) 
    elif friends == 1:
        bot.reply_to(message, 'I am sorry but you can not play this game alone. You can play when every friends has done the /partecipate command.' ) 
    else:
        random_num = random.randint(0,friends-1)
        #impostor = user_id[random_num]
        for index, value in enumerate(user_id):
            if index == random_num:
                bot.send_message(chat_id=user_id[index], text='You are the impostor! Try to guess the word I gave to the other people.')
            else:
                bot.send_message(chat_id=user_id[index], text=f'You are a friend! The word is \'{friends_word}\'.')

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, 'This command is not valid. Please read the istructions and follow them to play this game.')

bot.infinity_polling()
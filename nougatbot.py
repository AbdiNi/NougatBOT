import os
import random
import discord
from dotenv import load_dotenv
import pymongo
import nltk
from nltk.stem import WordNetLemmatizer
from nltk import word_tokenize
from nltk.corpus import stopwords
import string

load_dotenv()
client = discord.Client()

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["NougatBD2"]
mycol = mydb["astro2"]

myquery1 = { "PostTypeId": 1 }
questions = mycol.find(myquery1)

liste_questions=[]
for q in questions : 
    liste_questions.append(q['question'])

myquery2 = { "PostTypeId": 2 }
reponses = mycol.find(myquery2)
liste_responses=[]
for rep in reponses : 
    liste_responses.append(rep['response'])


def tokenize(corpus):
    #Tokenization
    words=[]
    tokens = nltk.word_tokenize(corpus)
    words.append(tokens)
    flat_words = [item for sublist in words for item in sublist]
    stopW = stopwords.words('english')
    stopW.extend(set(string.punctuation))
    tokens_without_stopwords = [x for x in flat_words if x not in stopW]
    return tokens_without_stopwords


def check(liste, words): 
    res = []
    indexrep = -1 
    for index,substring in enumerate(liste): 
        k = [ w.lower() for w in words if w.lower() in substring.lower() ] 
        if (len(k) == len(words) ): 
            res.append(substring)
            indexrep=index           
    return indexrep 


@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')


@client.event
async def on_message(message):
    
    dic = {"hello": [" hello", " I'am here", "yes!"],
       "hi": [" hello", " I'am here", "yes!"],
       "hey": [" hello", " I'am here", "yes!"],
       "how are you" : ["My name is Nougat and I'm a chatbot ?","I'am a rabbit!"],
       "thank you" : ["you are welcome"],
       "thanks" : ["you are welcome"],
       "quit" : ["Bye take care. See you soon :)","Bye bye"],
       "bye" : ["Bye take care. See you soon :)","Bye bye"],
       "help": ["Hello, Im NougatBOT, i was created by AfrIcA agency to make a basic conversation with you, i can give you answers for your questions related to astronomy :)  ."]

        }  
    

    if message.author == client.user:
        return
    
    if message.content == 'raise-exception':
        raise discord.DiscordException
    
    if message.content.lower() in dic.keys():
        await message.channel.send(random.choice(dic[message.content.lower()]))
    
    else : 
        words = tokenize(message.content)
        print(words)
        ind = check(liste_questions, words)     
        print(ind)
        if(ind!=-1) : 

            reponse_f = liste_responses[ind]

            print(reponse_f)
            if (len(reponse_f)>1999) :
                reponse_ff = reponse_f[0:1995]
                reponse_ff += '...'
                await message.channel.send(reponse_ff)
            else : await message.channel.send(reponse_f)
        
        else: await message.channel.send('sorry, i don\'t have an answer for this question' )

        #quest = message.content  # a taper sur discord
        #question = "^"+ quest[0:200]
   
        # myquery = { "question": { "$regex": question } }
        # mydoc = mycol.find(myquery)
        # ansID = 0
        # for x in mydoc:
        #     print(x['question'])
        #     ansID = x['AcceptedAnswerId']

        # if ansID !=0 : 

        #     myquery = { "_id": ansID }
        #     mydoc = mycol.find(myquery)
        #     for x in mydoc:
        #         reponse = x['response']
        #         if (len(reponse)>1999) : 
        #             reponse = reponse[0:1999]
        #         await message.channel.send(reponse)
        #         ansID = 0

    
client.run('ODA4OTkwOTg3Mjk2NDQwMzYw.YCOlkQ.RWX_g18z_y7HeWw5838HFbndpbk')

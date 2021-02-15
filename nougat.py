import discord
from discord.ext import commands
import random
from nltk.chat.util import Chat, reflections


#import nest_asyncio

#nest_asyncio.apply()
#__import__('IPython').embed()


TOKEN = 'ODA4OTkwOTg3Mjk2NDQwMzYw.YCOlkQ.9BsXAfC02LhCzV3eBS3rSoRcZxw'


pairs = [
    [
        r"bonjour|salut|coucou",
        ["Bien le bonjour à toi","Bonjour","Salut","Coucou","Bonjour , je m'appelle Nougat!"]

    ],
    [
        r"nougat|nounou",
        ["Yes, I'am here","Yes","I'am ready"]

    ],
    [
        r"bom dia",
        ["Bom dia!"]

    ],
    [
        r"buenos dias|hola",
        ["Buenos dias!","hola!"]

    ],
   
    [
        r"guten morgen",
        ["Guten Morgen!"]

    ],
    
    [
        r"que peux-tu faire| ? faire |que fais-tu",
        ["Je peux répondre à des questions simples ou aller chercher des réponses plus éléborées", "Je peux vous saluer en plusieurs langues ou aller chercher l'information ","Je peux vous surprendre!","je peux répondre à des questions simples"]

    ],
    [
        r"comment ppouvez-vous me surprendre| comment",
        ["Je peux répondre à des questions simples ou aller chercher des réponses plus éléborées", "Je peux vous saluer en plusieurs langues ou aller chercher l'information ","je peux répondre à des questions simples "]

    ],
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?",]
    ],
     [
        r"what is your name ?",
        ["My name is Nougat and I'm a rabbitbot ?",]
    ],
    [
        r"sorry (.*)",
        ["Ihits alright","Its OK, never mind",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
        
    [
        r"quit|bye|good bye|see you later",
        ["BBye take care. See you soon :) ","It was nice talking to you. See you soon :)"]

    ],
    
]

chat = Chat(pairs, reflections)

class Nougatbot(commands.Bot):
    def __init__(self):
        
        super().__init__(command_prefix = "/")
   
    async def on_ready(self):
        print(f"{self.user.display_name} est connecté au serveur.")
 
    async def on_message(self, message):
        rabbit = chat.respond(message.content.lower())
        if message.author == self.user:
            return
        
        if rabbit:
            await message.channel.send(rabbit)
        else: 

            await message.channel.send("I didn't understand ...")

    
        if message.content.startswith("!del"):
            number = int(message.content.split()[1])
            messages = await message.channel.history(limit=number +1).flatten()

            for each_message in messages:
                await each_message.delete()


nougat_bot = Nougatbot()
nougat_bot.run(TOKEN)
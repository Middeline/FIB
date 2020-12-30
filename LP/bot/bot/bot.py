#imports necessaris per evaluar les expressions
import sys
import os
import pickle
import skyline as sky
from antlr4 import *
from cl.SkylineLexer import SkylineLexer
from cl.SkylineParser import SkylineParser
from EvalVisitor import EvalVisitor

# importa l'API de Telegram
from telegram.ext import Updater, CommandHandler
from telegram.ext import MessageHandler, Filters


diccionario = {}


# defineix una funció que saluda i que s'executarà quan el bot rebi el missatge /start
def start(update, context):
    #if 'dicc' not in context.user_data:
        #context.user_data['dicc'] = {}
    first_Name = update.message.from_user['first_name']
    context.bot.send_message(chat_id = update.effective_chat.id, text = "Hola " + first_Name + ", sóc el Bot Skyline. \nUtilitza la comanda /help per demanar-me ajuda")


def help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=
    "Aquestes són les comandes i funcions que tinc: \n\n"
    "/start: Inicia la conversa amb el Bot. \n"
    "/help: El Bot et contesta amb una llista de totes les possibles comandes i una breu documentació sobre el seu propòsit i ús. \n"
    "/author: El Bot escriu el nom complet de l'autora del projecte i seu correu electrònic oficial de la facultat.\n"
    "/lst: Mostra una llista amb els identificadors definits i la seva corresponent àrea.\n"
    "/clean: Esborra tots els identificadors definits.\n"
    "/save id: Guarda un skyline definit amb el nom id.sky.\n"
    "/load id: Carrega un skyline de l'arxiu id.sky."

    "\n\nPer crear skylines pots fer: \n\n"
    "* ID := (xmin, alçada, xmax) on xmin i xmax especifiquen la posició d'inici i final a la coordenada horizontal i alçada l'alçada de l'edifici. Ex: (1, 2, 3) \n"
    "* ID := [(xmin, alçada, xmax), ...] permet definir diversos edificis mitjançant una llista d'edificis simples. Ex: [(1, 2, 3), (3, 4, 6)]\n"
    "* ID := {n, h, w, xmin, xmax} construeix n edificis, cadascun d'ells amb una alçada aleatòria entre 0 i h, amb una amplada aleatòria entre 1 i w, i una posició d'inici i de final aleatòria entre xmin i xmax.\n\n"

    "\n\nPer a operar amb skylines usa les funcions:\n\n"
    "* skyline + skyline: unió\n"
    "* skyline * skyline: intersecció \n"
    "* skyline * N: replicació N vegades de l'skyline (vegeu exemple d'interacció).\n"
    "* skyline + N: desplaçament a la dreta de l'skyline N posicions.\n"
    "* skyline - N: desplaçament a l'esquerra de l'skyline N posicions.\n"
    "*  - skyline: retorna l'skyline reflectit.")


def author(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Autora: Carolina Middel Soria \nMail: carolina.middel@est.fib.upc.edu")


def lst(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Identificadors definits:")
    for i, s in diccionario.items():
        context.bot.send_message(chat_id=update.effective_chat.id, text="ID: "+i+" | area: "+str(s.area))


def clean(update, context):
    global diccionario
    diccionario = {}
    context.bot.send_message(chat_id=update.effective_chat.id, text="S'han esborrat tots els identificadors")


def save(update, context):
    try:
        id = context.args[0]
        user = update.effective_chat.id
        name = str(os.getcwd())+"/"+str(user)+"."+str(id)+".sky"
        file = open(name, 'wb')
        guardar = diccionario[id]
        pickle.dump(guardar, file)
        context.bot.send_message(chat_id=update.effective_chat.id, text="El id "+str(id)+" s'ha guardat correctament")

    except:
        context.bot.send_message(chat_id=update.effective_chat.id, text="id incorrecta")


def load(update, context):
    try:
        id = context.args[0]
        user = update.effective_chat.id
        name = str(os.getcwd())+"/"+str(user)+"."+str(id)+".sky"
        file = open(name, 'rb')
        diccionario[id] = pickle.load(file)
        context.bot.send_message(chat_id=update.effective_chat.id, text="El id "+str(id)+" s'ha carregat correctament")

    except:
        context.bot.send_message(chat_id=update.effective_chat.id, text="id incorrecta")


def visitor(update, context):
    msg = update.message.text
    input_stream = InputStream(msg)
    lexer = SkylineLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = SkylineParser(token_stream)
    tree = parser.root()

    global diccionario
    visitor = EvalVisitor(diccionario)
    s, dicc = visitor.visit(tree)
    diccionario = dicc

    al_am = "area: " + str(s.area) + "\nalçada: " + str(s.alcada)

    fitxer = s.matplot(s.skyline)

    context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo=open(fitxer, 'rb'))

    context.bot.send_message(chat_id=update.effective_chat.id, text=al_am)

# declara una constant amb el access token que llegeix de token.txt
TOKEN = open('token.txt').read().strip()

# crea objectes per treballar amb Telegram
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# indica que quan el bot rebi la comanda /start s'executi la funció start
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(CommandHandler('author', author))
dispatcher.add_handler(CommandHandler('lst', lst))
dispatcher.add_handler(CommandHandler('clean', clean))
dispatcher.add_handler(CommandHandler('save', save))
dispatcher.add_handler(CommandHandler('load', load))
dispatcher.add_handler(MessageHandler(Filters.text, visitor))

# engega el bot
updater.start_polling()


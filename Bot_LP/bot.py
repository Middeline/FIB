#imports necessaris per evaluar les expressions
import sys
import Skyline as sky
from antlr4 import *
from SkylineLexer import SkylineLexer
from SkylineParser import SkylineParser
from EvalVisitor import EvalVisitor


# importa l'API de Telegram
from telegram.ext import Updater, CommandHandler
from telegram.ext import MessageHandler, Filters

# defineix una funció que saluda i que s'executarà quan el bot rebi el missatge /start
def start(update, context):
    first_Name = update.message.from_user['first_name']
    context.bot.send_message(chat_id=update.effective_chat.id, text= "Hola "  + first_Name + ", sóc el Bot Skyline. \nUtilitza la comanda /help per demanar-me ajuda")

def help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=
    "/start: Inicia la conversa amb el Bot. \n"
    "/help: El Bot et contesta amb una llista de totes les possibles comandes i una breu documentació sobre el seu propòsit i ús. \n"
    "/author: El Bot escriu el nom complet de l'autora del projecte i seu correu electrònic oficial de la facultat.\n"
    "/lst: Mostra una llista amb els identificadors definits i la seva corresponent àrea.\n"
    "/clean: Esborra tots els identificadors definits.\n"
    "/save id: Guarda un skyline definit amb el nom id.sky.\n"
    "/load id: Carrega un skyline de l'arxiu id.sky.")

def author(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Autora: Carolina Middel Soria \nMail: carolina.middel@est.fib.upc.edu")

def lst(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="mostra els identificadors definits i la seva corresponent àrea.")

def clean(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="esborra tots els identificadors definits.")

def save(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="ha de guardar un skyline definit amb el nom id.sky.")

def load(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="ha de carregar un skyline de l'arxiu id.sky")

def visitor(update, context):
    msg = update.message.text
    input_stream = InputStream(msg)
    lexer = SkylineLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = SkylineParser(token_stream)
    tree = parser.root()

    dicc = {}
    s = sky.Skyline([])

    visitor = EvalVisitor(dicc)
    s, dicc = visitor.visit(tree)

    al_am = "area: " + str(s.area) + "\nalçada: "  + str(s.alcada)
    s.matplot()

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

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import sys
import os
from antlr4 import *
from cl.SkylineLexer import SkylineLexer
from cl.SkylineParser import SkylineParser
from TreeVisitor import TreeVisitor
import skyline
import pickle
# Dirección del bot: t.me/Sky_Line_Bot


# Definimos las funciones necesarias para los comandos:
def start(update, context):
    nom = update.effective_chat.first_name
    context.bot.send_message(chat_id=update.message.chat_id, text="Hola, %s!\nBenvingut al Skyline Bot" % nom)
    if 'skylines' not in context.user_data:
        context.user_data['skylines'] = {}
    context.user_data['started'] = True


def help(update, context):
    helptxt = '''
L’_skyline_ d’una ciutat mostra una vista horizontal dels seus edificis.
Aquest ChatBot t'ajuda a crear i manipular _Skylines_.

Pots controlar-me utilitzant les següents *comandes*:

/start - fa les inicialitzacions pertinents.
/author - dóna informacio sobre el meu creador.
/help - dóna la llista de comandes possibles.

/lst: mostra els identificadors definits i la seva corresponent àrea.
/clean: esborra tots els identificadors definits.
/save id: guarda un skyline definit amb el nom id.
/load id: carrega l'skyline definit amb el nom id.


*Sintaxi*
El llenguatge permet els tipus d’operacions següents:

* - Creació d’edificis:*
        Simple: (xmin, alçada, xmax) on xmin i xmax especifiquen la posició d’inici i final a la coordenada horizontal i alçada l’alçada de l’edifici. Ex: (1, 2, 3).
        Compostos: [(xmin, alçada, xmax), ...] permet definir diversos edificis mitjançant una llista d’edificis simples. Ex: [(1, 2, 3), (3, 4, 6)] o [(1, 1, 2), (1000000000000, 1, 1000000000001)].
        Aleatoris: {n, h, w, xmin, xmax} construeix n edificis, cadascun d’ells amb una alçada aleatòria entre 0 i h, amb una amplada aleatòria entre 1 i w, i una posició d’inici i de final aleatòria entre xmin i xmax.

* - Operadors d’skylines:*
        skyline + skyline: unió
        skyline * skyline: intersecció
        skyline * N: replicació N vegades de l’skyline.
        skyline + N: desplaçament a la dreta de l’skyline N posicions.
        skyline - N: desplaçament a l’esquerra de l’skyline N posicions.
        - skyline: retorna l’skyline reflectit.

El llenguatge admet l’ús d’identificadors i d’assignacions mitjançant l’operador :=. Els identificadors han de ser una lletra seguida de zero o més lletres o dígits.
    '''
    context.bot.send_message(chat_id=update.effective_chat.id, text=helptxt, parse_mode="Markdown")


def author(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="Skyline Bot\nPer: Federico Rubinstein\nfederico.rubinstein@est.fib.upc.edu")


def lst(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="Mostrant els identificadors definits i la seva corresponent àrea.")

    skylines = context.user_data['skylines']

    if not skylines:
        context.bot.send_message(chat_id=update.message.chat_id, text="No hi ha cap skyline assignat!")

    for k, sky in skylines.items():
        context.bot.send_message(chat_id=update.message.chat_id, text="ID: {}\nÀrea: {}".format(k, sky.getArea()))


def clean(update, context):
    context.user_data['skylines'] = {}
    context.bot.send_message(chat_id=update.message.chat_id, text="S'han esborrat tots els identificadors definits.")


def save(update, context):
    try:
        userID = update.effective_chat.id
        id = context.args[0]
        saveFile = "./data/"+str(userID)+"/"+id+".sky"
        d = context.user_data['skylines']
        skyline = d[id]

        context.bot.send_message(chat_id=update.message.chat_id, text="Guardant un skyline definit amb el id %s..." % id)

        if not os.path.exists(os.path.dirname(saveFile)):  # Fragment de codi (només el if) extret de: https://stackoverflow.com/questions/12517451/automatically-creating-directories-with-file-output
            os.makedirs(os.path.dirname(saveFile))

        pickle.dump(skyline, open(saveFile, "wb"))
    except Exception as e:
        print(e)
        context.bot.send_message(chat_id=update.message.chat_id, text="Has de proporcionar un id correcte!\nFes /help per a més informació")


def load(update, context):
    try:
        userID = update.effective_chat.id
        id = context.args[0]
        loadFile = "./data/"+str(userID)+"/"+id+".sky"
        d = context.user_data['skylines']

        context.bot.send_message(chat_id=update.message.chat_id, text="Carregant un skyline definit amb el id %s..." % id)
        d[id] = pickle.load(open(loadFile, "rb"))
        context.user_data['skylines'] = d
    except Exception as e:
        print(e)
        context.bot.send_message(chat_id=update.message.chat_id, text="Has de proporcionar un id correcte!\nFes /help per a més informació")


# Función para cuando lo que se escribe no es un comando:
def missatge(update, context):
    if 'started' in context.user_data and context.user_data['started'] == True:
        try:
            # Inicialització i interacció amb la gramàtica:
            input_stream = InputStream(update.message.text)
            lexer = SkylineLexer(input_stream)
            token_stream = CommonTokenStream(lexer)
            parser = SkylineParser(token_stream)
            tree = parser.root()

            # Obtenim el resultat de la operació:
            skylines = context.user_data['skylines']
            visitor = TreeVisitor(skylines)
            skyline, skylines = visitor.visit(tree)
            context.user_data['skylines'] = skylines  # Guardem el resultat

            # Retornem el resultat a l'usuari:
            fileName = skyline.getImage()
            if fileName == -1:  # S'ha intentat mostrar un skyline buit
                context.bot.send_message(chat_id=update.message.chat_id, text="💣 Error! 💣\nEl skyline és buit!")
            else:
                context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(fileName, 'rb'))
                context.bot.send_message(chat_id=update.message.chat_id, text="area: {}\nalçada: {}".format(skyline.getArea(), skyline.getAltura()))
                os.remove(fileName)

        except Exception as e:
            print(e)
            context.bot.send_message(chat_id=update.message.chat_id, text='💣 Error! 💣')
    else:
            context.bot.send_message(chat_id=update.message.chat_id, text='💣 Error! 💣')
            context.bot.send_message(chat_id=update.message.chat_id, text="Has d'iniciar el bot amb /start")


# declara una constant amb el access token que llegeix de token.txt
TOKEN = open('token.txt').read().strip()

# crea objecte per treballar amb Telegram
updater = Updater(token=TOKEN, use_context=True)

# Añadimos handlers para los comandos, que ejecutaran las respectivas funciones:
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('author', author))
updater.dispatcher.add_handler(CommandHandler('lst', lst))
updater.dispatcher.add_handler(CommandHandler('clean', clean))
updater.dispatcher.add_handler(CommandHandler('save', save))
updater.dispatcher.add_handler(CommandHandler('load', load))
updater.dispatcher.add_handler(MessageHandler(Filters.text, missatge))

# engega el bot
updater.start_polling()

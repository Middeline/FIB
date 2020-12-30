
# BOT SKYLINE
## Carolina Middel Soria
## LP, Curs 2019-2020

## El bot Skyline manipula areas d'edificis via un interpret

### Instal·lació / Prerrequisits

    Es pot usar la comanda:

    `pip install -r requirements.txt`

    Per a instalar els softwares/paquets necessaris

    python3
    antlr4-python3-runtime
    telegram
    python-telegram-bot
    matplotlib
    pickle


### Començant

  La compilació i execució del codi es podrà fer amb les comandes:

  -  `antlr4 -Dlanguage=Python3 -no-listener -visitor Skyline.g`
    Al directori cl, per a generar els parsers de la gramatica Skyline.

  - `python3 bot.py`
    Aquesta comanda l'executarem al terminal en el mateix directori principal. Aquest compilarà i executarà el codi per a poder probar el Bot Skyline

  - Per accedir al bot directament, feu servir aquest enllaç:
    http://t.me/skymiddelline_bot


### Codi
  En aquest apartat explicaré alguna de les coses que he implementat que no estaven especificades a l'enunciat.

  - Comanda */save* del bot
    Primerament havia de guardar un skyline a un arxiu id.sky. Però he trobat que té més sentit que es guardi per a cada usuari en concret, per aixo ara aquest es guardarà amb el nom user.id.sky



### Compiladors

  La gramatica es pot trobar al fitxer [Skyline.g] (cl/Skyline.g). Usant antlr4 es crearan alguns fitxers a la mateixa carpeta, necessaris per a poder recórrer-la. (però no serà necessari fer res amb ells).

  Els fitxers relevants de la gramatica es troben al directori principal, aquests són:

  [EvalVisitor.py](EvalVisitor.py) es un *tree visitor* (iterat amb AST). Quan se'l crida des de bot.py, li entra com a parametre un diccionari (taula de simbols) per a controlar les IDs dels Skylines sobre els que treballem.

  [skyline.py](skyline.py) és la classe que conté les funcions per a crear, unir, reflectir... els "edificis" que creem amb el bot. La classe Skyline té una llista de tuplas (el propi skyline), un atribut area i un atribut alçada en la seva creadora, per a poder representar l'skyline.



### Bot

  Un cop compilat i executat el fitxer bot.py. S'accedeix a Telegram i s'inicia la conversa amb el bot.
  Per a començar la conversació usa la comanda /start
  El bot indica totes les comandes i funcions amb la comanda /help.

  Per a començar a parlar amb el bot usa l'enllaç:

  [Skyline Bot](http://t.me/skymiddelline_bot)

### Reconeixaments

 Inspiració per als agoritmes de unio i interseccio, amb el pseudocodi de:
    https://www.geeksforgeeks.org/the-skyline-problem-using-divide-and-conquer-algorithm/#:~:text=The%20Skyline%20Problem%20using%20Divide%20and%20Conquer%20algorithm,sections%20that%20are%20not%20visible.

### Author

####Carolina Middel Soria

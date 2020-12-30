import os
os.system("antlr -Dlanguage=Python3 -no-listener -visitor .\cl\Skyline.g")
import sys
from antlr4 import *
from SkylineLexer import SkylineLexer
from SkylineParser import SkylineParser
from TreeVisitor import TreeVisitor
while True:
    input_stream = InputStream(input('? '))
    lexer = SkylineLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = SkylineParser(token_stream)
    tree = parser.root() 
    visitor = TreeVisitor()
    visitor.visit(tree)
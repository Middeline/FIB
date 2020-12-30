import sys
import skyline as sky
from antlr4 import *
from SkylineLexer import SkylineLexer
from SkylineParser import SkylineParser
from EvalVisitor import EvalVisitor

dicc = {}

while True:
    input_stream = InputStream(input('? '))
    lexer = SkylineLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = SkylineParser(token_stream)
    tree = parser.root()

    s = sky.Skyline([])

    visitor = EvalVisitor(dicc)
    s, dicc = visitor.visit(tree)
    print(dicc)
    print(s.skyline)
    print(s.alcada)
    print(s.area)

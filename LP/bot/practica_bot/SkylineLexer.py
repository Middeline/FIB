# Generated from Skyline.g by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\20")
        buf.write("I\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\3\2\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3")
        buf.write("\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\6\n\62\n\n\r\n\16\n")
        buf.write("\63\3\13\6\13\67\n\13\r\13\16\138\3\13\3\13\3\f\3\f\7")
        buf.write("\f?\n\f\f\f\16\fB\13\f\3\r\3\r\3\16\3\16\3\17\3\17\2\2")
        buf.write("\20\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write("\31\16\33\17\35\20\3\2\6\3\2\62;\5\2\13\f\17\17\"\"\4")
        buf.write("\2C\\c|\5\2\62;C\\c|\2K\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3")
        buf.write("\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2")
        buf.write("\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2")
        buf.write("\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\3\37\3\2\2\2\5")
        buf.write("\"\3\2\2\2\7$\3\2\2\2\t&\3\2\2\2\13(\3\2\2\2\r*\3\2\2")
        buf.write("\2\17,\3\2\2\2\21.\3\2\2\2\23\61\3\2\2\2\25\66\3\2\2\2")
        buf.write("\27<\3\2\2\2\31C\3\2\2\2\33E\3\2\2\2\35G\3\2\2\2\37 \7")
        buf.write("<\2\2 !\7?\2\2!\4\3\2\2\2\"#\7*\2\2#\6\3\2\2\2$%\7+\2")
        buf.write("\2%\b\3\2\2\2&\'\7.\2\2\'\n\3\2\2\2()\7]\2\2)\f\3\2\2")
        buf.write("\2*+\7_\2\2+\16\3\2\2\2,-\7}\2\2-\20\3\2\2\2./\7\177\2")
        buf.write("\2/\22\3\2\2\2\60\62\t\2\2\2\61\60\3\2\2\2\62\63\3\2\2")
        buf.write("\2\63\61\3\2\2\2\63\64\3\2\2\2\64\24\3\2\2\2\65\67\t\3")
        buf.write("\2\2\66\65\3\2\2\2\678\3\2\2\28\66\3\2\2\289\3\2\2\29")
        buf.write(":\3\2\2\2:;\b\13\2\2;\26\3\2\2\2<@\t\4\2\2=?\t\5\2\2>")
        buf.write("=\3\2\2\2?B\3\2\2\2@>\3\2\2\2@A\3\2\2\2A\30\3\2\2\2B@")
        buf.write("\3\2\2\2CD\7,\2\2D\32\3\2\2\2EF\7-\2\2F\34\3\2\2\2GH\7")
        buf.write("/\2\2H\36\3\2\2\2\6\2\638@\3\b\2\2")
        return buf.getvalue()


class SkylineLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    NUM = 9
    WS = 10
    IDENT = 11
    MULT = 12
    SUMA = 13
    RESTA = 14

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "':='", "'('", "')'", "','", "'['", "']'", "'{'", "'}'", "'*'", 
            "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>",
            "NUM", "WS", "IDENT", "MULT", "SUMA", "RESTA" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "NUM", "WS", "IDENT", "MULT", "SUMA", "RESTA" ]

    grammarFileName = "Skyline.g"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


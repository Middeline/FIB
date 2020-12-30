# Generated from Skyline.g by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\20")
        buf.write("e\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\3\2\3\2\3\2\3\3\3\3\5\3\30\n\3\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\5\4 \n\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\5\5+\n\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\7\5<\n\5\f\5\16\5?\13\5\3\6\3\6")
        buf.write("\3\6\5\6D\n\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b")
        buf.write("\3\b\3\b\7\bR\n\b\f\b\16\bU\13\b\3\b\3\b\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\2\3\b\n\2\4\6\b")
        buf.write("\n\f\16\20\2\2\2i\2\22\3\2\2\2\4\27\3\2\2\2\6\37\3\2\2")
        buf.write("\2\b*\3\2\2\2\nC\3\2\2\2\fE\3\2\2\2\16M\3\2\2\2\20X\3")
        buf.write("\2\2\2\22\23\5\4\3\2\23\24\7\2\2\3\24\3\3\2\2\2\25\30")
        buf.write("\5\b\5\2\26\30\5\6\4\2\27\25\3\2\2\2\27\26\3\2\2\2\30")
        buf.write("\5\3\2\2\2\31\32\7\r\2\2\32\33\7\3\2\2\33 \5\n\6\2\34")
        buf.write("\35\7\r\2\2\35\36\7\3\2\2\36 \5\b\5\2\37\31\3\2\2\2\37")
        buf.write("\34\3\2\2\2 \7\3\2\2\2!\"\b\5\1\2\"#\7\4\2\2#$\5\b\5\2")
        buf.write("$%\7\5\2\2%+\3\2\2\2&\'\7\20\2\2\'+\5\b\5\n(+\7\r\2\2")
        buf.write(")+\5\n\6\2*!\3\2\2\2*&\3\2\2\2*(\3\2\2\2*)\3\2\2\2+=\3")
        buf.write("\2\2\2,-\f\t\2\2-.\7\16\2\2.<\5\b\5\n/\60\f\7\2\2\60\61")
        buf.write("\7\17\2\2\61<\5\b\5\b\62\63\f\b\2\2\63\64\7\16\2\2\64")
        buf.write("<\7\13\2\2\65\66\f\6\2\2\66\67\7\17\2\2\67<\7\13\2\28")
        buf.write("9\f\5\2\29:\7\20\2\2:<\7\13\2\2;,\3\2\2\2;/\3\2\2\2;\62")
        buf.write("\3\2\2\2;\65\3\2\2\2;8\3\2\2\2<?\3\2\2\2=;\3\2\2\2=>\3")
        buf.write("\2\2\2>\t\3\2\2\2?=\3\2\2\2@D\5\f\7\2AD\5\16\b\2BD\5\20")
        buf.write("\t\2C@\3\2\2\2CA\3\2\2\2CB\3\2\2\2D\13\3\2\2\2EF\7\4\2")
        buf.write("\2FG\7\13\2\2GH\7\6\2\2HI\7\13\2\2IJ\7\6\2\2JK\7\13\2")
        buf.write("\2KL\7\5\2\2L\r\3\2\2\2MN\7\7\2\2NS\5\f\7\2OP\7\6\2\2")
        buf.write("PR\5\f\7\2QO\3\2\2\2RU\3\2\2\2SQ\3\2\2\2ST\3\2\2\2TV\3")
        buf.write("\2\2\2US\3\2\2\2VW\7\b\2\2W\17\3\2\2\2XY\7\t\2\2YZ\7\13")
        buf.write("\2\2Z[\7\6\2\2[\\\7\13\2\2\\]\7\6\2\2]^\7\13\2\2^_\7\6")
        buf.write("\2\2_`\7\13\2\2`a\7\6\2\2ab\7\13\2\2bc\7\n\2\2c\21\3\2")
        buf.write("\2\2\t\27\37*;=CS")
        return buf.getvalue()


class SkylineParser ( Parser ):

    grammarFileName = "Skyline.g"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':='", "'('", "')'", "','", "'['", "']'", 
                     "'{'", "'}'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'*'", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "NUM", "WS", "IDENT", "MULT", "SUMA", 
                      "RESTA" ]

    RULE_root = 0
    RULE_ini = 1
    RULE_assig = 2
    RULE_expr = 3
    RULE_creadora = 4
    RULE_simple = 5
    RULE_composta = 6
    RULE_aleatoria = 7

    ruleNames =  [ "root", "ini", "assig", "expr", "creadora", "simple", 
                   "composta", "aleatoria" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    NUM=9
    WS=10
    IDENT=11
    MULT=12
    SUMA=13
    RESTA=14

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class RootContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ini(self):
            return self.getTypedRuleContext(SkylineParser.IniContext,0)


        def EOF(self):
            return self.getToken(SkylineParser.EOF, 0)

        def getRuleIndex(self):
            return SkylineParser.RULE_root

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = SkylineParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self.ini()
            self.state = 17
            self.match(SkylineParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IniContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(SkylineParser.ExprContext,0)


        def assig(self):
            return self.getTypedRuleContext(SkylineParser.AssigContext,0)


        def getRuleIndex(self):
            return SkylineParser.RULE_ini

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIni" ):
                return visitor.visitIni(self)
            else:
                return visitor.visitChildren(self)




    def ini(self):

        localctx = SkylineParser.IniContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_ini)
        try:
            self.state = 21
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 19
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 20
                self.assig()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AssigContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(SkylineParser.IDENT, 0)

        def creadora(self):
            return self.getTypedRuleContext(SkylineParser.CreadoraContext,0)


        def expr(self):
            return self.getTypedRuleContext(SkylineParser.ExprContext,0)


        def getRuleIndex(self):
            return SkylineParser.RULE_assig

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssig" ):
                return visitor.visitAssig(self)
            else:
                return visitor.visitChildren(self)




    def assig(self):

        localctx = SkylineParser.AssigContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assig)
        try:
            self.state = 29
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 23
                self.match(SkylineParser.IDENT)
                self.state = 24
                self.match(SkylineParser.T__0)
                self.state = 25
                self.creadora()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 26
                self.match(SkylineParser.IDENT)
                self.state = 27
                self.match(SkylineParser.T__0)
                self.state = 28
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SkylineParser.ExprContext)
            else:
                return self.getTypedRuleContext(SkylineParser.ExprContext,i)


        def RESTA(self):
            return self.getToken(SkylineParser.RESTA, 0)

        def IDENT(self):
            return self.getToken(SkylineParser.IDENT, 0)

        def creadora(self):
            return self.getTypedRuleContext(SkylineParser.CreadoraContext,0)


        def MULT(self):
            return self.getToken(SkylineParser.MULT, 0)

        def SUMA(self):
            return self.getToken(SkylineParser.SUMA, 0)

        def NUM(self):
            return self.getToken(SkylineParser.NUM, 0)

        def getRuleIndex(self):
            return SkylineParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SkylineParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 32
                self.match(SkylineParser.T__1)
                self.state = 33
                self.expr(0)
                self.state = 34
                self.match(SkylineParser.T__2)
                pass

            elif la_ == 2:
                self.state = 36
                self.match(SkylineParser.RESTA)
                self.state = 37
                self.expr(8)
                pass

            elif la_ == 3:
                self.state = 38
                self.match(SkylineParser.IDENT)
                pass

            elif la_ == 4:
                self.state = 39
                self.creadora()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 59
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 57
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = SkylineParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 42
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 43
                        self.match(SkylineParser.MULT)
                        self.state = 44
                        self.expr(8)
                        pass

                    elif la_ == 2:
                        localctx = SkylineParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 45
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 46
                        self.match(SkylineParser.SUMA)
                        self.state = 47
                        self.expr(6)
                        pass

                    elif la_ == 3:
                        localctx = SkylineParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 48
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 49
                        self.match(SkylineParser.MULT)
                        self.state = 50
                        self.match(SkylineParser.NUM)
                        pass

                    elif la_ == 4:
                        localctx = SkylineParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 51
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 52
                        self.match(SkylineParser.SUMA)
                        self.state = 53
                        self.match(SkylineParser.NUM)
                        pass

                    elif la_ == 5:
                        localctx = SkylineParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 54
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 55
                        self.match(SkylineParser.RESTA)
                        self.state = 56
                        self.match(SkylineParser.NUM)
                        pass

             
                self.state = 61
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class CreadoraContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simple(self):
            return self.getTypedRuleContext(SkylineParser.SimpleContext,0)


        def composta(self):
            return self.getTypedRuleContext(SkylineParser.CompostaContext,0)


        def aleatoria(self):
            return self.getTypedRuleContext(SkylineParser.AleatoriaContext,0)


        def getRuleIndex(self):
            return SkylineParser.RULE_creadora

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCreadora" ):
                return visitor.visitCreadora(self)
            else:
                return visitor.visitChildren(self)




    def creadora(self):

        localctx = SkylineParser.CreadoraContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_creadora)
        try:
            self.state = 65
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SkylineParser.T__1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 62
                self.simple()
                pass
            elif token in [SkylineParser.T__4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 63
                self.composta()
                pass
            elif token in [SkylineParser.T__6]:
                self.enterOuterAlt(localctx, 3)
                self.state = 64
                self.aleatoria()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SimpleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self, i:int=None):
            if i is None:
                return self.getTokens(SkylineParser.NUM)
            else:
                return self.getToken(SkylineParser.NUM, i)

        def getRuleIndex(self):
            return SkylineParser.RULE_simple

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimple" ):
                return visitor.visitSimple(self)
            else:
                return visitor.visitChildren(self)




    def simple(self):

        localctx = SkylineParser.SimpleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_simple)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(SkylineParser.T__1)
            self.state = 68
            self.match(SkylineParser.NUM)
            self.state = 69
            self.match(SkylineParser.T__3)
            self.state = 70
            self.match(SkylineParser.NUM)
            self.state = 71
            self.match(SkylineParser.T__3)
            self.state = 72
            self.match(SkylineParser.NUM)
            self.state = 73
            self.match(SkylineParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CompostaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simple(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SkylineParser.SimpleContext)
            else:
                return self.getTypedRuleContext(SkylineParser.SimpleContext,i)


        def getRuleIndex(self):
            return SkylineParser.RULE_composta

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComposta" ):
                return visitor.visitComposta(self)
            else:
                return visitor.visitChildren(self)




    def composta(self):

        localctx = SkylineParser.CompostaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_composta)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(SkylineParser.T__4)
            self.state = 76
            self.simple()
            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SkylineParser.T__3:
                self.state = 77
                self.match(SkylineParser.T__3)
                self.state = 78
                self.simple()
                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 84
            self.match(SkylineParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AleatoriaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self, i:int=None):
            if i is None:
                return self.getTokens(SkylineParser.NUM)
            else:
                return self.getToken(SkylineParser.NUM, i)

        def getRuleIndex(self):
            return SkylineParser.RULE_aleatoria

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAleatoria" ):
                return visitor.visitAleatoria(self)
            else:
                return visitor.visitChildren(self)




    def aleatoria(self):

        localctx = SkylineParser.AleatoriaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_aleatoria)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(SkylineParser.T__6)
            self.state = 87
            self.match(SkylineParser.NUM)
            self.state = 88
            self.match(SkylineParser.T__3)
            self.state = 89
            self.match(SkylineParser.NUM)
            self.state = 90
            self.match(SkylineParser.T__3)
            self.state = 91
            self.match(SkylineParser.NUM)
            self.state = 92
            self.match(SkylineParser.T__3)
            self.state = 93
            self.match(SkylineParser.NUM)
            self.state = 94
            self.match(SkylineParser.T__3)
            self.state = 95
            self.match(SkylineParser.NUM)
            self.state = 96
            self.match(SkylineParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[3] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         





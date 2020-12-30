# Generated from Skyline.g by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\20")
        buf.write("]\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\5\2\23\n\2\3\3\3\3\3\3\3\3\3\3\3\3\5\3\33")
        buf.write("\n\3\3\4\3\4\3\4\3\4\3\4\7\4\"\n\4\f\4\16\4%\13\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4\64")
        buf.write("\n\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\5\6G\n\6\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\7\6X\n\6\f\6\16\6[")
        buf.write("\13\6\3\6\2\3\n\7\2\4\6\b\n\2\2\2d\2\22\3\2\2\2\4\32\3")
        buf.write("\2\2\2\6\63\3\2\2\2\b\65\3\2\2\2\nF\3\2\2\2\f\r\5\4\3")
        buf.write("\2\r\16\7\2\2\3\16\23\3\2\2\2\17\20\5\n\6\2\20\21\7\2")
        buf.write("\2\3\21\23\3\2\2\2\22\f\3\2\2\2\22\17\3\2\2\2\23\3\3\2")
        buf.write("\2\2\24\25\7\f\2\2\25\26\7\3\2\2\26\33\5\6\4\2\27\30\7")
        buf.write("\f\2\2\30\31\7\3\2\2\31\33\5\n\6\2\32\24\3\2\2\2\32\27")
        buf.write("\3\2\2\2\33\5\3\2\2\2\34\64\5\b\5\2\35\36\7\4\2\2\36#")
        buf.write("\5\b\5\2\37 \7\5\2\2 \"\5\b\5\2!\37\3\2\2\2\"%\3\2\2\2")
        buf.write("#!\3\2\2\2#$\3\2\2\2$&\3\2\2\2%#\3\2\2\2&\'\7\6\2\2\'")
        buf.write("\64\3\2\2\2()\7\7\2\2)*\7\13\2\2*+\7\5\2\2+,\7\13\2\2")
        buf.write(",-\7\5\2\2-.\7\13\2\2./\7\5\2\2/\60\7\13\2\2\60\61\7\5")
        buf.write("\2\2\61\62\7\13\2\2\62\64\7\b\2\2\63\34\3\2\2\2\63\35")
        buf.write("\3\2\2\2\63(\3\2\2\2\64\7\3\2\2\2\65\66\7\t\2\2\66\67")
        buf.write("\7\13\2\2\678\7\5\2\289\7\13\2\29:\7\5\2\2:;\7\13\2\2")
        buf.write(";<\7\n\2\2<\t\3\2\2\2=>\b\6\1\2>?\7\t\2\2?@\5\n\6\2@A")
        buf.write("\7\n\2\2AG\3\2\2\2BC\7\16\2\2CG\5\n\6\nDG\7\f\2\2EG\5")
        buf.write("\6\4\2F=\3\2\2\2FB\3\2\2\2FD\3\2\2\2FE\3\2\2\2GY\3\2\2")
        buf.write("\2HI\f\t\2\2IJ\7\r\2\2JX\5\n\6\nKL\f\5\2\2LM\7\17\2\2")
        buf.write("MX\5\n\6\6NO\f\b\2\2OP\7\r\2\2PX\7\13\2\2QR\f\7\2\2RS")
        buf.write("\7\17\2\2SX\7\13\2\2TU\f\6\2\2UV\7\16\2\2VX\7\13\2\2W")
        buf.write("H\3\2\2\2WK\3\2\2\2WN\3\2\2\2WQ\3\2\2\2WT\3\2\2\2X[\3")
        buf.write("\2\2\2YW\3\2\2\2YZ\3\2\2\2Z\13\3\2\2\2[Y\3\2\2\2\t\22")
        buf.write("\32#\63FWY")
        return buf.getvalue()


class SkylineParser ( Parser ):

    grammarFileName = "Skyline.g"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':='", "'['", "','", "']'", "'{'", "'}'", 
                     "'('", "')'", "<INVALID>", "<INVALID>", "'*'", "'-'", 
                     "'+'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "NUM", "ID", "MULT", "SUB", "ADD", "WS" ]

    RULE_root = 0
    RULE_assign = 1
    RULE_constructor = 2
    RULE_edifici = 3
    RULE_op = 4

    ruleNames =  [ "root", "assign", "constructor", "edifici", "op" ]

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
    ID=10
    MULT=11
    SUB=12
    ADD=13
    WS=14

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class RootContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign(self):
            return self.getTypedRuleContext(SkylineParser.AssignContext,0)


        def EOF(self):
            return self.getToken(SkylineParser.EOF, 0)

        def op(self):
            return self.getTypedRuleContext(SkylineParser.OpContext,0)


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
            self.state = 16
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 10
                self.assign()
                self.state = 11
                self.match(SkylineParser.EOF)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 13
                self.op(0)
                self.state = 14
                self.match(SkylineParser.EOF)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AssignContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SkylineParser.ID, 0)

        def constructor(self):
            return self.getTypedRuleContext(SkylineParser.ConstructorContext,0)


        def op(self):
            return self.getTypedRuleContext(SkylineParser.OpContext,0)


        def getRuleIndex(self):
            return SkylineParser.RULE_assign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)




    def assign(self):

        localctx = SkylineParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_assign)
        try:
            self.state = 24
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 18
                self.match(SkylineParser.ID)
                self.state = 19
                self.match(SkylineParser.T__0)
                self.state = 20
                self.constructor()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 21
                self.match(SkylineParser.ID)
                self.state = 22
                self.match(SkylineParser.T__0)
                self.state = 23
                self.op(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ConstructorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def edifici(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SkylineParser.EdificiContext)
            else:
                return self.getTypedRuleContext(SkylineParser.EdificiContext,i)


        def NUM(self, i:int=None):
            if i is None:
                return self.getTokens(SkylineParser.NUM)
            else:
                return self.getToken(SkylineParser.NUM, i)

        def getRuleIndex(self):
            return SkylineParser.RULE_constructor

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstructor" ):
                return visitor.visitConstructor(self)
            else:
                return visitor.visitChildren(self)




    def constructor(self):

        localctx = SkylineParser.ConstructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_constructor)
        self._la = 0 # Token type
        try:
            self.state = 49
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SkylineParser.T__6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 26
                self.edifici()
                pass
            elif token in [SkylineParser.T__1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 27
                self.match(SkylineParser.T__1)
                self.state = 28
                self.edifici()
                self.state = 33
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==SkylineParser.T__2:
                    self.state = 29
                    self.match(SkylineParser.T__2)
                    self.state = 30
                    self.edifici()
                    self.state = 35
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 36
                self.match(SkylineParser.T__3)
                pass
            elif token in [SkylineParser.T__4]:
                self.enterOuterAlt(localctx, 3)
                self.state = 38
                self.match(SkylineParser.T__4)
                self.state = 39
                self.match(SkylineParser.NUM)
                self.state = 40
                self.match(SkylineParser.T__2)
                self.state = 41
                self.match(SkylineParser.NUM)
                self.state = 42
                self.match(SkylineParser.T__2)
                self.state = 43
                self.match(SkylineParser.NUM)
                self.state = 44
                self.match(SkylineParser.T__2)
                self.state = 45
                self.match(SkylineParser.NUM)
                self.state = 46
                self.match(SkylineParser.T__2)
                self.state = 47
                self.match(SkylineParser.NUM)
                self.state = 48
                self.match(SkylineParser.T__5)
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

    class EdificiContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self, i:int=None):
            if i is None:
                return self.getTokens(SkylineParser.NUM)
            else:
                return self.getToken(SkylineParser.NUM, i)

        def getRuleIndex(self):
            return SkylineParser.RULE_edifici

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEdifici" ):
                return visitor.visitEdifici(self)
            else:
                return visitor.visitChildren(self)




    def edifici(self):

        localctx = SkylineParser.EdificiContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_edifici)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(SkylineParser.T__6)
            self.state = 52
            self.match(SkylineParser.NUM)
            self.state = 53
            self.match(SkylineParser.T__2)
            self.state = 54
            self.match(SkylineParser.NUM)
            self.state = 55
            self.match(SkylineParser.T__2)
            self.state = 56
            self.match(SkylineParser.NUM)
            self.state = 57
            self.match(SkylineParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class OpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def op(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SkylineParser.OpContext)
            else:
                return self.getTypedRuleContext(SkylineParser.OpContext,i)


        def SUB(self):
            return self.getToken(SkylineParser.SUB, 0)

        def ID(self):
            return self.getToken(SkylineParser.ID, 0)

        def constructor(self):
            return self.getTypedRuleContext(SkylineParser.ConstructorContext,0)


        def MULT(self):
            return self.getToken(SkylineParser.MULT, 0)

        def ADD(self):
            return self.getToken(SkylineParser.ADD, 0)

        def NUM(self):
            return self.getToken(SkylineParser.NUM, 0)

        def getRuleIndex(self):
            return SkylineParser.RULE_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp" ):
                return visitor.visitOp(self)
            else:
                return visitor.visitChildren(self)



    def op(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SkylineParser.OpContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_op, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 60
                self.match(SkylineParser.T__6)
                self.state = 61
                self.op(0)
                self.state = 62
                self.match(SkylineParser.T__7)
                pass

            elif la_ == 2:
                self.state = 64
                self.match(SkylineParser.SUB)
                self.state = 65
                self.op(8)
                pass

            elif la_ == 3:
                self.state = 66
                self.match(SkylineParser.ID)
                pass

            elif la_ == 4:
                self.state = 67
                self.constructor()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 87
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 85
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        localctx = SkylineParser.OpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_op)
                        self.state = 70
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 71
                        self.match(SkylineParser.MULT)
                        self.state = 72
                        self.op(8)
                        pass

                    elif la_ == 2:
                        localctx = SkylineParser.OpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_op)
                        self.state = 73
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 74
                        self.match(SkylineParser.ADD)
                        self.state = 75
                        self.op(4)
                        pass

                    elif la_ == 3:
                        localctx = SkylineParser.OpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_op)
                        self.state = 76
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 77
                        self.match(SkylineParser.MULT)
                        self.state = 78
                        self.match(SkylineParser.NUM)
                        pass

                    elif la_ == 4:
                        localctx = SkylineParser.OpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_op)
                        self.state = 79
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 80
                        self.match(SkylineParser.ADD)
                        self.state = 81
                        self.match(SkylineParser.NUM)
                        pass

                    elif la_ == 5:
                        localctx = SkylineParser.OpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_op)
                        self.state = 82
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 83
                        self.match(SkylineParser.SUB)
                        self.state = 84
                        self.match(SkylineParser.NUM)
                        pass

             
                self.state = 89
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[4] = self.op_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def op_sempred(self, localctx:OpContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 4)
         





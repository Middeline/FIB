# Generated from Skyline.g by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SkylineParser import SkylineParser
else:
    from SkylineParser import SkylineParser

# This class defines a complete generic visitor for a parse tree produced by SkylineParser.

class SkylineVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SkylineParser#root.
    def visitRoot(self, ctx:SkylineParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#ini.
    def visitIni(self, ctx:SkylineParser.IniContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#assig.
    def visitAssig(self, ctx:SkylineParser.AssigContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#expr.
    def visitExpr(self, ctx:SkylineParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#creadora.
    def visitCreadora(self, ctx:SkylineParser.CreadoraContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#simple.
    def visitSimple(self, ctx:SkylineParser.SimpleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#composta.
    def visitComposta(self, ctx:SkylineParser.CompostaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#aleatoria.
    def visitAleatoria(self, ctx:SkylineParser.AleatoriaContext):
        return self.visitChildren(ctx)



del SkylineParser
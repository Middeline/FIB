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


    # Visit a parse tree produced by SkylineParser#assign.
    def visitAssign(self, ctx:SkylineParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#constructor.
    def visitConstructor(self, ctx:SkylineParser.ConstructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#edifici.
    def visitEdifici(self, ctx:SkylineParser.EdificiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#op.
    def visitOp(self, ctx:SkylineParser.OpContext):
        return self.visitChildren(ctx)



del SkylineParser
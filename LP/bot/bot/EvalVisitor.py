import skyline as sky
import copy

if __name__ is not None and "." in __name__:
    from .SkylineParser import SkylineParser
    from .SkylineVisitor import SkylineVisitor
else:
    from cl.SkylineParser import SkylineParser
    from cl.SkylineVisitor import SkylineVisitor


class EvalVisitor(SkylineVisitor):

    def __init__(self, identificadors):
        self.nivell = 0
        self.IDs = identificadors

    def visitRoot(self, ctx: SkylineParser.RootContext):
        n = next(ctx.getChildren())
        S = self.visit(n)
        #print(self.visit(n))
        #print("root")
        #print("  " * self.nivell +
        #n.getText())
        return S, self.IDs

    def visitIni(self, ctx: SkylineParser.IniContext):
        #print("Ini")
        S = self.visit(ctx.getChild(0))
        return S

    def visitAssig(self, ctx: SkylineParser.AssigContext):
        #print("assig")
        id = ctx.IDENT().getText()
        #print(id)
        S = self.visit(ctx.getChild(2))
        self.IDs[id] = S
        return S

    def visitSimple(self, ctx: SkylineParser.SimpleContext):
        x = int(ctx.NUM(0).getText())
        a = int(ctx.NUM(1).getText())
        y = int(ctx.NUM(2).getText())
        #skyline.append((x, a, y))
        #print("simple")
        #print(x, a, y)
        tup = (x, a, y)
        return sky.Skyline([tup])

    def visitAleatoria(self, ctx: SkylineParser.AleatoriaContext):
        n = int(ctx.NUM(0).getText())
        h = int(ctx.NUM(1).getText())
        w = int(ctx.NUM(2).getText())
        xmin = int(ctx.NUM(3).getText())
        xmax = int(ctx.NUM(4).getText())
        #retornar
        #print("aleatoria")
        #print(n, h, w, xmin, xmax)
        S = sky.Skyline([])
        S.creacio_aleatoria(n, h, w, xmin, xmax)
        return S

    def visitComposta(self, ctx: SkylineParser.CompostaContext):
        #print("composta")
        S = sky.Skyline([])
        for i in ctx.getChildren():
            if i.getText() == '[' or i.getText() == ']' or i.getText() == ',':
                continue
            else:
                a = self.visit(i)
                S.afegeix_gratacel(a.skyline)
        return S

    def visitCreadora(self, ctx: SkylineParser.CreadoraContext):
        #print(ctx.getText())
        #print("creadora")
        s = self.visit(ctx.getChild(0))  #skyline
        return s

    def visitExpr(self, ctx: SkylineParser.ExprContext):
        n = ctx.getChildCount()
        S = sky.Skyline([])
        if n == 1:  #NUM, IDENT, o creadora
            if ctx.IDENT():
                id = ctx.IDENT().getText()
                return copy.deepcopy(self.IDs[id])
            else:
                S = self.visit(ctx.getChild(0))
                return S

        elif n == 2:  #RESTA expr
            #print(ctx.getChild(0).getText())
            S = self.visit(ctx.getChild(1))
            S.skyline_reflectit()
            return S

        else:
            S = self.visit(ctx.getChild(0))
            if ctx.MULT():
                #Multiplicacio
                if ctx.NUM():
                    #MULTIPLICAR PER N
                    n = int(ctx.NUM().getText())
                    S.mult_skyline(n)
                    #print("replicació:" + n)
                    return S
                else:
                    #INTERSECCIO
                    #print("INTERSECCIO")
                    S2 = self.visit(ctx.getChild(2))
                    #falta implementacio interseccio
                    S.interseccio(S2)
                    return S

            elif ctx.SUMA():
                #Suma
                if ctx.NUM():
                    #desplacament
                    n = int(ctx.NUM().getText())
                    #print("desplaçament dreta:" + n)
                    S.desplacar_D_skyline(n)
                    return S
                else:
                    #UNIO
                    #print("UNIO")
                    S2 = self.visit(ctx.getChild(2))
                    #print(S.skyline)
                    S.unio(S2)
                    #print(S.skyline)
                    #print(S2.skyline)
                    #implementar unio
                    return S

            elif ctx.RESTA():
                #RESTA, desplaçament a l'esquerra
                n = int(ctx.NUM().getText())
                S.desplacar_E_skyline(n)
                #print("desplaçament esquerra:" + n)
                return S

            else:
                #print("( expr )")
                S = self.visit(ctx.getChild(1))
                return S

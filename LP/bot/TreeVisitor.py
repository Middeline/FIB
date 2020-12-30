from cl.SkylineParser import SkylineParser
from cl.SkylineVisitor import SkylineVisitor
import skyline as sl
import copy


class TreeVisitor(SkylineVisitor):
    def __init__(self, skylines):
        self.skylines = skylines

    def visitRoot(self, ctx: SkylineParser.RootContext):
        n = next(ctx.getChildren())
        return self.visit(n), self.skylines

    # Fem la assignació al diccionari self.skylines i retornem el skyline
    def visitAssign(self, ctx: SkylineParser.AssignContext):
        id = ctx.getChild(0).getText()
        s = self.visit(ctx.getChild(2))
        self.skylines[id] = s
        return s

    def visitEdifici(self, ctx: SkylineParser.EdificiContext):  # Retorna un edifici simple (una tupla)
        x1 = int(ctx.NUM(0).getText())
        h = int(ctx.NUM(1).getText())
        x2 = int(ctx.NUM(2).getText())
        if x2 > x1 and h >= 0:  # Controlem que xmax sigui més gran que xmin i que no es donin edificis amb alçades negatives
            return (x1, h, x2)
        else:
            return (0, 0, 0)  # Retornem un edifici buit, que després eliminarem a la classe skyline

    def visitConstructor(self, ctx: SkylineParser.ConstructorContext):  # Visitem 3 tipus diferents de constructores
        fChild = ctx.getChild(0)

        if ctx.getChildCount() == 1:  # Només construim un edifici (xmin, alçada, xmax)
            edifici = [self.visit(fChild)]
            s = sl.skyline(edifici)
            return s

        elif fChild.getText() == '[':  # Segona constructora [edifici (, edifici)*]
            edificis = []
            for c in ctx.getChildren():
                if c.getText() == '[' or c.getText() == ',' or c.getText() == ']':
                    continue
                else:
                    edificis.append(self.visit(c))
            return sl.skyline(edificis)

        elif fChild.getText() == '{':  # Tercera constructora {n, h, w, xmin, xmax}
            n = int(ctx.NUM(0).getText())
            h = int(ctx.NUM(1).getText())
            w = int(ctx.NUM(2).getText())
            xmin = int(ctx.NUM(3).getText())
            xmax = int(ctx.NUM(4).getText())
            s = sl.skyline([])  # Hem de crear un skyline buit per a poder usar randEdificis(). D'aquesta forma no hem de crear un mòdul només per una funció
            edificis = s.randEdificis(n, h, w, xmin, xmax)
            return sl.skyline(edificis)

    def visitOp(self, ctx: SkylineParser.OpContext):
        nChilds = ctx.getChildCount()

        if nChilds == 3 and ctx.getChild(0).getText() == '(' and ctx.getChild(2).getText() == ')':  # (op)
            return self.visit(ctx.getChild(1))

        if ctx.SUB():
            if nChilds == 2:  # Operació mirall
                op = ctx.getChild(1)
                s = self.visit(op)
                s.reflectir()
                return s

            elif ctx.NUM():  # Operació desplaçament negatiu
                op = ctx.getChild(0)
                s = self.visit(op)
                N = int(ctx.NUM().getText())
                s.desplacament(-N)
                return s

        if ctx.MULT():
            if ctx.NUM():  # op MULT NUM
                op = ctx.getChild(0)
                s = self.visit(op)
                N = int(ctx.NUM().getText())
                s.replicacio(N)
                return s

            else:  # op MULT op (interescció)
                s1 = self.visit(ctx.getChild(0))
                s2 = self.visit(ctx.getChild(2))
                s1.interseccio(s2)
                return s1

        if ctx.ADD():
            if ctx.NUM():  # Operació desplaçament
                op = ctx.getChild(0)
                s = self.visit(op)
                N = int(ctx.NUM().getText())
                s.desplacament(N)
                return s

            else:  # op ADD op Operació unió
                s1 = self.visit(ctx.getChild(0))
                s2 = self.visit(ctx.getChild(2))
                s1.unio(s2)
                return s1

        if ctx.ID():  # Atómic, la id
            try:
                id = ctx.getChild(0).getText()
                return copy.deepcopy(self.skylines[id])
            except:  # Si la id no és correcte, retornem un skyline buit
                return sl.skyline([])

        if nChilds == 1 and ctx.constructor():  # Operació constructora
            return self.visit(ctx.getChild(0))

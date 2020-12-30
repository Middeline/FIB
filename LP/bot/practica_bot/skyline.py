import matplotlib.pyplot as mpl
import random

class Skyline:

    def __init__(self, skyline):
        self.skyline = skyline
        self.alcada = self.calcula_alcada()
        self.area = self.calcula_area()

#Calcul alçada
    def calcula_alcada(self):
        alcada = 0
        for edifici in self.skyline:
            alcada = max(alcada, edifici[1])
        return alcada

#Calcul area
    def calcula_area(self):
        area = 0
        for gratacel in self.skyline:
            area += (gratacel[2] - gratacel[0]) * gratacel[1]
        return area


#afegir gratacel/edifici
    def afegeix_gratacel(self, gratacels):
        self.skyline.extend(gratacels)  #llista de tumplas de gratacels
        self.skyline.sort(key=lambda tup: tup[0])
        self.alcada = self.calcula_alcada()
        self.area = self.calcula_area()



#desplaçament a la dreta de l'skyline N posicions.
    def desplacar_D_skyline(self, desplacament):
        nou_sky = []
        for edifici in self.skyline:
            nou_sky.append((edifici[0] + desplacament, edifici[1], edifici[2] + desplacament))
        self.skyline = nou_sky


#desplaçament a l'esquerra de l'skyline N posicions.
    def desplacar_E_skyline(self, desplacament):
        nou_sky = []
        for edifici in self.skyline:
            nou_sky.append((edifici[0] - desplacament, edifici[1], edifici[2] - desplacament))
        self.skyline = nou_sky


#replicació N vegades de l'skyline (vegeu exemple d'interacció).
    def mult_skyline(self, n):
        maxx = max(self.skyline, key=lambda tup: tup[2])[2]
        minn = min(self.skyline, key=lambda tup: tup[0])[0]
        size = maxx-minn
        aux = []
        for i in range(n-1):
            for edifici in self.skyline:
                nou_edifici = (edifici[0]+size, edifici[1], edifici[2]+size)
                aux.append(nou_edifici)
            size = size + maxx-minn;
        self.skyline.extend(aux)
        self.alcada = self.calcula_alcada()
        self.area = self.calcula_area()



# retorna l'skyline reflectit.
    def skyline_reflectit(self):
        maxx = max(self.skyline,key=lambda tup:tup[2])[2]
        min = self.skyline[0][0]
        skyline2 = []
        for edifici in self.skyline:
            x = edifici[0]
            a = edifici[1]
            x2 = edifici[2]
            skyline2.append((maxx-(x2-min), a, maxx-(x-min)))
        self.skyline = skyline2
        self.skyline.sort(key=lambda tup: tup[0])


#n = num edificis, altura= 0-h, amplada = 1-n, x = xmin -xmax
    def creacio_aleatoria(self, n, h, w, xmin, xmax):
        if h > 0 and xmax > xmin:
            for i in range(n):
                al = random.randint(0, h)
                am = random.randint(1, min(w, xmax-xmin))
                x = random.randint(xmin, xmax-am)
                self.skyline.append((x, al, x+am))
            self.alcada = self.calcula_alcada()
            self.area = self.calcula_area()


    def interseccio(self, Skyline):
        self.skyline.extend(Skyline.skyline)
        self.skyline.sort(key=lambda tup: tup[0])
        self.alcada = self.calcula_alcada()
        self.area = self.calcula_area()


    def unio(self, Skyline):
        self.skyline.extend(Skyline.skyline)
        self.skyline.sort(key=lambda tup: tup[0])
        self.alcada = self.calcula_alcada()
        self.area = self.calcula_area()


    def matplot(self, sky):
        #matplotlib.pyplot.bar(x, height, width=0.8, bottom=None, \*, align='center', data=None, \*\*kwargs)
        mpl.clf()
        for edifici in sky:
            mpl.bar(edifici[0], edifici[1], (edifici[2]-edifici[0]), align='edge', color='purple')

        fileName = "tmp.foto.png"
        mpl.savefig(fileName)
        return fileName
        #mpl.show()


        def treure_solapaments (self):
            a = self.punts_unio(self.skyline)
            #convertir puntos en edificios
            sky = []
            for i in a:
                if i[1] != 0:
                    sky.append(i[0], i[1], i+1[0])



        def punts_unio (self, sky):
                 if sky == []:
                     return []
                 if len(sky) == 1:
                     return [(sky[0][0], sky[0][2]), (sky[0][1], 0)]
                 #punt mig
                 mig = len(sky) // 2
                 esq = self.punts_unio(sky[:mig])
                 dreta = self.punts_unio(sky[mig:])
                 return self.merge(esq, dret)

        def merge(self, esq, dret):
                 alt1, alt2 = 0, 0
                 i, j = 0, 0
                 punts_result = []

                 while i < len(esq) and j < len(dret):
                     #cas E < D
                     if esq[i][0] < dret[j][0]:
                         alt1 = esq[i][1]
                         punt = esq[i][0]
                         i += 1
                     #cas D < E
                     elif dret[j][0] < esq[i][0]:
                         alt2 = dret[j][1]
                         punt = dret[j][0]
                         j += 1
                     #sino D<E o E<D, E==D
                     else:
                         alt1 = esq[i][1]
                         alt2 = dret[j][1]
                         punt = dret[j][0]
                         i += 1
                         j += 1
                    #comprova que el maxim no es el mateix o que la llista es buida
                     if punts_result == [] or punts_result[-1][1] != max(h1, h2):
                         punts_result.append(corner, max(h1, h2))

                 punts_result.extend(dret[j:])
                 punts_result.extend(esq[i:])
                 return punts_result


L = []

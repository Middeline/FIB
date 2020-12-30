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
        #self.skyline = s
        #print("area")
        s = self.overlaping(self.skyline)
        self.skyline = self.conversio_punts_edificis(s)

        #print(self.skyline)
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
            size = size + maxx-minn
        self.skyline.extend(aux)
        self.area = self.calcula_area()
        self.alcada = self.calcula_alcada()


# retorna l'skyline reflectit.
    def skyline_reflectit(self):
        maxx = max(self.skyline, key=lambda tup: tup[2])[2]
        min = self.skyline[0][0]
        skyline2 = []
        for edifici in self.skyline:
            x = edifici[0]
            a = edifici[1]
            x2 = edifici[2]
            skyline2.append((maxx-(x2-min), a, maxx-(x-min)))
        self.skyline = skyline2
        self.skyline.sort(key=lambda tup: tup[0])
        self.calcula_area()
        self.calcula_alcada()


#n = num edificis, altura= 0-h, amplada = 1-n, x = xmin -xmax
    def creacio_aleatoria(self, n, h, w, xmin, xmax):
        if h > 0 and xmax > xmin:
            for i in range(n):
                al = random.randint(0, h)
                am = random.randint(1, min(w, xmax-xmin))
                x = random.randint(xmin, xmax-am)
                self.skyline.append((x, al, x+am))
            self.area = self.calcula_area()
            self.alcada = self.calcula_alcada()


# intersecció
    def interseccio(self, Skyline):
        self.skyline.extend(Skyline.skyline)
        self.skyline.sort(key=lambda tup: tup[0])
        a = self.skyline
        s = self.punts_inter(self.skyline)
        b = self.conversio_punts_edificis(s)
        if b == []:
            self.skyline = [(0, 0, 0)]
        elif b[0] != a[1]:
            self.skyline = b
        else:
            self.skyline = [(0, 0, 0)]

        self.area = self.calcula_area()
        self.alcada = self.calcula_alcada()


#unio
    def unio(self, Skyline):
        self.skyline.extend(Skyline.skyline)
        self.skyline.sort(key=lambda tup: tup[0])

        self.area = self.calcula_area()
        self.alcada = self.calcula_alcada()


#per a imprimir grafic de barres (representacio skyline)
    def matplot(self, sky):
        #matplotlib.pyplot.bar(x, height, width=0.8, bottom=None, \*, align='center', data=None, \*\*kwargs)
        mpl.clf()
        for edifici in sky:
            mpl.bar(edifici[0], edifici[1], (edifici[2]-edifici[0]), align='edge', color='purple')
        fileName = "tmp.foto.png"
        mpl.savefig(fileName)
        return fileName
        #mpl.show()


#funció passa punts a edificis
    def conversio_punts_edificis(self, punts):
        sky = []
        #print("puntos")
        #print(punts)
        for i in range(len(punts)-1):
            if punts[i][1] != 0:
                sky.append((punts[i][0], punts[i][1], punts[i+1][0]))
        return sky


#treu overlaping entre edificis
    def overlaping(self, sky):   # O(nlogn) amb merge
        #entra ordenada
        #cas base 1 esta buida
        if sky == []:
            return []
        #cas base 2 nomes hi ha un edifici
        if len(sky) == 1:
            return [(sky[0][0], sky[0][1]), (sky[0][2], 0)]
        #punt mig
        mig = int(len(sky)/2)
        #meitat esquerra
        esq = self.overlaping(sky[:mig])
        #print(esq)
        #meitat dreta
        dret = self.overlaping(sky[mig:])
        #print(dret)
        result = self.merge_unio(esq, dret)
        #print(result)
        #print("lool")
        return result


#merge unio
    def merge_unio(self, esq, dret):  #DIVIDE AND CONQUER  O(nlogn)
        #ja entren ordenades pk sempre que faig funcio ordeno
        #alçades
        alt1 = 0
        alt2 = 0
        i = 0
        j = 0
        punts_result = []

        while i < len(esq) and j < len(dret):
            #cas el primer edifici de l'esquerra comença abans que el primer de la llista de la dreta
            if esq[i][0] < dret[j][0]:
                alt1 = esq[i][1]  # alçada edifici esquerra ja que es mes alt
                x = esq[i][0]
                i += 1
            #cas D < E igual que abans però del revés
            elif dret[j][0] < esq[i][0]:
                alt2 = dret[j][1]  # alçada edifici dreta mes ALT
                x = dret[j][0]
                j += 1
            #quan els dos edificis comencen a la vegada
            else:
                alt1 = esq[i][1]  #alçada edifici 1 (esquerra)
                alt2 = dret[j][1]  # alçada edifici 2 (dreta)
                x = dret[j][0]
                i += 1
                j += 1
            #comprova que el maxim no es el mateix o que la llista es buida
            if punts_result == [] or punts_result[-1][1] != max(alt1, alt2):
                punts_result.append((x, max(alt1, alt2)))
                #print(punts.result)
        #sense els primers j elements
        punts_result.extend(dret[j:])
        #print(punts.result)
        #sense els primers i elements
        punts_result.extend(esq[i:])
        #print(punts.result)
        return punts_result


#crida al merge interseccio
    def punts_inter(self, sky):   # O(nlogn) amb merge
        #entra ordenada
        #cas base 1 esta buida
        if sky == []:
            return []
        #cas base 2 nomes hi ha un edifici
        if len(sky) == 1:
            return [(sky[0][0], sky[0][1]), (sky[0][2], 0)]
        #punt mig
        mig = int(len(sky)/2)
        #meitat esquerra
        esq = self.punts_inter(sky[:mig])
        #print(esq)
        #meitat dreta
        dret = self.punts_inter(sky[mig:])
        #print(dret)
        result = self.merge_inter(esq, dret)
        #print(result)
        #print("lool")
        return result


#merge interseccio
    def merge_inter(self, esq, dret):  #DIVIDE AND CONQUER  O(nlogn)
    #nomes comprova la interseccio si entre ells es solapen
    #en un altre cas comprovat a la funcion interseccio
        #ja entren ordenades pk sempre que faig funcio ordeno
        #alçades
        alt1 = 0
        alt2 = 0
        i = 0
        j = 0
        punts_result = []

        while i < len(esq) and j < len(dret):
            #cas el primer edifici de l'esquerra comença abans que el primer de la llista de la dreta
            if esq[i][0] < dret[j][0]:
                alt1 = esq[i][1]  # alçada edifici esquerra ja que es mes alt
                x = esq[i][0]
                i += 1
            #cas D < E igual que abans però del revés
            elif dret[j][0] < esq[i][0]:
                alt2 = dret[j][1]  # alçada edifici dreta mes ALT
                x = dret[j][0]
                j += 1
            #quan els dos edificis comencen a la vegada
            else:
                alt1 = esq[i][1]  #alçada edifici 1 (esquerra)
                alt2 = dret[j][1]  # alçada edifici 2 (dreta)
                x = dret[j][0]
                i += 1
                j += 1
            #comprova que el maxim no es el mateix o que la llista es buida
            if punts_result == [] or punts_result[-1][1] != min(alt1, alt2):
                punts_result.append((x, min(alt1, alt2)))
                #print(punts.result)
        #sense els primers j elements
        punts_result.extend(dret[j:])
        #print(punts.result)
        #sense els primers i elements
        punts_result.extend(esq[i:])
        #print(punts.result)
        return punts_result


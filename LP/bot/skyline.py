import random as rd
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from heapq import heappush, heappop


class skyline():
    # Crea un skyline amb els edificis, on edificis es una llista de tuples
    # Invariants:
    #   · Els edificis han d'estar simplificats, és a dir, sense solapaments i sense edificis buits
    #   · self.area, self.altura, self.minX i self.maxX han de estar actualitzats
    def __init__(self, edificis):
        self.edificis = edificis
        self.simplify()
        self.calculateArea()
        self.calculateMinMaxAlt()

    # Getters:
    def getEdificis(self):
        return self.edificis

    def getArea(self):
        return self.area

    def getAltura(self):
        return self.altura

    def getImage(self):  # Retorna el nom del ficher amb el que s'ha guardat la figura del skyline o -1 si el skyline és buit
        try:
            if len(self.edificis) != 0:
                fig = plt.figure()
                ax = fig.add_subplot(111)
                for ed in self.edificis:
                    ax.bar(ed[0], ed[1], (ed[2]-ed[0]), align='edge', color='#4570a9')

                ax.xaxis.set_major_locator(MaxNLocator(integer=True))
                ax.yaxis.set_major_locator(MaxNLocator(integer=True))

                fileName = "tmp.%d.png" % rd.randint(1000000, 9999999)  # El nom del fitxer es crea aleatòriament (es podria fer millor, però així ja farà el fet)
                plt.savefig(fileName)

                plt.cla()  # Tanquem el axis
                plt.clf()  # Tanquem la figura a matplotlib
                plt.close()  # Per si acas, també tanquem la finestra

                return fileName
            else:  # If trying to print an empty skyline return -1 as a control result
                return -1
        except Exception as e:
            return e

    # Operacions útils:
    # Retorna n edificis, cadascun d’ells amb una alçada aleatòria entre 0 i h, amb una amplada
    # aleatòria entre 1 i w, i una posició d’inici i de final aleatòria entre xmin i xmax
    def randEdificis(self, n, h, w, xmin, xmax):  # Cost: O(n log n)
        edificis = []
        if h > 0 and xmax - xmin > 0:
            for _ in range(n):
                ampl = rd.randint(1, min(w, xmax-xmin))
                h1 = rd.randint(0, h)
                x1 = rd.randint(xmin, xmax-ampl)
                x2 = x1+ampl
                edificis.append((x1, h1, x2))
            edificis.sort(key=lambda tup: tup[0])
        return edificis  # Retorna [] si no es compleixen els prerequisits

    # Retorna els skylines en format de punts
    def toPoints(self):  # Cost: O(n log n)
        initialPoints = list(map(lambda ed: (ed[0], ed[1], "s"), self.edificis))  # obtenim els punts inicials de cada edifici. O(n)
        initialPoints.extend(list(map(lambda ed: (ed[2], ed[1], "e"), self.edificis)))  # afegim els punts finals de cada edifici. O(n)

        initialPoints.sort(key=lambda tup: tup[0])  # endreçem els punts per ordre de x. O(n log n)

        finalPoints = []
        maxPQ = [0]  # on guardem les alçades
        altDescartades = []  # lazy approach per a descartar items de la maxPQ
        maxAltura = 0
        for p in initialPoints:  # O(p)
            if p[2] == "s":  # Començament d'un edifici
                # Fiquem la altura de l'edifici al heap, negada ja que a python és un minHeap
                heappush(maxPQ, -p[1])
                if p[1] > maxAltura:  # Si l'edifici és el més alt afegim el punt
                    finalPoints.append((p[0], p[1]))
                    maxAltura = p[1]

            else:  # Final d'un edifici
                if maxPQ[0] == -p[1]:  # Si és l'edici més alt
                    heappop(maxPQ)
                    while (-maxPQ[0]) in altDescartades:  # Si el nou màxim l'hem descartat prèviament
                        altDescartades.remove(-maxPQ[0])
                        heappop(maxPQ)
                    if maxAltura > -maxPQ[0]:  # Si canvia l'altura màxima
                        maxAltura = -maxPQ[0]
                        finalPoints.append((p[0], maxAltura))
                else:  # si no és l'edifici més alt l'afegim a les alçades per descartar
                    altDescartades.append(p[1])

        return finalPoints

    # Retorna els punts en format d'edificis
    def pointsToBuildings(self, points):  # Cost: O(p)
        edificis = []
        h = 0
        xmin = 0
        for p in points:
            if h != 0:
                edificis.append((xmin, h, p[0]))

            xmin = p[0]
            h = p[1]

        return edificis

    # Endreça els skylines per xmin, elimina edificis buits i elimina solapaments de edificis
    def simplify(self):  # Cost: O(n log n)
        self.edificis.sort(key=lambda tup: tup[0])  # Endreçem per xmin
        while len(self.edificis) > 0 and self.edificis[0] == (0, 0, 0):  # Eliminem edificis buits
            self.edificis.pop(0)
        # Eliminem solapaments d'edificis:
        points = self.toPoints()
        self.edificis = self.pointsToBuildings(points)

    # Càlculs de variables privades:
    def calculateArea(self):
        area = 0
        for edifici in self.edificis:
            area += (edifici[2] - edifici[0]) * edifici[1]
        self.area = area

    def calculateMinMaxAlt(self):
        try:  # Dóna errors amb skylines buits
            self.minX = min(self.edificis, key=lambda el: el[0])[0]
            self.altura = max(self.edificis, key=lambda el: el[1])[1]
            self.maxX = max(self.edificis, key=lambda el: el[2])[2]
        except:
            self.minX = 0
            self.altura = 0
            self.maxX = 0

    # Operacions amb skylines:
    def addEdificis(self, edificis):
        self.edificis += edificis
        self.simplify()  # treiem solapaments
        self.calculateArea()
        self.calculateMinMaxAlt()

    def unio(self, skyline2):  # self = unió de self amb skyline2
        self.addEdificis(skyline2.getEdificis())

    def interseccio(self, skyline2):  # self = intersecció de self amb skyline2. Cost = O(len(s1)+len(s2))
        interseccio = []
        j = i = 0
        edificisj = skyline2.getEdificis()
        while i < len(self.edificis) and j < len(edificisj):
            edi = self.edificis[i]
            edj = edificisj[j]
            while i < len(self.edificis) and edi[2] < edj[0]:
                i += 1
                edi = self.edificis[i]
            while j < len(edificisj) and edj[2] < edi[0]:
                j += 1
                edj = edificisj[j]
            if i == len(self.edificis) or j == len(edificisj):
                break
            # En aquest punt, edi[0] <= edj[0] <= edi[2] o edj[0] <= edi[0] <= edj[2]
            if edi[0] <= edj[0] and edj[0] <= edi[2]:
                interseccio.append((edj[0], min(edi[1], edj[1]), min(edi[2], edj[2])))

            if edj[0] <= edi[0] and edi[0] <= edj[2]:
                interseccio.append((edi[0], min(edi[1], edj[1]), min(edi[2], edj[2])))

            if i+1 < len(self.edificis) and self.edificis[i+1][0] < edj[2]:
                j -= 1
            elif j+1 < len(edificisj) and edificisj[j+1][0] < edi[2]:
                i -= 1
            i += 1
            j += 1

        self.edificis = interseccio

    def replicacio(self, N):  # repliquem el skyline N vegades
        newEdificis = self.edificis
        addFactor = self.maxX - self.minX
        for _ in range(N-1):
            newEdificis = list(map(lambda x: (x[0] + addFactor, x[1], x[2] + addFactor), newEdificis))
            self.edificis += newEdificis
        self.calculateArea()
        self.calculateMinMaxAlt()

    def desplacament(self, N):  # desplaçem N posicions a la dreta o a l'esquerra. Els edificis poden tenir x negativa
        self.edificis = list(map(lambda ed: (ed[0] + N, ed[1], ed[2] + N), self.edificis))

    def reflectir(self):  # Operació mirall
        min = self.minX
        max = self.maxX
        self.edificis = list(map(lambda ed: (max-(ed[2]-min), ed[1], max-(ed[0]-min)), self.edificis))
        self.edificis.sort(key=lambda tup: tup[0])

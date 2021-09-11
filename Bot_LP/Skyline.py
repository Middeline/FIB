import matplotlib.pyplot as mpl

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
                size += maxx-minn;
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


    def creacio_aleatoria(self, n, h, w, xmin, xmax):
        for i in n:
            al = random.randint(0, h)
            am = random.randint(1, w)
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


    def matplot(self):
        alturas = []
        Xs = []
        #matplotlib.pyplot.bar(x, height, width=0.8, bottom=None, \*, align='center', data=None, \*\*kwargs)
        for edifici in self.skyline:
            alturas.append(edifici[1])
            Xs.append(edifici[0])

        x_pos = [i for i, _ in enumerate(Xs)]

        mpl.bar(x_pos, alturas, color='purple')
        mpl.show()


    def get_skyline(self, buildings):
             """
             :type buildings: List[List[int]]
             :rtype: List[List[int]]
             """
             if not buildings:
                 return []
             if len(buildings) == 1:
                 return [[buildings[0][0], buildings[0][2]], [buildings[0][1], 0]]

             mid = len(buildings) // 2
             left = self.get_skyline(buildings[:mid])
             right = self.get_skyline(buildings[mid:])
             return self.merge(left, right)

    def merge(self, left, right):
             h1, h2 = 0, 0
             i, j = 0, 0
             result = []

             while i < len(left) and j < len(right):
                 if left[i][0] < right[j][0]:
                     h1 = left[i][1]
                     corner = left[i][0]
                     i += 1
                 elif right[j][0] < left[i][0]:
                     h2 = right[j][1]
                     corner = right[j][0]
                     j += 1
                 else:
                     h1 = left[i][1]
                     h2 = right[j][1]
                     corner = right[j][0]
                     i += 1
                     j += 1
                 if self.is_valid(result, max(h1, h2)):
                     result.append([corner, max(h1, h2)])
             result.extend(right[j:])
             result.extend(left[i:])
             return result

    def is_valid(self, result, new_height):
             return not result or result[-1][1] != new_height

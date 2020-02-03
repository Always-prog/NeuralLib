import numpy as np


class Network5():
    def __init__(self,kol):
        self.kol = kol
        #слои нейронов
        self.N1 = np.full((self.kol[0],2),0.0)
        self.N2 = np.full((self.kol[1],2),0.0)
        self.N3 = np.full((self.kol[2],2),0.0)
        self.N4 = np.full((self.kol[3],2),0.0)
        self.N5 = np.full((self.kol[4],2),0.0)
        #случайные веса
        self.W1 = np.random.rand(len(self.N1),len(self.N2)) - 0.5
        self.W2 = np.random.rand(len(self.N2),len(self.N3)) - 0.5
        self.W3 = np.random.rand(len(self.N3),len(self.N4)) - 0.5
        self.W4 = np.random.rand(len(self.N4),len(self.N5)) - 0.5

    def trening(self,inputs,VD,k):
        self.N1 = inputs
        self.VD = VD
        self.k = k
        #прогоняем по всем слоям сигналы
        self.N2 = progon(self.N1,self.N2,self.W1)
        self.N3 = progon(self.N2,self.N3,self.W2)
        self.N4 = progon(self.N3,self.N4,self.W3)
        self.N5 = progon(self.N4,self.N5,self.W4)
        #находим ошибку выходного слоя
        self.N5 = OutFindError(self.VD,self.N5)
        #находим ошибки
        self.N4 = FindError(self.N4,self.N5,self.W4)
        self.N3 = FindError(self.N3,self.N4,self.W3)
        self.N2 = FindError(self.N2,self.N3,self.W2)
        self.N1 = FindError(self.N1,self.N2,self.W1)
        #сохраняем найденную ошибку
        self.W1 = SaveError(self.N1,self.N2,self.W1,self.k)
        self.W2 = SaveError(self.N2,self.N3,self.W2,self.k)
        self.W3 = SaveError(self.N3,self.N4,self.W3,self.k)
        self.W4 = SaveError(self.N4,self.N5,self.W4,self.k)
    def status(self,stat_num):
        self.stat_num = stat_num
        if self.stat_num == 1:
            return self.N1
        elif self.stat_num == 2:
            return self.N2
        elif self.stat_num == 3:
            return self.N3
        elif self.stat_num == 4:
            return self.N4
        elif self.stat_num == 5:
            return self.N5
        else:
            return "this is not definet"
    def think(self,inputs):
        self.inputs = inputs
        self.N1 = self.inputs
        self.N2 = progon(self.N1,self.N2,self.W1)
        self.N3 = progon(self.N2,self.N3,self.W2)
        self.N4 = progon(self.N3,self.N4,self.W3)
        self.N5 = progon(self.N4,self.N5,self.W4)
        return self.N5




def act(x):
    return 1/(1 + np.exp(-x))

def progon(Li,Lo,W):
    VI = len(Li)
    VO = len(Lo)
    x = 0
    while x < VO:
        y = 0
        Lo[x][0] = 0
        while y < VI:
            Lo[x][0] += Li[y][0] * W[y][x]
            y += 1
        Lo[x][0] = act(Lo[x][0])
        x += 1
    return Lo

def OutFindError(IDL,N):
    V = len(IDL)
    x = 0
    while x < V:
        N[x][1] = IDL[x][0] - N[x][0] 
        x += 1
    return N

def FindError(Li,Lo,W):
    VO = len(Lo)
    VI = len(Li)
    x = 0
    while x < VI:
        Li[x][1] = 0
        y = 0
        while y < VO:
            Li[x][1] = Li[x][1] + W[x][y] * Lo[y][1]
            y += 1
        x += 1
    return Li

        

def SaveError(Li,Lo,W,k):
    VI = len(Li)
    VO = len(Lo)
    x = 0
    while x < VO:
        y = 0
        while y < VI:
            W[y][x] += Lo[x][1] * (Lo[x][0]* (1-Lo[x][0])) *(Li[y][0] * k)
            y += 1
        x += 1
    return W

    

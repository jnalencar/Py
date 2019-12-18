class processo:
    def __init__(self, tempo, tipo, estado = '    novo   '):
        self.tempo = tempo
        self.tipo = tipo
        if estado:
            self.estado = estado
        else:
            self.estado = '    novo   '

    def __str__(self):
        return str(self.tempo)+' '+str(self.tipo)

def ComparaPrimeiros(M, k, v):
    j = 3000
    i = 0
    for proc in M:
        i = i + 1
        if proc == []:
            continue
        elif j > proc[0].tempo:
            j = proc[0].tempo
            k = i
    k = k - 1
    j = 0
    if v[k] != ' Concluido ':
        v[k] = 'Em Execucao'
    printV(v)
    return k


def ChecaFim(M):
    v = []
    for i in range(len(M)):
        v.append([])
    return v

def CriaVetorResultado(M):
    v = []
    for i in range(len(M)):
        v.append('    novo   ')
    return v

def printInicio(v):
    for i in range(len(v)):
        print('--------------', end='')
    print()

def printV(v):
    for i in range(len(v)):
        print(' '+v[i]+' ', end='|')
    print()

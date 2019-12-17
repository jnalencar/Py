class processo:
    def __init__(self, tempo, tipo, estado = 'novo'):
        self.tempo = tempo
        self.tipo = tipo
        if estado:
            self.estado = estado
        else:
            self.estado = 'novo'

    def __str__(self):
        return str(self.tempo)+' '+str(self.tipo)

def ComparaPrimeiros(M, k):
    j = 3000
    for i in range(len(M)):
        if j > M[i][0].tempo:
            j = M[i][0].tempo
            k = i
    return k


M = []
tempo = 0
with open('escal.txt', "r") as ins:
    for line in ins:
        M.append([])
        v = []
        inner_list = [elt.strip() for elt in line.split(' ')]
        for i in range(0, len(inner_list), 2):
            v.append(processo(int(inner_list[i]), inner_list[i+1]))
        M[len(M)-1] = v
v = []
for i in range(len(M)):
    v.append('novo')
while M != []:
    k = 0
##    for vec in M:
##        for pross in vec:
##            print (pross, end=' ')
##        print()
##    print()
    line = ComparaPrimeiros(M, k)       
    popz = M[line].pop(0).tempo
    if v[line] != 'concluido':
        v[line] = 'Em espera'
    if M[line] == []:
        M.pop(line)
        v[line] = 'concluido'
    print (v)
    
    tempo = tempo + popz        
print ('Total de unidades de tempo gastas:',tempo)

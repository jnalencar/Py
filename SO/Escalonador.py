from Escalonadorlib import *

def UltimaVolta():
    global tempo
    global v
    global M
    global popz
    k = 0
##    for vec in M:
##        for pross in vec:
##            print (pross, end=' ')
##        print()
##    print()
##    print ('------------------------------------------------')
    line = ComparaPrimeiros(M, k, v)
    if len(M[line]) == 1:
        v[line] = ' Concluido '
    if v[line] != ' Concluido ':
        v[line] = ' Em espera '
    if M[line] != []:
        popz = M[line].pop(0).tempo
    tempo = tempo + popz
    print ('Total de unidades de tempo gastas (ao todo):',tempo)

M = []
tempo = 0
print ('O arquivo deve estar no mesmo diretório do programa.')
nomearquivo = input('Insira o nome do arquivo: ')
with open(nomearquivo, "r") as ins:
    for line in ins:
        M.append([])
        v = []
        inner_list = [elt.strip() for elt in line.split(' ')]
        for i in range(0, len(inner_list), 2):
            v.append(processo(int(inner_list[i]), inner_list[i+1]))
        M[len(M)-1] = v

Final = ChecaFim(M)
v = CriaVetorResultado(M)
printInicio(v)
printV (v)
while M != []:
##    print (v)
    i = 0
    k = 0
##    for vec in M:
##        for pross in vec:
##            print (pross, end=' ')
##        print()
##    print()
##    print ('------------------------------------------------')
    line = ComparaPrimeiros(M, k, v)
    if len(M[line]) == 1:
        v[line] = ' Concluido '
    if v[line] != ' Concluido ':
        v[line] = ' Em espera '
    if M[line] != []:
        popz = M[line].pop(0).tempo
    if M == Final:
        break
    tempo = tempo + popz
    printV(v)
##    print ('Total de unidades de tempo gastas (até o momento):',tempo)
UltimaVolta()

import os, os.path

path, dirs, files = next(os.walk('TSE'))

for d in dirs:
    caminho = os.path.join(path, d)
    tam = 0
    for arq in os.listdir(caminho):

        tam = tam + os.path.getsize(os.path.join(caminho, arq))

    print('Tamanho de {} = {} Mbytes'.format(caminho, tam))
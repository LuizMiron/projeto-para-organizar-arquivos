import os

# 1. Criar pastas: imagens, audios e documentos obs: pasta "outros" já existe
def criar_pastas(diretorio):
    lista = []
    lista.append(os.path.join(diretorio, 'audios'))
    lista.append(os.path.join(diretorio, 'imagens'))
    lista.append(os.path.join(diretorio, 'documentos'))
    lista.append(os.path.join(diretorio, 'videos'))
    lista.append(os.path.join(diretorio, 'outros'))

    for pasta in lista:
        if not os.path.isdir(pasta):
            os.mkdir(pasta)

# 2. Pegar o nome dos arquivos
def organizar(diretorio):
    arquivos = os.listdir(diretorio)

    for arq in arquivos:
        extensao = ext_arquivos(arq)

# 3. Pegar sua extensão para deternimar o seu tipo
def ext_arquivos(arquivo):
    if arquivo.count('.') > 0:
        index = arquivo.rfind('.')
        return arquivo[index:]
    else:
        pass

# 4. Mover determinado arquivo nas pastas, baseado no seu tipo
def mover_arq():
    pass

# organizar('arquivos')
criar_pastas('arquivos')

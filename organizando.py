import os


# 1. Pegar o nome dos arquivos
def nome_arquivos(diretorio):
    arquivos = os.listdir(diretorio)

    for arq in arquivos:
        ext_arquivos(arq)

# 2. Pegar sua extensão para deternimar o seu tipo
def ext_arquivos(arquivo):
    if arquivo.count('.') > 0:
        est = arquivo.split('.')
        print(est[-1])
    else:
        print('é uma pasta!')
# 3. Criar pastas: imagens, audios e documentos obs: pasta "outros" já existe
# 4. Mover determinado arquivo nas pastas, baseado no seu tipo
nome_arquivos('arquivos')

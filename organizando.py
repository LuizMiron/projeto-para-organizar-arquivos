import os

# 1. Criar pastas: imagens, audios e documentos obs: pasta "outros" já existe
def criar_pastas(diretorio):
    AUDIOS_DIR = os.path.join(diretorio, 'audios')
    IMAGENS_DIR = os.path.join(diretorio, 'imagens')
    DOCS_DIR = os.path.join(diretorio, 'documentos')
    VIDEOS_DIR = os.path.join(diretorio, 'videos')
    OUTROS_DIR = os.path.join(diretorio, 'outros')


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
# 1. Criar pastas: imagens, audios e documentos obs: pasta "outros" já existe
# 4. Mover determinado arquivo nas pastas, baseado no seu tipo
organizar('arquivos')

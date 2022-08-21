from genericpath import isfile
import os


# lista dos diretorios das pastas
dicionario = dict()

# lista de extensões de cada tipo
audios_ext = ['.mp3', '.wav']
imagens_ext = ['.img', '.jpg', '.jpeg']
documentos_ext = ['.txt', '.doc', '.docx', '.pdf', '.log']
videos_ext = ['.mp4', '.mov', '.avi']


# 1. Criar pastas: imagens, audios e documentos obs: pasta "outros" já existe
def criar_pastas(diretorio):
    global dicionario
    dicionario.update({'audios': os.path.join(diretorio, 'audios')})
    dicionario.update({'imagens': os.path.join(diretorio, 'imagens')})
    dicionario.update({'docs': os.path.join(diretorio, 'documentos')})
    dicionario.update({'videos': os.path.join(diretorio, 'videos')})
    dicionario.update({'outros': os.path.join(diretorio, 'outros')})

    for pasta in dicionario.values():
        if not os.path.isdir(pasta):
            os.mkdir(pasta)


# Função para pegar a extensão do arquivo
def ext_arquivos(nome):
    index = nome.rfind('.')
    return nome[index:]


# 2. Pegar o nome dos arquivos
def organizar(diretorio):
    criar_pastas(diretorio)
    arquivos = os.listdir(diretorio)

    for arq in arquivos:
        if os.path.isfile(os.path.join(diretorio, arq)):
            # 3. Pegar sua extensão para deternimar o seu tipo
            extensao = str(ext_arquivos(arq)).lower()
            print(arq, extensao)

            # 4. Mover determinado arquivo nas pastas, baseado no seu tipo
            nova_pasta = str()
            if extensao in audios_ext:
                nova_pasta = dicionario['audios']
            elif extensao in imagens_ext:
                nova_pasta = dicionario['imagens']
            elif extensao in documentos_ext:
                nova_pasta = dicionario['docs']
            elif extensao in videos_ext:
                nova_pasta = dicionario['videos']
            else:
                nova_pasta = dicionario['outros']
            
            velho = os.path.join(diretorio, arq)
            novo = os.path.join(nova_pasta, arq)
            os.rename(velho, novo)
            print(f'Moveu: {velho} -> {novo}')


if __name__ == '__main__':
    organizar('arquivos')

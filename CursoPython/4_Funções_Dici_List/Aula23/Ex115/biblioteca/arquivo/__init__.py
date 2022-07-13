from biblioteca import menu

def arquivoExiste(nome):
    try:
        with open(nome,'r') as arquivo:
            arquivo.read()
    except FileNotFoundError:
        return False
    else: 
        return True

def criarArquivo(nome):
    try:
        with open(nome,'w') as arquivo:
            arquivo.close()
            
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')

def lerArquivo(nome):
    try:
        arquivo = open(nome,'r',encoding="utf-8")
    except:
        print('Erro ao ler o arquivo!')
    else:
        menu.cabeçalho('PESSOAS CADASTRADAS')
        for linha in arquivo:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:<30}{dado[1]:>5} anos')
        
    finally:
        arquivo.close()

def cadastrar(arq,nome='desconhecido',idade=0):
    try:
        arquivo = open(arq,'a')
    except:
        print('Houve um ERRO na abertura do arquivo')
    else:
        try:
            arquivo.write(f'{nome};{idade}\n')
        except:
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado.')
        finally:
            arquivo.close()
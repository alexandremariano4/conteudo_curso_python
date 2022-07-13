from time import sleep
from biblioteca import arquivo
from biblioteca import menu

arq = 'cursoemvideo.txt'

if arquivo.arquivoExiste(arq):
    print('Arquivo encontrado com sucesso!')
else:
    print('Aquivo não encontrado')
    arquivo.criarArquivo(arq)
    
    
while True:
    resposta = menu.menu(['Ver pessoas cadastradas','Cadastrar nova pessoa','Sair do sistema'])
    if resposta == 1:
        #Opção de lista o conteúdo!
        arquivo.lerArquivo(arq)
    elif resposta == 2:
        menu.cabeçalho('NOVO CADASTRO')
        #Cadastrar uma nova pessoa
        nome = str(input('Nome: '))
        idade = menu.leiaInt('Idade: ')
        arquivo.cadastrar(arq,nome,idade)
        

    elif resposta == 3:
        menu.cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida\033[m')
    sleep(2)
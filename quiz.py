
'''
iMPORTEI AS BIBLIOTECAS DO JASON E DO WINDOS PARA LIMPAR O TERMINAL, JSON PARA SALVAR E SYS PARA SAIR DO JOGO
'''
import os
import json
import sys
import random



'''
CRIEI A LISTA DE JOGADOR3ES E AS DEMAIS VARIAVEIS GLOBAIS
'''
lista_de_jogadores = []
nome_json = "C:\\Users\\IANCA\\Documents\\Quiz\\dados.json"
questoes_json = "C:\\Users\\IANCA\\Documents\\Quiz\\banco_de_perguntas.json"
lista_questoes = []



'''
ESTRUTURA DO JOGO
'''

def perguntas ():
    pergunta = random.choice(lista_questoes)
    print("Pergunta:", pergunta["pergunta"])
    print("Alternativas:")



    for i, alternativa in enumerate(pergunta["alternativas"]):
        print(f"{i + 1}. {alternativa['resposta']}")
    resp = int(input('Digite sua alternativa: '))
    indice_resposta_correta = next((i for i, alternativa in enumerate(pergunta["alternativas"]) if alternativa["correta"]), None)
    if resp - 1 == indice_resposta_correta:
        print('Resposta correta!')
        

        #DELETAR QUESTÃO PARA ELA NÃO REPETIR
        lista_questoes.remove(pergunta)

             
        return(10)
        
    else:
        print('Resposta incorreta!')
        input
        return (0)

def jogar():
    for i in range (4):
        for jogador in lista_de_jogadores:
            print("Agora é a vez de: {}!".format(jogador["nome"]))
            jogador["pontuacao"] = perguntas() + jogador["pontuacao"] 
            input
            os.system('cls')

def carrega_perguntas():
    with open (questoes_json, 'r' ,encoding="utf8") as arquivo_json:
        data = json.load(arquivo_json)
        questoes = data ['questoes']
        return(questoes)


    
'''
ORDENANDO LISTA DO RANKING
'''
def ranking ():
    ranking_list = sorted(lista_de_jogadores, key = lambda x: x['pontuacao'], reverse=True)
    cont = 1

    for jogador in (ranking_list):
        print(cont,"º Lugar")
        print(f"Jogador: {jogador['nome']}, Pontuação: {jogador['pontuacao']}")
        cont = cont + 1

'''
FUNÇÃO CRIADA PARA SALVAR O NOME DOS JOGADORES
'''
def salvar_play ():
    with open(nome_json, 'w') as arquivo_json:
        json.dump(lista_de_jogadores, arquivo_json)
    print('lista salva')
  
'''
FUNÇAO DE CADASTRO NA VARIÁVEL GLOBAL (LISTA)
'''
def cadastro_de_jogadores ():

    for i in range (3):
        nome = str(input('Digite o nome do {}º: '.format(i+1)))
        jogador = {
            "id": i+1,
            "nome": nome,
            "pontuacao": i + 1
        }
        lista_de_jogadores.append (jogador)
    os.system('cls')
   
    
'''
TERMINAL DO JOGO
'''
print("""
      
************************************** BEM VINDO AO NOME DO JOGO ***************************************************


*************************************** CONHECIMENTOS GERAIS ***************************************************

*********************************************** MENU ***************************************************

1 - JOGAR
2 - SAIR

""")


lista_questoes = carrega_perguntas()

while True:
    resp = int(input('Escolha sua opção: '))

    if resp == 1:
        os.system('cls')
        print('Inicio do jogo')
        cadastro_de_jogadores ()
        jogar()
        ranking()
        print('****** Parabéns por participar do Quiz! Até logo! ******')
        break
      
    else:    
       print ('****** Volte logo! ******')
       
    sys.exit()




nomes = []
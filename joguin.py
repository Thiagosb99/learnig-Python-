from time import sleep
import re
import random
nome=''
vez=1

def quiz():
    vez = 2
    print("Voce selecionou o Quiz. Deseja prosseguir?\n")
    x = int(input("Digite 1 para continuar ou 0 para retornar ao menu:\n"))
    if (x == 1):
        print()
        print('Quiz\n')
        sleep(1.5)
        print('Agora vamos testar seus conhecimentos sobre o UCM\nSerão 5 perguntas, valendo 10 pontos cada\n')
        sleep(2.5)

        placar = 0

        print('1) Qual equipe formou o primeiro esquadrão dos vingadores nos cinemas?\n')
        sleep(2.5)

        print('a) Capitã Marvel, Gavião Arqueiro, Visão e Hulk')
        print('b) Homem de Ferro, Thor, Hulk, Visão e Mercúrio')
        print('c) Hulk, Thor, Capitão América, Homem de Ferro, Viúva Negra e Gavião Arqueiro')
        print('d) Visão, Thor, Hulk, Cappitã Marvel e Pantera Negra\n')


        resp = input('Qual a alternativa correta? ')
        sleep(2)
        print()

        if resp == 'c':
            print('Parabéns, você acertou! Vamos para a próxima pergunta\n')
            placar = placar + 10
        else:
            print('Resposta errada! Vamos para a próxima pergunta\n')
        sleep(2)

        # segunda pergunta #####################################
        print('2) Quem foi o fundador da inciativa vingadores?\n')
        sleep(2)

        print('a) Tony Stark')
        print('b) Nick Fury')
        print('c) Peggy Carter')
        print('d) Maria Hill\n')


        resp = input('Qual a alternativa correta? ')
        sleep(2)
        print()

        if resp == 'b':
            print('Parabéns, você acertou! Vamos para a próxima pergunta\n')
            placar = placar + 10
        else:
            print('Resposta errada! Vamos para a próxima pergunta\n')
        sleep(2)

        # terceira pergunta ################################
        print('3) Quais personagens levantaram Mjolnir (Martelo de Thor) até Vingadores Ultimato ?\n')
        sleep(2)

        print('a) Hulk, Thor e Visão')
        print('b) Thor, Visão e Capitão América')
        print('c) Homem de Ferro, Thor e Hulk')
        print('d) Apenas Thor é digno\n')


        resp = input('Qual a alternativa correta? ')
        sleep(2)
        print()

        if resp == 'b':
            print('Parabéns, você acertou! Vamos para a próxima pergunta\n')
            placar = placar + 10
        else:
            print('Resposta errada! Vamos para a próxima pergunta\n')
        sleep(2)

        # quarta pergunta ############################
        print('4) Quantos filmes confirmados pela Marvel, fazem parte da saga do infinito?\n')
        sleep(2)

        print('a) 23 filmes')
        print('b) 4 filmes')
        print('c) 15 filmes')
        print('d) 22 filmes\n')


        resp = input('Qual a alternativa correta? ')
        sleep(2)
        print()

        if resp == 'a':
            print('Parabéns, você acertou! Vamos para a próxima pergunta\n')
            placar = placar + 10
        else:
            print('Resposta errada! Vamos para a pergunta bônus\n')
        sleep(2)

        # quinta pergunta ###########################
        print('Pergunta bonus:\n')
        print('5) Quem criou o Ultron?\n')
        sleep(2)

        print('a) S.H.I.E.L.D')
        print('b) Bruce Banner e Tony Stark')
        print('c) Bruce Banner')
        print('d) Tony Stark\n')

        resp = input('Qual a alternativa correta? ')
        sleep(2)
        print()

        if resp == 'd':
            print('Parabéns, você acertou! Chegamos ao fim do Quiz\n')
            placar = placar + 10
        else:
            print('Resposta errada! Chegamos ao fim do Quiz\n')

        sleep(2)
        print('Agora vamos calcular sua pontuação\n')
        for i in range(0, 3):
            print(".", end="")
            sleep(1)
        print("\n")

        # condiçoes do placar ###########
        if placar == 50:
            print('50 pontos\nParabéns!!! ',nome,', Gênio! Você atingiu a pontuação máxima')

        elif placar == 40:
            print('40 pontos\nParabéns!!! ',nome,', Você tem grande conhecimento sobre o Universo Marvel')

        elif placar == 30:
            print('30 pontos\n',nome,' Você foi bem, acertou metade das perguntas')

        elif placar == 20:
            print('20 pontos\n',nome,' Você acertou apenas 2 questões')

        elif placar == 10:
            print('10 pontos\n',nome,' É... Você não prestou muita atenção nos filmes...')

        elif placar == 0:
            print('0 pontos\nXiii... Provavelmente você é um fã da DC... :)')

        input("\nPressione enter para voltar ao menu principal... ")

        menu(vez)

    elif (x == 0):
        menu(vez)

def sinopse():
    vez = 2
    print("Voce selecionou a Sinopse do Filme. Deseja prosseguir?\n")
    y = int(input("Digite 2 para continuar ou 0 para retornar ao menu: \n"))
    if(y == 2):
         print("Após Thanos eliminar metade das criaturas vivas, os Vingadores têm\n"
         "de lidar com a perda de amigos e entes queridos. Com Tony Stark vagando\n"
         "perdido no espaço sem água e comida, Steve Rogers e Natasha Romanov lideram a\n"
         "resistência contra o titã louco.")
         input("\nPressione enter para voltar ao menu principal... ")
         menu(vez)
    elif(y == 0):
        menu(vez)

def elenco():
    vez = 2
    print("Voce selecionou Elenco e Personagens. Deseja prosseguir?\n")
    z = int(input("Digite 3 para continuar ou 0 para retornar ao menu: \n"))
    if(z == 3):
        print("ELENCO VINGADORES ULTIMATO")
        print(26*"—","\n")
        print("Robert Downey Jr. como Tony Stark / Homem de Ferro:\n"
              "O líder e benfeitor dos Vingadores que é auto-descrito como gênio, bilionário,\n"
              "playboy e filantropo que usa trajes eletromecânicos de sua própria criação.\n"
              "______________________________________________________________________________\n\n"
              "Chris Evans como Steve Rogers / Capitão América:\n"
              "Também líder dos Vingadores e um veterano da Segunda Guerra Mundial que foi\n"
              "aprimorado fisicamente através de um soro experimental e congelado até acordar no mundo moderno.\n"
              "________________________________________________________________________________________________\n\n"
              "Mark Ruffalo como Bruce Banner / Hulk:\n"
              "Um vingador e cientista genial, que após uma explosão envolvendo radiação gama,\n"
              "se transforma num monstro verde quando irritado ou enfurecido.\n"
              "_______________________________________________________________________________\n\n"
              "Chris Hemsworth como Thor:\n"
              "Um Vingador e rei de Asgard baseado na divindade nórdica de mesmo nome.\n"
              "Thor agora possui um machado místico conhecido como Stormbreaker, após a destruição de seu\n"
              "martelo Mjolnir em Thor: Ragnarok.\n"
              "__________________________________________________________________________________________\n\n"
              "Scarlett Johansson como Natasha Romanoff / Viúva Negra:\n"
              "Uma espiã russa altamente treinada que é ex-membra dos Vingadores e ex-agente da\n"
              "organização S.H.I.E.L.D.\n"
              "________________________________________________________________________________\n\n"
              "Jeremy Renner como Clint Barton / Gavião Arqueiro:\n"
              "Um mestre arqueiro, ex-membro dos Vingadores e ex-agente da S.H.I.E.L.D.\n"
              "Barton tem um novo visual no filme, visualmente semelhante ao Ronin dos quadrinhos.\n"
              "___________________________________________________________________________________\n\n"
              "Don Cheadle como James Rhodes / Máquina de Combate:\n"
              "Um ex-oficial da Força Aérea dos Estados Unidos que usa a armadura Máquina de Combate e\n"
              "melhor amigo de Tony Stark.\n"
              "_______________________________________________________________________________________\n\n"
              "Paul Rudd como Scott Lang / Homem-Formiga:\n"
              "Um ex-presidiário que adquiriu um traje que lhe permite diminuir seu tamanho,\n"
              "mas aumentar sua força e comandar formigas telepaticamente.\n"
              "_____________________________________________________________________________\n\n"
              "Karen Gillan como Nebulosa:\n"
              "Filha adotiva de Thanos, foi criada com Gamora e hoje é uma\n"
              "membra relutante dos Guardiões da Galáxia.\n"
              "___________________________________________________________\n\n"
              "Bradley Cooper como Rocket Raccoon:\n"
              "Um membro dos Guardiões da Galáxia que é um Guaxinim falante, geneticamente modificado,\n"
              "caçador de recompensas e um mercenário mestre em armas e táticas de batalha.\n"
              "____________________________________________________________________________\n\n"
              "Brie Larson como Carol Danvers / Capitã Marvel:\n"
              "Uma ex-pilota da Força Aérea dos Estados Unidos que ganhou habilidades sobre-humanas ao\n"
              "ser exposta à explosão de um motor de aceleração abastecido pela energia do Tesseract.\n"
              "Danvers foi, inicialmente, recrutada para integrar à força militar de elite Kree, conhecida como\n"
              "Starforce, porém desertou seu posto como guerreira Kree para reparar erros do seu antigo povo e\n"
              "dar um novo lar para os refugiados Skrulls (explicando sua ausência nos últimos 20 anos).\n"
              "Ela possui poderes como: força sobre-humana, projeção de energia e vôo.\n"
              "________________________________________________________________________________________________\n\n"
              "Danai Gurira como Okoye:\n"
              "Líder das Dora Milaje, da guarda real de Wakanda.\n"
              "_________________________________________________\n\n"
              "Josh Brolin como Thanos:\n"
              "Um déspota intergalático que reuniu as Joias do Infinito com objetivo de dizimar metade do universo.\n"
              "____________________________________________________________________________________________________\n\n")
        input("\nPressione enter para voltar ao menu principal... ")
        menu(vez)
    elif(z == 0):
        menu(vez)

def letras():

   vogais = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

   letra = random.randint(0,25)
   return vogais[letra]

def caca_palavras():
    vez=2
    print("Voce selecionou Caça-palavras. Deseja prosseguir?\n")
    y = int(input("Digite 4 para continuar ou 0 para retornar ao menu: \n"))
    if y==4:
        print("Há um Vingador nesse caça-palavras você consegue encontrá-lo? \n")
        print(21*".")
        for l in range(0, 10):
            if l == 0:
                print("\n ", end="")
            else:
                print(l, "", end="")
            for c in range(0, 10):
                if l == 0:
                    print("", c, end="")
                elif c == 4:
                    if l == 4:
                        print("R ", end="")
                    elif l == 5:
                        print("O ", end="")
                    elif l == 6:
                        print("H ", end="")
                    elif l == 7:
                        print("T ", end="")
                    else:
                        a = letras()
                        print(a + " ", end="")
                else:
                    a = letras()
                    print(a + " ", end="")
                if c == 9:
                    print()
        print(21 * ".","\n")
        ver = True
        while ver==True:
            print("Responda com as coordenadas da seguinte forma: linha,coluna-\nExemplo 1,1-1,2\n")
            print("Digite 0 caso queira voltar ao Menu Principal")
            coord = input()
            if coord=="0":
                ver=False
                menu(vez)
            elif re.search("\d{1},\d{1}-",coord):
                ver=False
                if (coord=="7,4-6,4-5,4-4,4"):
                    for l in range(0,9):
                        for c in range(0,21):
                            if c==10:
                                if l==4:
                                    print("R",end="")
                                elif l==5:
                                    print("O",end="")
                                elif l==6:
                                    print("H",end="")
                                elif l==7:
                                    print("T",end="")
                                else:
                                    print("*", end="")
                            else:
                                print("*",end="")
                            if c==20:
                                print()
                    print("Thor encontrado!\n")
                    input("Pressione enter para voltar ao Menu Principal...")
                    menu(vez)
                elif (coord!="7,4-6,4-5,4-4,4"):
                    print("Vingador não encontrado.\n")
                    input("Pressione enter para voltar ao Menu Principal...")
                    menu(vez)
            else:
                print("Você não digitou no formato especificado, tente novamente seguindo o exemplo.\n")
    elif y==0:
        menu(vez)

def menu(vex):
    global nome
    global vez
    print("""
    ..........................................................
       Bem vindo ao menu de opções               
                                                  ###
                                                 ####
          1 - Quiz                              ## ##
          2 - Sinopse do Filme                 ######
          3 - Elenco/ Personagens             ##   ##
          4 - Caça-palavras                  ##
          5 - Sair  
    ..........................................................\n""")
    if vex==1:
        nome=input("Antes de começar, gostariamos de saber o seu nome: ")
        vez=2
    opcao = int(input("{} escolha entre uma das opções acima: ".format(nome)))
    print()

    if (opcao == 1):
        quiz()
    elif (opcao == 2):
        sinopse()
    elif (opcao == 3):
        elenco()
    elif (opcao == 4):
        caca_palavras()
    elif (opcao == 5):
        print("Até a próxima", nome,"!")
        exit()
    else:
        print("Este número não está nas opções. Tente novamente.\n")
        menu(vez)



while vez>=1:
    try:
        menu(vez)
        vez=2
    except ValueError:
        print()
        print("Essa opção não existe! Tente Novamente")

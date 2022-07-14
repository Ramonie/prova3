def ini_matriz(tamanho):
# Para iniciar a matriz:
    m = [['' for g in range (tamanho[1])] for i in range(tamanho[0])]
    return m

def mostra_matriz(matriz):
# Para printar a matriz:
    print('  1   2   3   4   5   6')
    print("-------------------------")
    for linha in matriz:
        print("| ", end="")
        for elemento in linha:
            print(elemento, end=" | ")
        print("")
    print("-------------------------")

def jogada(matriz,coluna,token):

  # Colocar o jogo matriz


  for i in range(len(matriz)-1,-1,-1):

     token , matriz[i][coluna] = matriz[i][coluna], token


  return matriz

def verificar(jogo):

  # Verificação de jogadores

  for i in range(len(jogo)):

    cont = [0,0] #Matriz para contar quantas pecas tem na horizontal


    for j in range(len(jogo[i])):

        if cont[1] >= 4:

              return cont[0]
        elif jogo[i][j]:

              if cont[0] ==jogo[i][j]:

                  cont[1]+=1

              else:

                  cont[0] = jogo[i][j]

                  cont[1] = 1

        else:

              cont = [0,0]

    for i in range(len(jogo[1])):

      cont = [0,0]

#Matriz contador de pencas verticais

      for j in range(len(jogo)):

        if jogo[j][i]:


              if cont[0] ==jogo[j][i]:

                  cont[1]+=1

              else:


                  cont[0] = jogo[j][i]


                  cont[1] = 1


        else:


              cont = [0,0]


        if cont[1] >= 4:


              return cont[0]

               

  for i in range(4-1,len(jogo)):

      for g in range(len(jogo[1])-(4-1)):

          cont = [0,0]

# matriz para contar quantas pecas tem na diagonal

          for k in range(4):

              if jogo[i-k][g+k]:


                  if cont[0] ==jogo[i-k][g+k]:


                      cont[1]+=1


                  else:


                      cont[0] = jogo[i-k][g+k]


                      cont[1] = 1


              else:


                  break


          if cont[1] >= 4:


              return cont[0]

  for i in range(len(jogo)-(4-1)):

      for g in range(len(jogo[1])-(4-1)):

          cont = [0,0]

# Matriz contagem de diagonal

          for k in range(4):

              if jogo[i+k][g+k]:

                  if cont[0] ==jogo[i+k][g+k]:

                     cont[1]+=1

                  else:

                      cont[0] = jogo[i+k][g+k]

                      cont[1] = 1


              else:


                  break


          if cont[1] >= 4:


              return cont[0]


  return 0


         

def main():

  tamanho = (6,6) #serve pra setar o tamanho do jogo

  jogo = ini_matriz(tamanho)

  ganhou = 0

# parar o jogo

  jogador = 0

# quem vai jogar

  while not ganhou:

      mostra_matriz(jogo)

      print('Quem vai jogar é o jogador ', jogador%2 +1,'.')

      print('Escolha em qual coluna você quer jogar (escolha de 1 a ',tamanho[1],'): ')

      escolha = int(input())

      while escolha<1 or escolha>tamanho[1]:

              print('Número inválido.')

              print('Escolha em qual coluna você quer jogar (escolha de 1 a ',tamanho[1],'): ')

              escolha = int(input())

      jogo = jogada(jogo,escolha-1, jogador%2 +1)

      ganhou = verificar(jogo)

      jogador +=1

             

  mostra_matriz(jogo)

  print('O jogador', ganhou,' venceu!!')

  return main

if __name__ == "__main__":

  main()


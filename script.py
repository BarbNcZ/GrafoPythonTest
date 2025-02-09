import graphviz as gv
import uuid
from collections import defaultdict

'''-1 = espaço vazio
0 = estrada
a(ID) = armazem
(ID) = predio'''

x = [[str(uuid.uuid4()) + "_-1" , str(uuid.uuid4()) + "_0_1" , str(uuid.uuid4()) + "_-1" , str(uuid.uuid4()) + "_0_2" , str(uuid.uuid4()) + "_-1" , str(uuid.uuid4()) + "_-1" , str(uuid.uuid4()) + "_00_3" , str(uuid.uuid4()) + "_00_3" , str(uuid.uuid4()) + "_-1" , str(uuid.uuid4()) + "_-1" ],
     [str(uuid.uuid4()) + "_5" , str(uuid.uuid4()) + "_0_1" , str(uuid.uuid4()) + "_-1" , str(uuid.uuid4()) + "_0_2" , str(uuid.uuid4()) + "_a3" , str(uuid.uuid4()) + "_8" , str(uuid.uuid4()) + "_00_3" , str(uuid.uuid4()) + "_00_3" , str(uuid.uuid4()) + "_a2" , str(uuid.uuid4()) + "_a2" ],
     [str(uuid.uuid4()) + "_-1" , str(uuid.uuid4()) + "_0_4_1" , str(uuid.uuid4()) + "_-1" , str(uuid.uuid4()) + "_0_4_2" , str(uuid.uuid4()) + "_a3" , str(uuid.uuid4()) + "_8" , str(uuid.uuid4()) + "_00_3_4" , str(uuid.uuid4()) + "_00_3_4" , str(uuid.uuid4()) + "_-1" , str(uuid.uuid4()) + "_-1" ],
     [str(uuid.uuid4()) + "_00_4" , str(uuid.uuid4()) + "_00_4_1" , str(uuid.uuid4()) + "_00_4" , str(uuid.uuid4()) + "_00_4_2" , str(uuid.uuid4()) + "_00_4" , str(uuid.uuid4()) + "_00_4" , str(uuid.uuid4()) + "_00_4_3" , str(uuid.uuid4()) + "_00_4_3" , str(uuid.uuid4()) + "_00_4" , str(uuid.uuid4()) + "_00_4" ],
     [str(uuid.uuid4()) + "_00_4" , str(uuid.uuid4()) + "_00_4_1" , str(uuid.uuid4()) + "_00_4" , str(uuid.uuid4()) + "_00_4_2" , str(uuid.uuid4()) + "_00_4_2" , str(uuid.uuid4()) + "_00_4" , str(uuid.uuid4()) + "_00_4_3" , str(uuid.uuid4()) + "_00_4_3" , str(uuid.uuid4()) + "_00_4" , str(uuid.uuid4()) + "_00_4" ],
     [str(uuid.uuid4()) + "_-1" , str(uuid.uuid4()) + "_0_4_1" , str(uuid.uuid4()) + "_9" , str(uuid.uuid4()) + "_00_2_4" , str(uuid.uuid4()) + "_00_2_4" , str(uuid.uuid4()) + "_-1" , str(uuid.uuid4()) + "_00_3_4" , str(uuid.uuid4()) + "_00_3_4" , str(uuid.uuid4()) + "_6" , str(uuid.uuid4()) + "_6" ],
     [str(uuid.uuid4()) + "_-1" , str(uuid.uuid4()) + "_0_1" , str(uuid.uuid4()) + "_9" , str(uuid.uuid4()) + "_00_2" , str(uuid.uuid4()) + "_00_2" , str(uuid.uuid4()) + "_7" , str(uuid.uuid4()) + "_00_3_5" , str(uuid.uuid4()) + "_00_3_5" , str(uuid.uuid4()) + "_0_3_5" , str(uuid.uuid4()) + "_0_5" ],
     [str(uuid.uuid4()) + "_-1" , str(uuid.uuid4()) + "_0_1" , str(uuid.uuid4()) + "_9" , str(uuid.uuid4()) + "_00_2" , str(uuid.uuid4()) + "_00_2" , str(uuid.uuid4()) + "_-1" , str(uuid.uuid4()) + "_00_3" , str(uuid.uuid4()) + "_00_3" , str(uuid.uuid4()) + "_-1" , str(uuid.uuid4()) + "_-1" ],
     [str(uuid.uuid4()) + "_0_6" , str(uuid.uuid4()) + "_0_1_6" , str(uuid.uuid4()) + "_0_6" , str(uuid.uuid4()) + "_00_2_6" , str(uuid.uuid4()) + "_00_2_6" , str(uuid.uuid4()) + "_0_6" , str(uuid.uuid4()) + "_00_3_6" , str(uuid.uuid4()) + "_00_3_6" , str(uuid.uuid4()) + "_-1" , str(uuid.uuid4()) + "_-1" ],
     [str(uuid.uuid4()) + "_a1" , str(uuid.uuid4()) + "_a1" , str(uuid.uuid4()) + "_a1" , str(uuid.uuid4()) + "_-1" , str(uuid.uuid4()) + "_10" , str(uuid.uuid4()) + "_10" , str(uuid.uuid4()) + "_00_3" , str(uuid.uuid4()) + "_00_3" , str(uuid.uuid4()) + "_a4" , str(uuid.uuid4()) + "_a4" ]]

def dividirID(id):

     if id == None:
          return

     idDividido = id.split('_')

     if len(idDividido) == 2:
          return [idDividido[1]]

     uuid = idDividido[0]
     espessura = idDividido[1]
     idRuaLarga = idDividido[2]
     if len(idDividido) > 3:
          idRuaEstreita = idDividido[3]

     else:
          idRuaEstreita = None

     return [espessura, idRuaLarga, idRuaEstreita, uuid]

def printValores(element, y, x, indiceColuna, indiceLinha):
     print('Element ', element)
     print('Right ', getElementRight(y, indiceColuna) [0])
     print('Left ', getElementLeft(y, indiceColuna) [0])
     print('Top ', getElementTop(indiceColuna, y, x, indiceLinha) [0])
     print('Down ', getElementDown(indiceColuna, y, x, indiceLinha) [0])
     print('Top Diagonal Left ', getDiagonalTopLeft(indiceColuna, y, x, indiceLinha))
     print('Top Diagonal Right ', getDiagonalTopRight(indiceColuna, y, x, indiceLinha))
     print('Down Diagonal Left ', getDiagonalDownLeft(indiceColuna, y, x, indiceLinha))
     print('Down Diagonal Right ', getDiagonalDownRight(indiceColuna, y, x, indiceLinha))

def getElementRight(row, indiceColuna):
     if len(row) == 0:
          return

     '''buscar o indice de um elemento dentro de um array'''

     if indiceColuna < 0:
          return
     elif indiceColuna >= len(row) - 1:
          return
     else:
          return [row[indiceColuna + 1], row, indiceColuna + 1]

def getElementLeft(row, indiceColuna):
     if len(row) == 0:
          return

     if indiceColuna <= 0:
          return
     else:
          return [row[indiceColuna - 1], row, indiceColuna - 1]

def getElementTop(indiceColuna, row, array, indiceLinha):

     '''evitar erro/excecao de indexOutOfBounds'''
     if array == None or len(array) == 0:
          return
     if len(row) == 0:
          return

     if indiceLinha <= 0:
          return
     else:
          topRow = array[indiceLinha - 1]

     if indiceColuna >=0 and indiceColuna <= len(topRow) - 1:
          return [topRow[indiceColuna], topRow, indiceLinha - 1]
     else:
          return

def getElementDown(indiceColuna, row, array, indiceLinha):
     '''evitar erro/excecao de indexOutOfBounds'''
     if array == None or len(array) == 0:
          return
     if len(row) == 0:
          return

     if indiceLinha >= len(row) - 1:
          return
     else:
          downRow = array[indiceLinha + 1]

     if indiceColuna >=0 and indiceColuna <= len(downRow) - 1:
          return [downRow[indiceColuna], downRow, indiceLinha + 1]
     else:
          return

def getDiagonalTopLeft(indiceColuna, row, array, indiceLinha):

     if array == None or len(array) == 0:
          return
     if len(row) == 0:
          return

     if indiceLinha <= 0:
          return
     else:
          topRow = array[indiceLinha - 1]

     if indiceColuna >=0 and indiceColuna <= len(topRow) - 1:
          elementLeft = getElementLeft(topRow, indiceColuna)
          if elementLeft == None:
               return
          else:
               return elementLeft [0]

     else:
          return

def getDiagonalTopRight(indiceColuna, row, array, indiceLinha):

     if array == None or len(array) == 0:
          return
     if len(row) == 0:
          return

     if indiceLinha <= 0:
          return
     else:
          topRow = array[indiceLinha - 1]

     if indiceColuna >=0 and indiceColuna <= len(topRow) - 1:
          elementRight = getElementRight(topRow, indiceColuna)
          if elementRight == None:
               return
          else:
               return elementRight[0]

     else:
          return

def getDiagonalDownLeft(indiceColuna, row, array, indiceLinha):
     '''evitar erro/excecao de indexOutOfBounds'''
     if array == None or len(array) == 0:
          return
     if len(row) == 0:
          return

     if indiceLinha >= len(row) - 1:
          return
     else:
          downRow = array[indiceLinha + 1]

     if indiceColuna >= 0 and indiceColuna <= len(downRow) - 1:
          elementLeft = getElementLeft(downRow, indiceColuna)
          if elementLeft == None:
               return
          else:
               return elementLeft[0]
     else:
          return

def getDiagonalDownRight(indiceColuna, row, array, indiceLinha):
     '''evitar erro/excecao de indexOutOfBounds'''
     if array == None or len(array) == 0:
          return
     if len(row) == 0:
          return

     if indiceLinha >= len(row) - 1:
          return
     else:
          downRow = array[indiceLinha + 1]

     if indiceColuna >=0 and indiceColuna <= len(downRow) - 1:
          elementRight = getElementRight(downRow, indiceColuna)
          if elementRight == None:
               return
          else:
               return elementRight[0]
     else:
          return

def interseccao(indiceColuna, row, array, indiceLinha):

     element = row[indiceColuna]

     #dividindo ID do elemento a ser processado
     idDividido = dividirID(element)

     if idDividido == None:
          return

     '''Verificando se o elemento a ser processado é um estrada com base na informacao de espessura
     trazida pelo ID que foi dividido'''
     isRoad = idDividido [0] == '0' or idDividido[0] == '00'

     #Se a variável acima não é verdadeira, entao nao ha interseccoes, retornando nada
     if not isRoad:
          return

     #Buscando as 4 diagonais do elemento a ser processado
     diagonalTopLeft = getDiagonalTopLeft(indiceColuna, row, array, indiceLinha)
     diagonalTopRight = getDiagonalTopRight(indiceColuna, row, array, indiceLinha)
     diagonalDownLeft = getDiagonalDownLeft(indiceColuna, row, array, indiceLinha)
     diagonalDownRight = getDiagonalDownRight(indiceColuna, row, array, indiceLinha)

     diagonais = [diagonalTopLeft, diagonalTopRight, diagonalDownLeft, diagonalDownRight]

     #Filtrando e armazenando em um array apenas as diagonais identificadas com estrada
     estradas = [x for x in diagonais if dividirID(x) != None and (dividirID(x) [0] == '0' or dividirID(x) [0] == '00')]

     #Se a quantidade de estradas identificadas for igual a 2
     if len(estradas) == 2:

          idEstrada1 = None
          idEstrada2 = None

          #Extraindo o id/nome das 2 estradas
          for estrada in estradas:
              estradaDividida = dividirID(estrada)

              if idEstrada1 == None:
                   idEstrada1 = estradaDividida [1]

              else:
                   idEstrada2 = estradaDividida [1]

          '''Verificando se o id/nome das 2 estradas sao o mesmo, sendo assim retorna o UUID do espaço
          e o tipo de interseccao (estradas de mesma espessura) representado por x'''
          if idEstrada2 != None and idEstrada1 != None and idEstrada2 == idEstrada1:
               return idDividido[len(idDividido) - 1] + '_x'

          else:
               return

     #Se a quantidade de estradas identificadas for igual a 3
     elif len(estradas) == 3:
          idEstrada1 = None
          idEstrada2 = None
          idEstrada3 = None


          #Extraindo o id/nome das 3 estradas
          for estrada in estradas:
               estradaDividida = dividirID(estrada)

               if idEstrada1 == None and idEstrada2 == None:
                    idEstrada1 = estradaDividida[1]

               elif idEstrada2 == None:
                    idEstrada2 = estradaDividida[1]

               else:
                    idEstrada3 = estradaDividida[1]

          '''Verificando se o id/nome das 2 estradas sao o mesmo, e o id/nome de uma estrada é o mesmo
          do elemento a ser processado, sendo assim retorna o UUID do espaço e o tipo de interseccao
          (estradas de espessuras diferentes) representado por y'''
          if idEstrada2 != None and idEstrada1 != None and idEstrada3 != None:
               idEstradas = [idEstrada1, idEstrada2, idEstrada3]

               groups = defaultdict(list)

               for num in idEstradas:
                    groups[num].append(num)

               group = dict(groups)

               size_2_count = sum(1 for v in group.values() if len(v) == 2)
               size_1_count = sum(1 for v in group.values() if len(v) == 1)

               if size_2_count == 1 and size_1_count == 1:
                    return idDividido[len(idDividido) - 1] + '_y'

          else:
               return
     else:
          return

d = gv.Digraph()

nodePartida = None

backtrack = []

interseccoes = []

def nextStep(indiceColuna, row, array, indiceLinha):

     global d

     global nodePartida

     global backtrack

     global interseccoes

     elementWithUuid = row[indiceColuna]

     #dividindo o id do elemento a ser processado
     idDividido = dividirID(elementWithUuid)

     #Buscando todas as informacoes do id do espaço a ser processado excluindo o UUID
     element = elementWithUuid[elementWithUuid.find('_') +1:]

     '''Verificando se o elemento a ser processado é um estrada com base na informacao de espessura
     trazida pelo ID que foi dividido'''
     isRoad = idDividido[0] == '0' or idDividido[0] == '00'

     '''Verifica se o elemento a ser processado não é estrada nem espaco vazio representado por -1
     e tambem se ainda nao existe um no inicial representado pelo id de um predio ou armazem'''
     if not isRoad and element != '-1' and nodePartida == None:
          nodePartida = element

     #Verifica se o elemento a ser processado não é estrada nem espaco vazio representado por -1
     elif not isRoad and element != '-1':
          partida = nodePartida
          nodePartida = None
          backtrack = []
          interseccoes = []
          return [partida, element]

     #Verifica se o elemento a ser processado não é espaço vazio representado por -1 e se ja existe um no inicial
     #representado pelo id de um predio ou armazem
     elif element != '-1' and nodePartida != None:

          #Armazena o UUID do espaço a ser processado em um array que representa o caminho que esta sendo feito
          #pelos espacos do tipo estrada
          backtrack.append(idDividido [len(idDividido) - 1])

          #Busca uma interseccao no espaco a ser processado
          crossroad = interseccao(indiceColuna, row, array, indiceLinha)

          #Verifica se ha uma interseccao no esaco a ser processado
          if crossroad != None:

               #Se houver interseccoes, verifica se a ultima interseccao armazenada é diferente da interseccao encontrada
               #no espaco a ser processado e entao a armazena caso seja diferente
               if len(interseccoes) > 0:
                   lastCrossroad = interseccoes[len(interseccoes) - 1]
                   lastCrossroadType = lastCrossroad.split('_')[1]
                   crossroadType = crossroad.split('_')[1]

                   if crossroad not in interseccoes and lastCrossroadType != crossroadType:
                        interseccoes.append(crossroad)

               #Se nao houver interseccoes, armazena a interseccao do espaco a ser processado
               else:
                   if crossroad not in interseccoes:
                        interseccoes.append(crossroad)


          #Buscando os 4 espacos do elemento a ser processado em uma linha ortogonal
          top = getElementTop(indiceColuna, row, array, indiceLinha)
          down = getElementDown(indiceColuna, row, array, indiceLinha)
          left = getElementLeft(row, indiceColuna)
          right = getElementRight(row, indiceColuna)

          topDividido = None
          downDividido = None
          leftDividido = None
          rightDividido = None
          topElement = None
          downElement = None
          leftElement = None
          rightElement = None


          #Se houver um espaco acima do elemento a ser processado
          if top != None:
               #Busca o id dividido deste espaco acima do elemento a ser processado
               topDividido = dividirID(top[0])
               #Buscando todas as informacoes do id do espaço acima do elemento a ser processado excluindo o UUID
               topElement = top[0][top[0].find('_') + 1:]

          if down != None:
               downDividido = dividirID(down [0])
               downElement = down[0][down[0].find('_') + 1:]

          if left != None:
               leftDividido = dividirID(left [0])
               leftElement = left[0][left[0].find('_') + 1:]

          if right != None:
               rightDividido = dividirID(right[0])
               rightElement = right[0][right[0].find('_') + 1:]


          #Verifica se o espaco acima do elemento a ser processado nao e do tipo estrada nem mesmo do tipo espaco vazio
          #alem de tambem verificar se o espaco acima do elemento e diferente do no inicial do qual e um id de predio ou armazem
          if topDividido != None and (topDividido[0] != '0' and topDividido[0] != '00') and topElement != '-1' and topElement != nodePartida:

               #Exibe os nos entre um predio ou armazem e outro
               print('Nova aresta ', nodePartida, topElement)
               #Exibe os nos de interseccao entre um predio ou armazem e outro
               print('Interseccoes ', [x.split('_')[1] for x in interseccoes])
               print('----------')

               #Cria no graphviz os nos entre um predio ou armazem e outro e as arestas entre eles das quais passam por
               #outros nos que sao os nos de interseccao de estradas representados por x ou y
               for crossroad in interseccoes:
                   crossroadType = crossroad.split ('_') [1]
                   d.edge(nodePartida, crossroadType)
                   d.edge(crossroadType, topElement)
               return [nodePartida, topElement]

          elif downDividido != None and (downDividido[0] != '0' and downDividido[0] != '00') and downElement != '-1'and downElement != nodePartida:
               print('Nova aresta ', nodePartida, downElement)
               print('Interseccoes ', [x.split('_')[1] for x in interseccoes])
               print('----------')
               for crossroad in interseccoes:
                   crossroadType = crossroad.split ('_') [1]
                   d.edge(nodePartida, crossroadType)
                   d.edge(crossroadType, downElement)
               return [nodePartida, downElement]

          elif leftDividido != None and (leftDividido[0] != '0' and leftDividido[0] != '00') and leftElement != '-1'and leftElement != nodePartida:
               print('Nova aresta ', nodePartida, leftElement)
               print('Interseccoes ', [x.split('_')[1] for x in interseccoes])
               print('----------')
               for crossroad in interseccoes:
                   crossroadType = crossroad.split ('_') [1]
                   d.edge(nodePartida, crossroadType)
                   d.edge(crossroadType, leftElement)
               return [nodePartida, leftElement]

          elif rightDividido != None and (rightDividido[0] != '0' and rightDividido[0] != '00') and rightElement != '-1'and rightElement != nodePartida:
               print('Nova aresta ', nodePartida, rightElement)
               print('Interseccoes ', [x.split('_')[1] for x in interseccoes])
               print('----------')
               for crossroad in interseccoes:
                   crossroadType = crossroad.split ('_') [1]
                   d.edge(nodePartida, crossroadType)
                   d.edge(crossroadType, rightElement)
               return [nodePartida, rightElement]


          # Verifica se o espaco acima do elemento a ser processado e do tipo estrada alem de tambem verificar se o UUID
          # do espaco acima do elemento nao foi armazenado no array que representa o caminho que esta sendo feito
          # pelos espacos do tipo estrada
          elif topDividido != None and (topDividido [0] == '0' or topDividido[0] == '00') and topDividido[len(topDividido) -1] not in backtrack:

               #Caso a verificacao acima seja verdadeira, chama-se novamento o proprio metodo de nextStep (recursividade),
               #passando assim o indice da coluna do elemento, todos os elementos da linha, toda a matriz, o indice da linha de cima
               #do espaço a ser processado
               resultado = nextStep(indiceColuna, top [1], array, top [2])

               #Se o proximo passo na recursividade acima vier vazio, significa que a estrada chegou ao fim
               #chamando novamente o proprio metodo nextStep, porem agora passando todas as informacoes do espaco de estrada anterior
               #pelo qual estava a ser percorrido, forçando a buscar outro caminho a partir deste espaco anterior
               if resultado == None:
                   return nextStep(indiceColuna, row, array, indiceLinha)

               #Se no proximo passo a recursividade acima trouxer informacoes, significa que todo o caminho ate um segundo no
               #representado pelo id de um predio ou armazem ja foi encontrado, processado e incluido no grafo via graphviz
               else:
                   return resultado

          elif downDividido != None and (downDividido [0] == '0' or downDividido[0] == '00') and downDividido[len(downDividido) -1] not in backtrack:
               resultado = nextStep(indiceColuna, down [1], array, down [2])

               if resultado == None:
                   return nextStep(indiceColuna, row, array, indiceLinha)

               else:
                   return resultado


          elif leftDividido != None and (leftDividido [0] == '0' or leftDividido[0] == '00') and leftDividido[len(leftDividido) -1] not in backtrack:
               resultado = nextStep(left [2], left [1], array, indiceLinha)

               if resultado == None:
                   return nextStep(indiceColuna, row, array, indiceLinha)

               else:
                   return resultado

          elif rightDividido != None and (rightDividido [0] == '0' or rightDividido[0] == '00') and rightDividido[len(rightDividido) -1] not in backtrack:
               resultado = nextStep(right [2], right [1], array, indiceLinha)

               if resultado == None:
                   return nextStep(indiceColuna, row, array, indiceLinha)

               else:
                   return resultado

          else:
              '''fim da linha'''
              return

     else:
          return

if __name__ == '__main__':
    indiceLinha = 0

    for y in x:

        indiceColuna = 0
        for element in y:
            '''if indiceColuna == 3 and indiceLinha == 1:
                 printValores(element, y, x, indiceColuna, indiceLinha)
                 print(interseccao(indiceColuna, y, x, indiceLinha))
                 d = getGrafico()
                 d.render('grafo', format='png', cleanup=True)
                 print(d.source)'''

            nextStep(indiceColuna, y, x, indiceLinha)

            indiceColuna += 1

        indiceLinha += 1

    d.render('grafo', format='png', cleanup=True)
    print(d.source)

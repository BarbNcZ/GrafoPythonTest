import graphviz as gv
import uuid
from collections import defaultdict

#-1 = espaço vazio
#0 = estrada
#a(ID) = armazem
#(ID) = predio

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

     #Search for the index of an element within an array

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

     #Avoid indexOutOfBounds error/exception
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
     #Avoid indexOutOfBounds error/exception
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
     #Avoid indexOutOfBounds error/exception
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
     #Avoid indexOutOfBounds error/exception
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

     #Splitting ID of element to be processed
     idDividido = dividirID(element)

     if idDividido == None:
          return

     #Checking if the element to be processed is a Road based on the thickness information
     #brought by the ID that was split
     isRoad = idDividido [0] == '0' or idDividido[0] == '00'

     #If the above variable is not true, then there are no intersections, returning nothing
     if not isRoad:
          return

     #Searching for the 4 diagonals of the element to be processed
     diagonalTopLeft = getDiagonalTopLeft(indiceColuna, row, array, indiceLinha)
     diagonalTopRight = getDiagonalTopRight(indiceColuna, row, array, indiceLinha)
     diagonalDownLeft = getDiagonalDownLeft(indiceColuna, row, array, indiceLinha)
     diagonalDownRight = getDiagonalDownRight(indiceColuna, row, array, indiceLinha)

     diagonais = [diagonalTopLeft, diagonalTopRight, diagonalDownLeft, diagonalDownRight]

     #Filtering and storing in an array only the diagonals identified as road
     estradas = [x for x in diagonais if dividirID(x) != None and (dividirID(x) [0] == '0' or dividirID(x) [0] == '00')]

     #If the number of identified roads is equal to 2
     if len(estradas) == 2:

          idEstrada1 = None
          idEstrada2 = None

          #Extracting the id/name of the 2 roads
          for estrada in estradas:
              estradaDividida = dividirID(estrada)

              if idEstrada1 == None:
                   idEstrada1 = estradaDividida [1]

              else:
                   idEstrada2 = estradaDividida [1]

          #Checking if the id/name of the 2 roads are the same, thus returning the UUID of the space
          #and the type of intersection (roads of the same thickness) represented by x
          if idEstrada2 != None and idEstrada1 != None and idEstrada2 == idEstrada1:
               return idDividido[len(idDividido) - 1] + '_x'

          else:
               return

     #If the number of identified roads is equal to 3
     elif len(estradas) == 3:
          idEstrada1 = None
          idEstrada2 = None
          idEstrada3 = None


          #Extracting the id/name of the 3 roads
          for estrada in estradas:
               estradaDividida = dividirID(estrada)

               if idEstrada1 == None and idEstrada2 == None:
                    idEstrada1 = estradaDividida[1]

               elif idEstrada2 == None:
                    idEstrada2 = estradaDividida[1]

               else:
                    idEstrada3 = estradaDividida[1]

          #Checking if the id/name of the 2 roads are the same, and the id/name of a road
          #is the same as the element to be processed, thus returning the UUID of the space and the type of intersection
          #(roads of different thicknesses) represented by y
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

     #Splitting the id of the element to be processed
     idDividido = dividirID(elementWithUuid)

     #Fetching all information from the space id to be processed excluding the UUID
     element = elementWithUuid[elementWithUuid.find('_') +1:]

     #Checking if the element to be processed is a road based on the thickness information
     #brought by the ID that was split'''
     isRoad = idDividido[0] == '0' or idDividido[0] == '00'

     #Checks if the element to be processed is not a road or empty space represented by -1
     #and also if there is not already an initial node represented by the id of a building or warehouse'''
     if not isRoad and element != '-1' and nodePartida == None:
          nodePartida = element

     #Checks if the element to be processed is not a road or empty space represented by -1
     elif not isRoad and element != '-1':
          partida = nodePartida
          nodePartida = None
          backtrack = []
          interseccoes = []
          return [partida, element]

     #Checks if the element to be processed is not an empty space represented by -1
     #and if there is already an initial one represented by the id of a building or warehouse
     elif element != '-1' and nodePartida != None:

          #Stores the UUID of the space to be processed in an array that represents the path being taken
          #through the road-type spaces
          backtrack.append(idDividido [len(idDividido) - 1])

          #Searches for an intersection in the space to be processed
          crossroad = interseccao(indiceColuna, row, array, indiceLinha)

          #Checks if there is an intersection in the space to be processed
          if crossroad != None:

               #If there is an intersection, it checks whether the last stored intersection is different from
               #the intersection found in the space to be processed and then stores it if it is different.
               if len(interseccoes) > 0:
                   lastCrossroad = interseccoes[len(interseccoes) - 1]
                   lastCrossroadType = lastCrossroad.split('_')[1]
                   crossroadType = crossroad.split('_')[1]

                   if crossroad not in interseccoes and lastCrossroadType != crossroadType:
                        interseccoes.append(crossroad)

               #If there are no intersections, store the intersection of the space to be processed
               else:
                   if crossroad not in interseccoes:
                        interseccoes.append(crossroad)


          #Searching for the 4 spaces of the element to be processed in an orthogonal line
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


          #If there is a space above the element to be processed
          if top != None:
               #Fetches the split id of this space above the element to be processed
               topDividido = dividirID(top[0])
               #Fetching all id information from the space above the element to be processed excluding the UUID
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


          #Checks if the space above the element to be processed is not of the road type or even of the empty space type,
          #and also checks if the space above the element is different from the initial node of which is a building or warehouse id
          if topDividido != None and (topDividido[0] != '0' and topDividido[0] != '00') and topElement != '-1' and topElement != nodePartida:

               #Displays the nodes between one building or warehouse and another
               print('Nova aresta ', nodePartida, topElement)
               #Exibe os nos de interseccao entre um predio ou armazem e outro
               print('Interseccoes ', [x.split('_')[1] for x in interseccoes])
               print('----------')

               #Creates in graphviz the nodes between one building or warehouse and another and the edges between them
               #that pass through other nodes which are the intersection nodes of roads represented by x or y
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


          #Checks if the space above the element to be processed is of the road type and also checks if the UUID of the space
          #above the element has not been stored in the array that represents the path being taken through the road type spaces

          elif topDividido != None and (topDividido [0] == '0' or topDividido[0] == '00') and topDividido[len(topDividido) -1] not in backtrack:

               #If the above verification is true, the nextStep method itself (recursion) is called again,
               #thus passing the index of the element's column, all the elements of the line, the entire matrix,
               #the index of the line above the space to be processed.
               resultado = nextStep(indiceColuna, top [1], array, top [2])

               #If the next step in the above recursion comes up empty, it means that the road has reached the end,
               #calling the nextStep method again, but now passing all the information from the previous road space
               #through which it was being traveled, forcing it to look for another path from this previous space.
               if resultado == None:
                   return nextStep(indiceColuna, row, array, indiceLinha)

               #If in the next step the above recursion brings information, it means that the entire path up to a second node
               #represented by the id of a building or warehouse has already been found, processed and included in the graph node via graphviz.
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
              #end of the line
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

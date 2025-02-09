A matriz usada no Script foi criada com base no esboço a seguir:

<img alt="sketch.png" height="220" src="sketch.png" width="220"/>

## Def dividirID
O ID de um espaço é composto por um UUID, seguido de espessura/peso da estrada (se for estrada) ou -1 quando for espaço vazio, seguido de um id/nome de estrada ou id de um prédio/armazém, por fim seguido do nome da outra estrada na qual se for uma estrada com cruzamento.
### Exemplos: 
#### _Espaço vazio:_
`550e8400-e29b-41d4-a716-446655440000_-1`

#### _Estrada com 1 de espessura:_
`550e8400-e29b-41d4-a716-446655440000_0_4`

#### _Estrada com 2 de espessura:_
`550e8400-e29b-41d4-a716-446655440000_00_4`

#### _Estrada com cruzamento 1 de espessura:_
`550e8400-e29b-41d4-a716-446655440000_0_4_2`

#### _Estrada com cruzamento 2 de espessura:_
`550e8400-e29b-41d4-a716-446655440000_00_4_2`

#### _Prédio:_
`550e8400-e29b-41d4-a716-446655440000_5`

#### _Armazém:_
`550e8400-e29b-41d4-a716-446655440000_a3`

Nota-se que o ID de um espaço contém todas essas informações separadas por “_”, sendo assim esta função apenas divide cada uma destas informações e as armazena individualmente em um array, retornando este array.

## Def Interseccao
Esta função verifica os 4 possíveis espaços na diagonal de um elemento do tipo estrada a ser processado. Caso haja 2 diagonais do tipo estrada com o mesmo id/nome, a função retorna uma intersecção do tipo mudança de espessura de estrada. Caso haja 3 diagonais do tipo estrada sendo 2 com o mesmo id/nome e 1 tendo o mesmo id/nome do elemento processado, então a função retorna uma intersecção do tipo mesmas espessuras. Do contrário, ela não retorna nada.


## Def nextStep
Considerando que o processamento inicial de script fará uma varredura por cada elemento de uma matriz, sendo este elemento considerado um espaço. Esta é uma função recursiva, da qual inicialmente identifica o primeiro espaço do tipo prédio ou armazém e então, a partir daí, busca o próximo espaço em uma linha ortogonal que seja do tipo estrada a partir daí a função entra em recursividade, chamando a ela mesma, buscando sempre o próximo espaço do tipo estrada em uma linha ortogonal até encontrar em algum momento dentro desta linha um prédio ou armazém. Durante a recursividade, entre o primeiro espaço do tipo prédio ou armazém e o último, é guardada as intersecções de estradas. Sendo assim, ao fim da recursividade, retorna-se então como nós do grafo o prédio ou armazém identificado inicialmente, as intersecções e o prédio ou armazém identificado no final.

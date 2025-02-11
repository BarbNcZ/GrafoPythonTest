# coding=utf-8
import graphviz as gv
import uuid
from collections import defaultdict

# Subtitle:

# -1 = Empty space
# 0 = Road
# a(ID) = Warehouse
# (ID) = Building

graphFilename = "graph"
graphFileExtension = "png"

inputMatrix = [
	[str(uuid.uuid4()) + "_-1",		str(uuid.uuid4()) + "_0_1",		str(uuid.uuid4()) + "_-1",		str(uuid.uuid4()) + "_0_2",		str(uuid.uuid4()) + "_-1",		str(uuid.uuid4()) + "_-1",		str(uuid.uuid4()) + "_00_3",	str(uuid.uuid4()) + "_00_3",	str(uuid.uuid4()) + "_-1",		str(uuid.uuid4()) + "_-1"],
	[str(uuid.uuid4()) + "_5",    	str(uuid.uuid4()) + "_0_1",   	str(uuid.uuid4()) + "_-1",    	str(uuid.uuid4()) + "_0_2",   	str(uuid.uuid4()) + "_a3",    	str(uuid.uuid4()) + "_8",     	str(uuid.uuid4()) + "_00_3",  	str(uuid.uuid4()) + "_00_3",  	str(uuid.uuid4()) + "_a2",    	str(uuid.uuid4()) + "_a2" ],
	[str(uuid.uuid4()) + "_-1",    	str(uuid.uuid4()) + "_0_4_1", 	str(uuid.uuid4()) + "_-1",    	str(uuid.uuid4()) + "_0_4_2", 	str(uuid.uuid4()) + "_a3",    	str(uuid.uuid4()) + "_8",     	str(uuid.uuid4()) + "_00_3_4",	str(uuid.uuid4()) + "_00_3_4",	str(uuid.uuid4()) + "_-1",    	str(uuid.uuid4()) + "_-1" ],
	[str(uuid.uuid4()) + "_00_4",  	str(uuid.uuid4()) + "_00_4_1",	str(uuid.uuid4()) + "_00_4",  	str(uuid.uuid4()) + "_00_4_2",	str(uuid.uuid4()) + "_00_4",  	str(uuid.uuid4()) + "_00_4",  	str(uuid.uuid4()) + "_00_4_3",	str(uuid.uuid4()) + "_00_4_3",	str(uuid.uuid4()) + "_00_4",  	str(uuid.uuid4()) + "_00_4" ],
	[str(uuid.uuid4()) + "_00_4",  	str(uuid.uuid4()) + "_00_4_1",	str(uuid.uuid4()) + "_00_4",  	str(uuid.uuid4()) + "_00_4_2",	str(uuid.uuid4()) + "_00_4_2",	str(uuid.uuid4()) + "_00_4",  	str(uuid.uuid4()) + "_00_4_3",	str(uuid.uuid4()) + "_00_4_3",	str(uuid.uuid4()) + "_00_4",  	str(uuid.uuid4()) + "_00_4" ],
	[str(uuid.uuid4()) + "_-1",    	str(uuid.uuid4()) + "_0_4_1", 	str(uuid.uuid4()) + "_9",     	str(uuid.uuid4()) + "_00_2_4",	str(uuid.uuid4()) + "_00_2_4",	str(uuid.uuid4()) + "_-1",    	str(uuid.uuid4()) + "_00_3_4",	str(uuid.uuid4()) + "_00_3_4",	str(uuid.uuid4()) + "_6",     	str(uuid.uuid4()) + "_6" ],
	[str(uuid.uuid4()) + "_-1",    	str(uuid.uuid4()) + "_0_1",   	str(uuid.uuid4()) + "_9",     	str(uuid.uuid4()) + "_00_2",  	str(uuid.uuid4()) + "_00_2",  	str(uuid.uuid4()) + "_7",     	str(uuid.uuid4()) + "_00_3_5",	str(uuid.uuid4()) + "_00_3_5",	str(uuid.uuid4()) + "_0_3_5", 	str(uuid.uuid4()) + "_0_5" ],
	[str(uuid.uuid4()) + "_-1",    	str(uuid.uuid4()) + "_0_1",   	str(uuid.uuid4()) + "_9",     	str(uuid.uuid4()) + "_00_2",  	str(uuid.uuid4()) + "_00_2",  	str(uuid.uuid4()) + "_-1",    	str(uuid.uuid4()) + "_00_3",  	str(uuid.uuid4()) + "_00_3",  	str(uuid.uuid4()) + "_-1",    	str(uuid.uuid4()) + "_-1" ],
	[str(uuid.uuid4()) + "_0_6",   	str(uuid.uuid4()) + "_0_1_6", 	str(uuid.uuid4()) + "_0_6",   	str(uuid.uuid4()) + "_00_2_6",	str(uuid.uuid4()) + "_00_2_6",	str(uuid.uuid4()) + "_0_6",   	str(uuid.uuid4()) + "_00_3_6",	str(uuid.uuid4()) + "_00_3_6",	str(uuid.uuid4()) + "_-1",    	str(uuid.uuid4()) + "_-1" ],
	[str(uuid.uuid4()) + "_a1",    	str(uuid.uuid4()) + "_a1",    	str(uuid.uuid4()) + "_a1",    	str(uuid.uuid4()) + "_-1",    	str(uuid.uuid4()) + "_10",    	str(uuid.uuid4()) + "_10",    	str(uuid.uuid4()) + "_00_3",  	str(uuid.uuid4()) + "_00_3",  	str(uuid.uuid4()) + "_a4",    	str(uuid.uuid4()) + "_a4"]
]


def divideId(id):

	if id is None:
		return

	dividedId = id.split('_')

	if len(dividedId) == 2:
		return [dividedId[1]]

	_uuid = dividedId[0]
	thickness = dividedId[1]
	wideRoadId = dividedId[2]
	if len(dividedId) > 3:
		narrowRoadId = dividedId[3]

	else:
		narrowRoadId = None

	return [thickness, wideRoadId, narrowRoadId, _uuid]


def showElementData(element, row, input, columnIndex, rowIndex):
	print('Element: ', element)
	print('----------')
	print('Right: ', getElementRight(row, columnIndex)[0])
	print('Left: ', getElementLeft(row, columnIndex)[0])
	print('Top: ', getElementTop(columnIndex, row, input, rowIndex)[0])
	print('Down: ', getElementDown(columnIndex, row, input, rowIndex)[0])
	print('Top Diagonal Left: ', getDiagonalTopLeft(columnIndex, row, input, rowIndex))
	print('Top Diagonal Right: ', getDiagonalTopRight(columnIndex, row, input, rowIndex))
	print('Down Diagonal Left: ', getDiagonalDownLeft(columnIndex, row, input, rowIndex))
	print('Down Diagonal Right: ', getDiagonalDownRight(columnIndex, row, input, rowIndex))


def getElementRight(row, columnIndex):
	if len(row) == 0:
		return

	# Search for the index of an element within an array
	if 0 <= columnIndex < len(row) - 1:
		return [row[columnIndex + 1], row, columnIndex + 1]
	else:
		return


def getElementLeft(row, columnIndex):
	if len(row) == 0:
		return

	if columnIndex > 0:
		return [row[columnIndex - 1], row, columnIndex - 1]
	else:
		return


def getElementTop(columnIndex, row, input, rowIndex):
	# Avoid indexOutOfBounds error/exception
	if input is None or len(input) == 0:
		return
	if len(row) == 0:
		return

	if rowIndex <= 0:
		return
	else:
		topRow = input[rowIndex - 1]

	if 0 <= columnIndex <= len(topRow) - 1:
		return [topRow[columnIndex], topRow, rowIndex - 1]
	else:
		return


def getElementDown(columnIndex, row, input, rowIndex):
	# Avoid indexOutOfBounds error/exception
	if input is None or len(input) == 0:
		return
	if len(row) == 0:
		return

	if rowIndex >= len(row) - 1:
		return
	else:
		downRow = input[rowIndex + 1]

	if 0 <= columnIndex <= len(downRow) - 1:
		return [downRow[columnIndex], downRow, rowIndex + 1]
	else:
		return


def getDiagonalTopLeft(columnIndex, row, input, rowIndex):

	if input is None or len(input) == 0:
		return
	if len(row) == 0:
		return

	if rowIndex <= 0:
		return
	else:
		topRow = input[rowIndex - 1]

	if 0 <= columnIndex <= len(topRow) - 1:
		elementLeft = getElementLeft(topRow, columnIndex)
		if elementLeft is None:
			return
		else:
			return elementLeft[0]

	else:
		return


def getDiagonalTopRight(columnIndex, row, input, rowIndex):

	if input is None or len(input) == 0:
		return
	if len(row) == 0:
		return

	if rowIndex <= 0:
		return
	else:
		topRow = input[rowIndex - 1]

	if 0 <= columnIndex <= len(topRow) - 1:
		elementRight = getElementRight(topRow, columnIndex)
		if elementRight is None:
			return
		else:
			return elementRight[0]

	else:
		return


def getDiagonalDownLeft(columnIndex, row, input, rowIndex):
	# Avoid indexOutOfBounds error/exception
	if input is None or len(input) == 0:
		return
	if len(row) == 0:
		return

	if rowIndex >= len(row) - 1:
		return
	else:
		downRow = input[rowIndex + 1]

	if 0 <= columnIndex <= len(downRow) - 1:
		elementLeft = getElementLeft(downRow, columnIndex)
		if elementLeft is None:
			return
		else:
			return elementLeft[0]
	else:
		return


def getDiagonalDownRight(columnIndex, row, input, rowIndex):
	# Avoid indexOutOfBounds error/exception
	if input is None or len(input) == 0:
		return
	if len(row) == 0:
		return

	if rowIndex >= len(row) - 1:
		return
	else:
		downRow = input[rowIndex + 1]

	if 0 <= columnIndex <= len(downRow) - 1:
		elementRight = getElementRight(downRow, columnIndex)
		if elementRight is None:
			return
		else:
			return elementRight[0]
	else:
		return


def isCrossroad(columnIndex, row, input, rowIndex):

	element = row[columnIndex]

	# Splitting ID of element to be processed
	dividedId = divideId(element)

	if dividedId is None:
		return

	# Checking if the element to be processed is a Road based on the thickness information
	# brought by the ID that was split
	isRoad = dividedId[0] == '0' or dividedId[0] == '00'

	# If the above variable is not true, then there are no intersections, returning nothing
	if not isRoad:
		return

	# Searching for the 4 diagonals of the element to be processed
	diagonalTopLeft = getDiagonalTopLeft(columnIndex, row, input, rowIndex)
	diagonalTopRight = getDiagonalTopRight(columnIndex, row, input, rowIndex)
	diagonalDownLeft = getDiagonalDownLeft(columnIndex, row, input, rowIndex)
	diagonalDownRight = getDiagonalDownRight(columnIndex, row, input, rowIndex)

	diagonals = [diagonalTopLeft, diagonalTopRight, diagonalDownLeft, diagonalDownRight]

	# Filtering and storing in an array only the diagonals identified as road
	roads = [x for x in diagonals if divideId(x) is not None and (divideId(x)[0] == '0' or divideId(x)[0] == '00')]

	# If the number of identified roads is equal to 2
	if len(roads) == 2:

		road1Id = None
		road2Id = None

		# Extracting the id/name of the 2 roads
		for estrada in roads:
			dividedRoadId = divideId(estrada)
	
			if road1Id is None:
				road1Id = dividedRoadId[1]
	
			else:
				road2Id = dividedRoadId[1]

		# Checking if the id/name of the 2 roads are the same, thus returning the UUID of the space
		# and the type of intersection (roads of the same thickness) represented by x
		if road2Id is not None and road1Id is not None and road2Id == road1Id:
			return dividedId[len(dividedId) - 1] + '_x'

		else:
			return

	# If the number of identified roads is equal to 3
	elif len(roads) == 3:
		road1Id = None
		road2Id = None
		road3Id = None
	
	
		# Extracting the id/name of the 3 roads
		for estrada in roads:
			dividedRoadId = divideId(estrada)
	
			if road1Id is None and road2Id is None:
				road1Id = dividedRoadId[1]
	
			elif road2Id is None:
				road2Id = dividedRoadId[1]
	
			else:
				road3Id = dividedRoadId[1]
	
		# Checking if the id/name of the 2 roads are the same, and the id/name of a road
		# is the same as the element to be processed, thus returning the UUID of the space and the type of intersection
		#(roads of different thicknesses) represented by y
		if road2Id is not None and road1Id is not None and road3Id is not None:
			roadIds = [road1Id, road2Id, road3Id]
	
			roadIdsGroups = defaultdict(list)
	
			for num in roadIds:
				roadIdsGroups[num].append(num)
	
			group = dict(roadIdsGroups)
	
			size2Count = sum(1 for v in group.values() if len(v) == 2)
			size1Count = sum(1 for v in group.values() if len(v) == 1)
	
			if size2Count == 1 and size1Count == 1:
				return dividedId[len(dividedId) - 1] + '_y'
	
		else:
			return
	else:
		return


# Create Digraph
d = gv.Digraph()
# Initialize startup node of an edge (from road way)
startupNode = None
# Initialize array of backtrack of the road way
backtrack = []
# Initialize array of crossroads on the road way
crossroads = []


def nextStepOnTheRoad(columnIndex, row, input, rowIndex):

	global d

	global startupNode

	global backtrack

	global crossroads

	elementWithUuid = row[columnIndex]

	# Splitting the id of the element to be processed
	dividedId = divideId(elementWithUuid)

	# Fetching all information from the space id to be processed excluding the UUID
	element = elementWithUuid[elementWithUuid.find('_') +1:]

	# Checking if the element to be processed is a road based on the thickness information
	# brought by the ID that was split'''
	isRoad = dividedId[0] == '0' or dividedId[0] == '00'

	# Checks if the element to be processed is not a road or empty space represented by -1
	# and also if there is not already an initial node represented by the id of a building or warehouse'''
	if not isRoad and element != '-1' and startupNode is None:
		startupNode = element

	# Checks if the element to be processed is not a road or empty space represented by -1
	elif not isRoad and element != '-1':
		startup = startupNode
		startupNode = None
		backtrack = []
		crossroads = []
		return [startup, element]

	# Checks if the element to be processed is not an empty space represented by -1
	# and if there is already an initial one represented by the id of a building or warehouse
	elif element != '-1' and startupNode is not None:

		# Stores the UUID of the space to be processed in an array that represents the path being taken
		# through the road-type spaces
		backtrack.append(dividedId[len(dividedId) - 1])

		# Searches for an intersection in the space to be processed
		crossroad = isCrossroad(columnIndex, row, input, rowIndex)

		# Checks if there is an intersection in the space to be processed
		if crossroad is not None:

			# If there is an intersection, it checks whether the last stored intersection is different from
			# the intersection found in the space to be processed and then stores it if it is different.
			if len(crossroads) > 0:
				lastCrossroad = crossroads[len(crossroads) - 1]
				lastCrossroadType = lastCrossroad.split('_')[1]
				crossroadType = crossroad.split('_')[1]

				if crossroad not in crossroads and lastCrossroadType != crossroadType:
					crossroads.append(crossroad)

			# If there are no intersections, store the intersection of the space to be processed
			else:
				if crossroad not in crossroads:
					crossroads.append(crossroad)


		# Searching for the 4 spaces of the element to be processed in an orthogonal line
		top = getElementTop(columnIndex, row, input, rowIndex)
		down = getElementDown(columnIndex, row, input, rowIndex)
		left = getElementLeft(row, columnIndex)
		right = getElementRight(row, columnIndex)

		dividedTopId = None
		dividedDownId = None
		dividedLeftId = None
		dividedRightId = None
		topElement = None
		downElement = None
		leftElement = None
		rightElement = None


		# If there is a space above the element to be processed
		if top is not None:
			# Fetches the split id of this space above the element to be processed
			dividedTopId = divideId(top[0])
			# Fetching all id information from the space above the element to be processed excluding the UUID
			topElement = top[0][top[0].find('_') + 1:]

		if down is not None:
			dividedDownId = divideId(down[0])
			downElement = down[0][down[0].find('_') + 1:]

		if left is not None:
			dividedLeftId = divideId(left[0])
			leftElement = left[0][left[0].find('_') + 1:]

		if right is not None:
			dividedRightId = divideId(right[0])
			rightElement = right[0][right[0].find('_') + 1:]


		# Checks if the space above the element to be processed is not of the road type or even of the empty space type,
		# and also checks if the space above the element is different from the initial node of which is a building or warehouse id
		if dividedTopId is not None and (dividedTopId[0] != '0' and dividedTopId[0] != '00') and topElement != '-1' and topElement != startupNode:

			# Displays the nodes between one building or warehouse and another
			print('New edge: ', startupNode, topElement)
			# Displays the crossroad nodes beteween one building or warehouse and another
			print('Crossroads: ', [x.split('_')[1] for x in crossroads])
			print('----------')

			# Creates in graphviz the nodes between one building or warehouse and another and the edges between them
			# that pass through other nodes which are the intersection nodes of roads represented by x or y
			for crossroad in crossroads:
				crossroadType = crossroad.split('_')[1]
				d.edge(startupNode, crossroadType)
				d.edge(crossroadType, topElement)
			return [startupNode, topElement]

		elif dividedDownId is not None and (dividedDownId[0] != '0' and dividedDownId[0] != '00') and downElement != '-1'and downElement != startupNode:
			print('New edge: ', startupNode, downElement)
			print('Crossroads: ', [x.split('_')[1] for x in crossroads])
			print('----------')
			for crossroad in crossroads:
				crossroadType = crossroad.split ('_')[1]
				d.edge(startupNode, crossroadType)
				d.edge(crossroadType, downElement)
			return [startupNode, downElement]

		elif dividedLeftId is not None and (dividedLeftId[0] != '0' and dividedLeftId[0] != '00') and leftElement != '-1'and leftElement != startupNode:
			print('New edge: ', startupNode, leftElement)
			print('Crossroads: ', [x.split('_')[1] for x in crossroads])
			print('----------')
			for crossroad in crossroads:
				crossroadType = crossroad.split ('_')[1]
				d.edge(startupNode, crossroadType)
				d.edge(crossroadType, leftElement)
			return [startupNode, leftElement]

		elif dividedRightId is not None and (dividedRightId[0] != '0' and dividedRightId[0] != '00') and rightElement != '-1'and rightElement != startupNode:
			print('New edge: ', startupNode, rightElement)
			print('Crossroads: ', [x.split('_')[1] for x in crossroads])
			print('----------')
			for crossroad in crossroads:
				crossroadType = crossroad.split ('_')[1]
				d.edge(startupNode, crossroadType)
				d.edge(crossroadType, rightElement)
			return [startupNode, rightElement]


		# Checks if the space above the element to be processed is of the road type and also checks if the UUID of the space
		# above the element has not been stored in the array that represents the path being taken through the road type spaces

		elif dividedTopId is not None and (dividedTopId[0] == '0' or dividedTopId[0] == '00') and dividedTopId[len(dividedTopId) - 1] not in backtrack:

			# If the above verification is true, the nextStep method itself (recursion) is called again,
			# thus passing the index of the element's column, all the elements of the line, the entire matrix,
			# the index of the line above the space to be processed.
			nextStepResult = nextStepOnTheRoad(columnIndex, top[1], input, top[2])

			# If the next step in the above recursion comes up empty, it means that the road has reached the end,
			# calling the nextStep method again, but now passing all the information from the previous road space
			# through which it was being traveled, forcing it to look for another path from this previous space.
			if nextStepResult is None:
				return nextStepOnTheRoad(columnIndex, row, input, rowIndex)

			# If in the next step the above recursion brings information, it means that the entire path up to a second node
			# represented by the id of a building or warehouse has already been found, processed and included in the graph node via graphviz.
			else:
				return nextStepResult

		elif dividedDownId is not None and (dividedDownId[0] == '0' or dividedDownId[0] == '00') and dividedDownId[len(dividedDownId) - 1] not in backtrack:
			nextStepResult = nextStepOnTheRoad(columnIndex, down[1], input, down[2])

			if nextStepResult is None:
				return nextStepOnTheRoad(columnIndex, row, input, rowIndex)

			else:
				return nextStepResult


		elif dividedLeftId is not None and (dividedLeftId[0] == '0' or dividedLeftId[0] == '00') and dividedLeftId[len(dividedLeftId) -1] not in backtrack:
			nextStepResult = nextStepOnTheRoad(left[2], left[1], input, rowIndex)

			if nextStepResult is None:
				return nextStepOnTheRoad(columnIndex, row, input, rowIndex)

			else:
				return nextStepResult

		elif dividedRightId is not None and (dividedRightId[0] == '0' or dividedRightId[0] == '00') and dividedRightId[len(dividedRightId) -1] not in backtrack:
			nextStepResult = nextStepOnTheRoad(right[2], right[1], input, rowIndex)

			if nextStepResult is None:
				return nextStepOnTheRoad(columnIndex, row, input, rowIndex)

			else:
				return nextStepResult

		else:
			# End of the line
			return

	else:
		return


if __name__ == '__main__':
	rowIndex = 0

	for row in inputMatrix:

		columnIndex = 0

		for element in row:
			"""
			if columnIndex == 3 and rowIndex == 1:
				showElementData(element, row, inputMatrix, columnIndex, rowIndex)
				print(isCrossroad(columnIndex, row, inputMatrix, rowIndex))
			"""

			nextStepOnTheRoad(columnIndex, row, inputMatrix, rowIndex)

			columnIndex += 1

		rowIndex += 1

	d.render(graphFilename, format=graphFileExtension, cleanup=True)
	print(d.source)

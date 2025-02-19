# coding=utf-8
import graphviz as gv
import uuid
from collections import defaultdict

# Subtitle:

# -1 = Empty space
# 0 = Road
# a(ID) = Warehouse
# (ID) = Building

# SETTABLE
graphFilename = "graph"
graphFileExtension = "png"
crossroadsLimiter = 5

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


# NOT-SETTABLE (DO NOT TOUCH !!)

# Create Digraph
d = gv.Digraph()
# Initialize startup node of an edge (from road way)
startupNode = None
# Initialize array of backtrack of the road way
backtrack = []
# Initialize array of crossroads on the road way
crossroads = []

graphEdgesData = []

# Constants
EMPTY_SPACE_ID = "-1"
NARROW_ROAD_ID = "0"
WIDE_ROAD_ID = "00"


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


def getStartupNodeAndLastNodeFrom(fullElement):
	global startupNode
	global EMPTY_SPACE_ID
	global NARROW_ROAD_ID
	global WIDE_ROAD_ID

	dividedIdAndElement = getDividedIdAndElement(fullElement)

	if dividedIdAndElement is None:
		return

	dividedId = dividedIdAndElement[0]
	element = dividedIdAndElement[1]

	isRoad = dividedId[0] == NARROW_ROAD_ID or dividedId[0] == WIDE_ROAD_ID

	isEmptySpace = element == EMPTY_SPACE_ID

	isTheSameAsStartupNode = element == startupNode

	if dividedId is not None and\
		not isRoad and\
		not isEmptySpace and\
		not isTheSameAsStartupNode:

		return [startupNode, element]
	else:
		return


def lookAroundForLastBuildingOrWarehouse(top, down, left, right):
	global d
	global crossroads
	global graphEdgesData
	global crossroadsLimiter

	# Checks if the space above, bellow, on the left or the right of the element to be processed is
	# not of the road type or even of the empty space type, and also checks if the space above,
	# bellow, on the left or the right of the element is different from the initial node of which
	# is a building or warehouse id
	startupNodeAndLastNodeFromAbove = getStartupNodeAndLastNodeFrom(top)
	startupNodeAndLastNodeFromBellow = getStartupNodeAndLastNodeFrom(down)
	startupNodeAndLastNodeFromTheLeft = getStartupNodeAndLastNodeFrom(left)
	startupNodeAndLastNodeFromTheRight = getStartupNodeAndLastNodeFrom(right)

	if startupNodeAndLastNodeFromAbove is not None:
		startupNodeFromAbove = startupNodeAndLastNodeFromAbove[0]
		lastNodeFromAbove = startupNodeAndLastNodeFromAbove[1]

		copyOfCrossroads = crossroads.copy()
		if len(copyOfCrossroads) <= crossroadsLimiter:
			canAppend = True

			for data in graphEdgesData:
				if data[0] == startupNodeFromAbove and areEqual(data[1], copyOfCrossroads) and data[2] == lastNodeFromAbove:
					canAppend = False
					break

			if canAppend:
				graphEdgesData.append([startupNodeFromAbove, copyOfCrossroads, lastNodeFromAbove])

		return startupNodeAndLastNodeFromAbove

	elif startupNodeAndLastNodeFromBellow is not None:
		startupNodeFromBellow = startupNodeAndLastNodeFromBellow[0]
		lastNodeFromBellow = startupNodeAndLastNodeFromBellow[1]

		copyOfCrossroads = crossroads.copy()
		if len(copyOfCrossroads) <= crossroadsLimiter:
			canAppend = True

			for data in graphEdgesData:
				if data[0] == startupNodeFromBellow and areEqual(data[1], copyOfCrossroads) and data[2] == lastNodeFromBellow:
					canAppend = False
					break

			if canAppend:
				graphEdgesData.append([startupNodeFromBellow, copyOfCrossroads, lastNodeFromBellow])

		return startupNodeAndLastNodeFromBellow

	elif startupNodeAndLastNodeFromTheLeft is not None:
		startupNodeFromTheLeft = startupNodeAndLastNodeFromTheLeft[0]
		lastNodeFromTheLeft = startupNodeAndLastNodeFromTheLeft[1]

		copyOfCrossroads = crossroads.copy()
		if len(copyOfCrossroads) <= crossroadsLimiter:
			canAppend = True

			for data in graphEdgesData:
				if data[0] == startupNodeFromTheLeft and areEqual(data[1], copyOfCrossroads) and data[2] == lastNodeFromTheLeft:
					canAppend = False
					break

			if canAppend:
				graphEdgesData.append([startupNodeFromTheLeft, copyOfCrossroads, lastNodeFromTheLeft])

		return startupNodeAndLastNodeFromTheLeft

	elif startupNodeAndLastNodeFromTheRight is not None:
		startupNodeFromTheRight = startupNodeAndLastNodeFromTheRight[0]
		lastNodeFromTheRight = startupNodeAndLastNodeFromTheRight[1]

		copyOfCrossroads = crossroads.copy()
		if len(copyOfCrossroads) <= crossroadsLimiter:
			canAppend = True

			for data in graphEdgesData:
				if data[0] == startupNodeFromTheRight and areEqual(data[1], copyOfCrossroads) and data[2] == lastNodeFromTheRight:
					canAppend = False
					break

			if canAppend:
				graphEdgesData.append([startupNodeFromTheRight, copyOfCrossroads, lastNodeFromTheRight])

		return startupNodeAndLastNodeFromTheRight

	else:
		return


def getNextStepResultVertically(fullElement, columnIndex, row, input, rowIndex):
	global backtrack
	global NARROW_ROAD_ID
	global WIDE_ROAD_ID

	dividedIdAndElement = getDividedIdAndElement(fullElement)

	if dividedIdAndElement is None:
		return

	dividedId = dividedIdAndElement[0]

	isRoad = dividedId[0] == NARROW_ROAD_ID or dividedId[0] == WIDE_ROAD_ID

	hasPassed = dividedId[len(dividedId) - 1] in backtrack

	# Checks if the space above or bellow the element to be processed is of the road type and also checks if the UUID of the space
	# above or bellow the element has not been stored in the array that represents the path being taken through the road type spaces
	if dividedId is not None and \
		isRoad and \
		not hasPassed:

		# If the above or bellow element verification is true, the nextStepOnTheRoad method is called again (recursion),
		# thus passing the index of the element's column, all the elements of the line, the entire matrix,
		# the index of the line above the space to be processed.
		nextStepResult = nextStepOnTheRoad(columnIndex, fullElement[1], input, fullElement[2])

		# If the next step in the above or bellow recursion comes up empty, it means that the road has reached the end,
		# calling the nextStepOnTheRoad method again, but now passing all the information from the previous road space
		# through which it was being traveled, forcing it to look for another path from this previous space.
		if nextStepResult is None:
			return nextStepOnTheRoad(columnIndex, row, input, rowIndex)

		# If in the next step on the road the above or bellow recursion brings information, it means that the entire path up to a second node
		# represented by the id of a building or warehouse has already been found, processed and included in the graph node via graphviz.
		else:
			return nextStepResult
	else:
		return


def getNextStepResultHorizontally(fullElement, columnIndex, row, input, rowIndex):
	global backtrack
	global NARROW_ROAD_ID
	global WIDE_ROAD_ID

	dividedIdAndElement = getDividedIdAndElement(fullElement)
	if dividedIdAndElement is None:
		return

	dividedId = dividedIdAndElement[0]

	isRoad = dividedId[0] == NARROW_ROAD_ID or dividedId[0] == WIDE_ROAD_ID

	hasPassed = dividedId[len(dividedId) - 1] in backtrack

	if dividedId is not None and \
		isRoad and \
		not hasPassed:

		nextStepResult = nextStepOnTheRoad(fullElement[2], fullElement[1], input, rowIndex)

		if nextStepResult is None:
			return nextStepOnTheRoad(columnIndex, row, input, rowIndex)

		else:
			return nextStepResult
	else:
		return


def lookAroundWhereToStep(top, down, left, right, columnIndex, row, input, rowIndex):
	global backtrack

	nextStepResultFromAbove = getNextStepResultVertically(top, columnIndex, row, input, rowIndex)
	nextStepResultFromBellow = getNextStepResultVertically(down, columnIndex, row, input, rowIndex)
	nextStepResultFromTheLeft = getNextStepResultHorizontally(left, columnIndex, row, input, rowIndex)
	nextStepResultFromTheRight = getNextStepResultHorizontally(right, columnIndex, row, input, rowIndex)

	if nextStepResultFromAbove is not None:
		return nextStepResultFromAbove

	elif nextStepResultFromBellow is not None:
		return nextStepResultFromBellow

	elif nextStepResultFromTheLeft is not None:
		return nextStepResultFromTheLeft

	elif nextStepResultFromTheRight is not None:
		return nextStepResultFromTheRight

	else:
		return


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
	global NARROW_ROAD_ID
	global WIDE_ROAD_ID

	element = row[columnIndex]

	# Splitting ID of element to be processed
	dividedId = divideId(element)

	if dividedId is None:
		return

	# Checking if the element to be processed is a Road based on the thickness information
	# brought by the ID that was split
	isRoad = dividedId[0] == NARROW_ROAD_ID or dividedId[0] == WIDE_ROAD_ID

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
	roads = [x for x in diagonals if divideId(x) is not None and (divideId(x)[0] == NARROW_ROAD_ID or divideId(x)[0] == WIDE_ROAD_ID)]

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
		# (roads of different thicknesses) represented by y
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


def getDividedIdAndElement(fullElement):
	# If there is a space above, bellow, on the left or on the right of the element to be processed
	if fullElement is None:
		return

	# Fetches the split id of this space above, bellow, on the left or on the right of he element to be processed
	dividedId = divideId(fullElement[0])

	# Fetching all id information from the space above, bellow, on the left or on the right of the
	# element to be processed excluding the UUID
	element = fullElement[0][fullElement[0].find('_') + 1:]

	return [dividedId, element]


def nextStepOnTheRoad(columnIndex, row, input, rowIndex):
	global startupNode
	global backtrack
	global crossroads
	global EMPTY_SPACE_ID
	global NARROW_ROAD_ID
	global WIDE_ROAD_ID

	elementWithUuid = row[columnIndex]

	# Splitting the id of the element to be processed
	dividedId = divideId(elementWithUuid)

	# Fetching all information from the space id to be processed excluding the UUID
	element = elementWithUuid[elementWithUuid.find('_') +1:]

	# Checking if the element to be processed is a road based on the thickness information
	# brought by the ID that was split'''
	isRoad = dividedId[0] == NARROW_ROAD_ID or dividedId[0] == WIDE_ROAD_ID

	# Checks if the element to be processed is not a road or empty space represented by -1
	# and also if there is not already an initial node represented by the id of a building or warehouse'''
	if not isRoad and element != EMPTY_SPACE_ID and startupNode is None:
		startupNode = element

	# Checks if the element to be processed is not a road or empty space represented by -1
	elif not isRoad and element != EMPTY_SPACE_ID:
		startup = startupNode
		startupNode = None
		backtrack = []
		crossroads = []
		return [startup, element]

	# Checks if the element to be processed is not an empty space represented by -1
	# and if there is already an initial one represented by the id of a building or warehouse
	elif element != EMPTY_SPACE_ID and startupNode is not None:

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

		lastBuildingOrWarehouse = lookAroundForLastBuildingOrWarehouse(top, down, left, right)
		if lastBuildingOrWarehouse is not None:
			return lastBuildingOrWarehouse

		nextStepResult = lookAroundWhereToStep(top, down, left, right, columnIndex, row, input, rowIndex)
		if nextStepResult is not None:
			return nextStepResult

		else:
			return

	else:
		return


def areEqual(array1, array2):
	if len(array1) != len(array2):
		return False

	result = True
	i = 0
	for item in array1:
		if item != array2[i]:
			result = False
			break
		i += 1

	return result


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

	for data in graphEdgesData:
		graphStartupNode = data[0]
		graphCrossroads = data[1]
		graphLastNode = data[2]

		# Displays the nodes between one building or warehouse and another
		print('New edge: ', graphStartupNode, graphLastNode)
		# Displays the crossroad nodes between one building or warehouse and another
		print('Crossroads: ', [x.split('_')[1] for x in graphCrossroads])
		print('----------')

		# Creates in graphviz the nodes between one building or warehouse and another and the edges between them
		# that pass through other nodes which are the intersection nodes of roads represented by x or y
		i = 0
		for graphCrossroad in graphCrossroads:
			crossroadType = graphCrossroad.split('_')[1]
			d.edge(graphStartupNode, crossroadType + str(i))
			d.edge(crossroadType + str(i), graphLastNode)
			i += 1

	d.render(graphFilename, format=graphFileExtension, cleanup=True)
	print(d.source)

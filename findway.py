global maze,sol

maze = [[ 0 for col in range(4)] for row in range(4) ]
sol = [[0,0,0,0],
	   [0,0,0,0],
	   [0,0,0,0],
	   [0,0,0,0]]

class Unit(object):
	def __init__(self,x,y):
		self.x = x
		self.y = y
		self.statu = 1

def GenerateMaze():
	for i in range(4):
		for j in range(4):
			maze[i][j] = Unit(i,j)

	maze[0][1].statu=maze[0][2].statu=maze[0][3].statu=maze[1][2].statu=maze[2][0].statu=maze[2][2].statu=maze[2][3].statu=0

def InMaze(point):
	if point.x in range(4) and point.y in range (4):
		return True
	else:
		return False

def SolveMazeUnit(point):
	if point.x == 3 and point.y == 3:
		sol[point.x][point.y] = 1;
		return True

	if InMaze(point):
		sol[point.x][point.y] = 1

		if point.x +1 in range(4):
			nextpoint1 = maze[point.x+1][point.y]
			if nextpoint1.statu == 1:
				if SolveMazeUnit(nextpoint1):
					return True
					
		if point.y + 1 in range(4):
			nextpoint2 = maze[point.x][point.y+1]
			if nextpoint2.statu == 1:
				if SolveMazeUnit(nextpoint2):
					return True

		sol[point.x][point.y] = 0

		return False

	return False


def SolveMaze():
	pointstart = maze[0][0]
	if SolveMazeUnit(pointstart)==False:
		print "No Solutiuon"
		return False
	printSolution()
	return True

def printSolution():
	for i in range(4):
		print sol[i]

if __name__ == "__main__":
	GenerateMaze()
	SolveMaze()
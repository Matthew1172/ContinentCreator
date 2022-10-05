import numpy as np

class BoardAnalysis:
    board = [[]]
    area = 0

    sea = 0
    land = 0

    #Returns true if 65% of all sea tiles have 2 or more neighbors that are sea tiles
    seaNeighborTest = False
    #Returns true if 65% of all land tiles have 2 or more neighbors that are land tiles
    landNeighborTest = False
    #Returns true if all edges of the board are sea tiles
    edgeCaseTest = False
    #Returns true if there are 60% or more sea tiles
    percentTileTest = False

    def __init__(self, board):
        self.board = board.board
        self.area = board.s * board.s
        self.getTiles()

        #run tests
        self.edgeCaseTest = self.runEdgeTest()
        self.runNeighborTest()
        self.percentTileTest = self.runPercentTileTest()

    def runPercentTileTest(self):
        if self.totalSea() < .6:
            return False
        else:
            return True

    '''
    set the number of land and sea tiles
    '''
    def getTiles(self):
        for r in self.board:
            for c in r:
                if c == 0:
                    self.sea+=1
                else:
                    self.land+=1

    '''
    return true or false. Returns true if all edges of the board are sea tiles
    '''
    def runEdgeTest(self):

        #check top
        for t in self.board[0]:
            if t != 0:
                return False
        #check bottom
        for t in self.board[-1]:
            if t != 0:
                return False

        board = np.transpose(self.board)
        #check left
        for t in board[0]:
            if t != 0:
                return False
        #check right
        for t in board[-1]:
            if t != 0:
                return False
        #all edge cases passed
        return True

    def checkNeighbors(self, i, j, tile):

        try:
            nw = self.board[i][j]
        except KeyError:
            return False
        if nw == tile:
            return True

    def checkTop(self, i, j):
        if i == 0: return True
        else: return False

    def checkBottom(self, i, j):
        if i == len(self.board[0])-1: return True
        else: return False

    def checkLeft(self, i, j):
        if j == 0: return True
        else: return False

    def checkRight(self, i, j):
        if j == len(self.board[0])-1: return True
        else: return False

    '''
    nw  n   ne
    w   t   e
    sw  s   se
    '''
    def runNeighborTest(self):
        sea_that_has_2n = 0
        land_that_has_2n = 0
        for i,r in enumerate(self.board):
            for j,t in enumerate(r):
                neighbors = 0
                if not self.checkTop(i, j):
                    #check if t is on the top or left edge
                    if self.checkLeft(i, j):
                        nw = -1
                    else:
                        nw = self.board[i - 1][j - 1]
                    if nw == t:
                        neighbors += 1

                    n = self.board[i-1][j]
                    if n == t:
                        neighbors += 1

                    #check if t is on the top or right edge
                    if self.checkRight(i, j):
                        ne = -1
                    else:
                        ne = self.board[i-1][j+1]
                    if ne == t:
                        neighbors += 1

                #check if t is on the left edge
                if self.checkLeft(i ,j):
                    w = -1
                else:
                    w = self.board[i][j-1]
                if w == t:
                    neighbors += 1

                #check if t is on the right edge
                if self.checkRight(i ,j):
                    e = -1
                else:
                    e = self.board[i][j+1]
                if e == t:
                    neighbors += 1

                if not self.checkBottom(i, j):
                    #check if t is on the left or bottom edge
                    if self.checkLeft(i, j):
                        sw = -1
                    else:
                        sw = self.board[i+1][j-1]
                    if sw == t:
                        neighbors += 1

                    s = self.board[i+1][j]
                    if s == t:
                        neighbors += 1

                    #check if t is on the bottom or right edge
                    if self.checkRight(i, j):
                        se = -1
                    else:
                        se = self.board[i+1][j+1]
                    if se == t:
                        neighbors += 1

                #check if current tile has 2 or more of the same neighbor
                if neighbors > 1:
                    if t == 0:
                        sea_that_has_2n += 1
                    else:
                        land_that_has_2n += 1

        self.landNeighborTest = self.landNeighbors(land_that_has_2n)
        self.seaNeighborTest = self.seaNeighbors(sea_that_has_2n)

    '''
    return true or false.
    Returns true if 65% of all sea tiles have 2 or more neighbors that are sea tiles
    '''
    def seaNeighbors(self, sea_that_has_2n):
        p = sea_that_has_2n/self.sea
        if p < .65:
            return False
        else:
            return True

    '''
    return true or false.
    Returns true if 65% of all land tiles have 2 or more neighbors that are land tiles
    '''
    def landNeighbors(self, land_that_has_2n):
        p = land_that_has_2n/self.land
        if p < .65:
            return False
        else:
            return True

    '''
    return true or false.
    Returns the percentage of land tiles
    '''
    def totalLand(self):
        return self.land/self.area

    '''
    return true or false.
    Returns the percentage of sea tiles
    '''
    def totalSea(self):
        return self.sea/self.area
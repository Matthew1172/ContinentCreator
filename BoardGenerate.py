from Board import Board
import numpy as np
import random as r
import math


class BoardGenerate(Board):
    s1 = 2
    def __init__(self, s):
        super().__init__(s)

    def generate(self):
        s = self.s

        for i in range(0, 1):
            # place a random chunk
            x = r.randint(self.s // 12, self.s // 2 - self.s // 3)
            y = r.randint(self.s // 12, self.s // 2 - self.s // 3)

            m = r.randint(s // 8, s // 4)
            n = r.randint(s // 8, s // 4)
            self.placeChunk(m, n, x, y)

            b = r.randint(s // 8, s // 4)
            h = int(math.sqrt((3*b**2)/4))
            x = self.s//2
            y = self.s//2


            #self.placeTriangleUp(b,h,x+b-1,y)
            #self.placeTriangleDown(b,h,x+b-1+b//2,y+b//2)
            #self.placeTriangleUp(b, h, x + b - 1+b, y)

            #self.placeTriangleRight(b,h,x+b-1,y)
            #self.placeTriangleLeft(b,h,x+b-1,y)

        self.board = np.pad(self.board, 2, 'constant', constant_values=(0))

    def placeTriangleLeft(self, b, h, x, y):
        i3=b-1
        for i in range(0, h):
            for j in range(0, b-i3):
                try:
                    self.board[x - j][y - i] = 1
                except IndexError:
                    pass
            for k in range(0, b-i3):
                try:
                    self.board[x + k][y - i] = 1
                except IndexError:
                    pass
            i3-=1

    def placeTriangleRight(self, b, h, x, y):
        i3 = b-1
        for i in range(0, h):
            for j in range(0, b-i3):
                try:
                    self.board[x - j][y + i] = 1
                except IndexError:
                    pass
            for k in range(0, b-i3):
                try:
                    self.board[x + k][y + i] = 1
                except IndexError:
                    pass
            i3-=1

    def placeTriangleUp(self, b, h, x, y):
        i3 = b-1
        for i in range(0, h):
            for j in range(0, b-i3):
                try:
                    self.board[x + i][y + j] = 1
                except IndexError:
                    pass
            for k in range(0, b-i3):
                if y - k > 0:
                    try:
                        self.board[x + i][y - k] = 1
                    except IndexError:
                        pass
            i3-=1

    def placeTriangleDown(self, b, h, x, y):
        i3=b-1
        for i in range(0, h):
            for j in range(0, b-i3):
                try:
                    self.board[x - i][y - j] = 1
                except IndexError:
                    pass

            for k in range(0, b-i3):
                if y - k > 0:
                    try:
                        self.board[x - i][y + k] = 1
                    except IndexError:
                        pass
            i3-=1



    def placeChunk(self, m, n, x, y):
        # place top right corner of mxn chunk at x,y
        for i in range(0, m):
            for j in range(0, n):
                try:
                    self.board[x + i][y + j] = 1
                except IndexError:
                    pass

                if j == 0:
                    for i2 in range(1, self.s1):
                        if y - i2 > 0:
                            try:
                                self.board[x + i][y - i2] = r.randint(0, 1)
                            except IndexError:
                                pass
                        else:
                            break

                if i == 0:
                    for i2 in range(1, self.s1):
                        if x - i2 > 0:
                            try:
                                self.board[x - i2][y + j] = r.randint(0, 1)
                            except IndexError:
                                pass
                        else:
                            break

                if j == n - 1:
                    for i2 in range(1, self.s1):
                        try:
                            self.board[x + i][y + j + i2] = r.randint(0, 1)
                        except IndexError:
                            pass

                if i == m - 1:
                    for i2 in range(1, self.s1):
                        try:
                            self.board[x + i + i2][y + j] = r.randint(0, 1)
                        except IndexError:
                            pass

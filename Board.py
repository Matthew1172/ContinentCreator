import random as r
import numpy as np
import matplotlib.colors
import matplotlib.pyplot as plt
import csv


class Board:

    board = [[]]
    s = 0

    def __init__(self, s):
        self.s = s
        self.board = np.zeros((s,s), dtype=int)

    def drawBoard(self):
        cmap = matplotlib.colors.ListedColormap(["lightseagreen", "lawngreen"])
        colormaps = [cmap]
        data = self.board
        n = len(colormaps)
        fig, axs = plt.subplots(1, n, figsize=(n * 2 + 2, 3),
                                constrained_layout=True, squeeze=False)
        for [ax, cmap] in zip(axs.flat, colormaps):
            psm = ax.pcolormesh(data, cmap=cmap, rasterized=True, vmin=0, vmax=1)
            #fig.colorbar(psm, ax=ax)
        plt.axis('off')
        plt.show()

    def saveBoard(self, name):
        with open(name, "w+") as my_csv:
            csvWriter = csv.writer(my_csv, delimiter=',')
            csvWriter.writerows(self.board)

    def loadBoard(self, name):
        file = open(name)
        self.board = np.loadtxt(file, delimiter=",", dtype=int)

class OldBoard:
    board = [[]]
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def createRandomBoardOLD(self):
        board = [[r.randint(0, 1) for j in range(self.y)] for i in range(self.x)]
        self.board = np.array(board)

    def createRandomBoard(self):
        # Array for random sampling
        sample_arr = [True, False]
        sample_arr = [0, 1]
        # Create a numpy array with random True or False of size 10
        self.board = np.random.choice(sample_arr, size=(self.x, self.y))
        print(self.board)

    def drawBoard(self):
        cmap = matplotlib.colors.ListedColormap(["lawngreen", "lightseagreen"])
        colormaps = [cmap]
        data = self.board
        n = len(colormaps)
        fig, axs = plt.subplots(1, n, figsize=(n * 2 + 2, 3),
                                constrained_layout=True, squeeze=False)
        for [ax, cmap] in zip(axs.flat, colormaps):
            psm = ax.pcolormesh(data, cmap=cmap, rasterized=True, vmin=0, vmax=1)
            #fig.colorbar(psm, ax=ax)
        plt.axis('off')
        plt.show()

    def saveBoard(self, name):
        with open(name, "w+") as my_csv:
            csvWriter = csv.writer(my_csv, delimiter=',')
            csvWriter.writerows(self.board)

    def loadBoard(self, name):
        file = open(name)
        self.board = np.loadtxt(file, delimiter=",", dtype=int)

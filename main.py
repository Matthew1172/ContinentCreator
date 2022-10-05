from Board import Board
from BoardGenerate import BoardGenerate
from BoardAnalysis import BoardAnalysis

def main():
    s = 100
    name = "board1.csv"

    #create board
    world = BoardGenerate(s)

    world.generate()
    world.saveBoard(name)

    #world.loadBoard(name)

    world.drawBoard()
    print(world.board)

    #analyze board
    A = BoardAnalysis(world)




if __name__ == "__main__":
    main()

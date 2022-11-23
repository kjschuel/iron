from source.CreateBoard import PuzzleBoard

def run():

    params = {
        'size': '6',
        'preset': '123r23bkj'
    }

    board = PuzzleBoard(params)

    print('Board Size:\t %i' % board.size)
    print('Board:\t\t %s' % board.board_pieces)




if __name__ == '__main__':
    run()
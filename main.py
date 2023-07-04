from source.CreateBoard import PuzzleBoard

def run():

    print('\n\n')


    params = {
        'size': '6',
        'preset': '123r23bkj'
    }

    board = PuzzleBoard(params)

    print('Board Size:\t %i' % board.size)
    print('Board:\t\t %s' % board.board_pieces)

    board.forge()
    # board.displayOptions


    print('\n\n')

if __name__ == '__main__':
    run()
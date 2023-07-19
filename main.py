from source.CreateBoard import PuzzleBoard

def run():

    print('\n\n')


    params = {
        'size': '3',
        'preset': '123r03bkj',
        'moves': 'all'
    }

    board = PuzzleBoard(params)

    print('Board Size:\t %i' % board.size)
    print('Board:\t\t %s' % board.board)
    print('Moves:\t\t %s' % board.moves)

    print('\n\n')

if __name__ == '__main__':
    run()
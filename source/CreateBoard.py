# should make as a board class
class PuzzleBoard:

    size = None
    board_pieces = None
    _viable_pieces = ['1', '2', '3', '4',
        'R',    # Rook
        'B',    # Bishop
        'K',    # Knight
        'Q',    # Queen
        'J'     # Rum Jug
    ]

    def __init__(self, params=None):
        self._initializeParams(params=params)

    def setSize(self, new_size):
        if isinstance(new_size, int):
            self.size = new_size
        else:
            print('Error: new size must be an \'int\'')

    def setBoardPieces(self, new_board_pieces):
        if isinstance(new_board_pieces, str):
            self.board_pieces = new_board_pieces
        else:
            print('Error: new board must be a \'string\'')

    def _initializeParams(self, params):

        if not isinstance(params, dict):
            print('Error: \'dict\' expected as the input form.')
            exit(0)

        try:
            size = params['size']
        except KeyError:
            size = None

        try:
            board_pieces = params['preset']
        except KeyError:
            board_pieces = None

        if size is None and board_pieces is None:
            print('Error: an initial size or board must be given.')
            exit(0)

        elif board_pieces is not None:

            if not isinstance(board_pieces, str):
                print('Error: The board must be of type \'string\'.')
                exit(0)

            board_pieces = board_pieces.upper()

            if size is not None:
                print('Warning: a size was given but a preset board was used.')

            from Universal.MathFuncs import is_square
            num_pieces = len(board_pieces)
            if not is_square(i=num_pieces):
                print('Error: the number of pieces must be a perfect square.')
                exit(0)

            from Universal.StringFun import stringOnlyUsesFromList
            if not stringOnlyUsesFromList(candidates=board_pieces,
                                          viable_chars=self._viable_pieces):
                print('Error: Only values from the following lise are allowed.')
                print(self._viable_pieces)
                exit(0)

            self.setSize(num_pieces)
            self.setBoardPieces(board_pieces)

        else:   # size not none and board_pieces is none

            if not isinstance(size, int):
                print('Error: The board size must be of type \'int\'.')
                exit(0)

            print('Warning: No board setup specified. Creating a Random board.')
            from Universal.StringFun import generateRandomStringUsing

            self.size = size
            self.board_pieces = generateRandomStringUsing(size**2,
                                                          self._viable_pieces)


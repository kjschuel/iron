# should make as a board class
class PuzzleBoard:

    size = None
    board = None
    moves = None
    _viable_pieces = ['1', '2', '3', '4',
        'R',    # Rook
        'B',    # Bishop
        'K',    # Knight
        'Q',    # Queen
        'J',    # Rum Jug
        '0'     # hole
    ]
    routes = None

    def __init__(self, params=None):
        self._initializeParams(params=params)

    def setSize(self, new_size):
        if isinstance(new_size, int):
            self.size = new_size
        else:
            print('Error: new size must be an \'int\'')

    def setBoard(self, new_board_pieces):
        if isinstance(new_board_pieces, str):
            placeholder = []
            new_row = []
            for i, piece in enumerate(new_board_pieces):
                new_row.append(piece)
                if len(new_row) == self.size:
                    placeholder.append(new_row)
                    new_row = []
            self.board = placeholder
        else:
            print('Error: new board must be a \'string\'')

    def setMoves(self, moves):
        if isinstance(moves, list):
            # TODO: check if valid move
            pass 
        # remove moves that index a '0'
        self.moves = moves

    def forge(self, choices=None):
        if choices == None:
            choices = 'all'
        
        if not self._validChoices(choices):
            #TODO we are done here, break out elegantly
            print('invalid choices')
            return False
        
        #TODO: if all choices are available, populate exactly what those 
        # choices are
        
        self._mapRoute([], choices)

        return True
    
    def getPiece(self, position):
        #TODO: return the piece
        return True
    
    def drawBoard(self):
        return 1

    def _initializeParams(self, params):

        if not isinstance(params, dict):
            print('Error: \'dict\' expected as the input form.')
            exit(0)

        self._initializeSize(params)
        self._initializeBoard(params)
        self._initializeMoves(params)
   
    def _validChoices(self, choices):
        #TODO complete
        #1. if 'all' this is valid at all times
        #2. choices are given as alpha/numeric combos, make sure the choice is
        #   a. fitting for the size of the board
        #   b. does not appear at a hole. 
        return True
    
    def _initializeSize(self, params):
        try:
            size = params['size']
        except KeyError:
            print('Warning: a size was not given.')
            size = None

        try:
            size = int(size)
        except ValueError:
            print('Warning: poor format for size; using a size = 6.')
            size = 6

        self.setSize(size)

    def _initializeBoard(self, params):
        try:
            board_pieces = params['preset']
        except KeyError:
            board_pieces = None

        if board_pieces is not None:

            if not isinstance(board_pieces, str):
                print('Error: The board must be of type \'string\'.')
                exit(0)

            board_pieces = board_pieces.upper()

            if self.size**2 != len(board_pieces):
                print('Error: the size given does not match the size of the' + 
                      ' preset board being used.')
                exit(0)

            from toolshed.MathFuncs import is_square
            num_pieces = len(board_pieces)
            if not is_square(i=num_pieces):
                print('Error: the number of pieces must be a perfect square.')
                exit(0)

            from toolshed.StringFun import stringOnlyUsesFromList
            if not stringOnlyUsesFromList(candidates=board_pieces,
                                          viable_chars=self._viable_pieces):
                print('Error: Only values from the following lise are allowed.')
                print(self._viable_pieces)
                exit(0)

        else:
            print('Warning: No board setup specified. Creating a Random board.')
            from toolshed.StringFun import generateRandomStringUsing
            board_pieces = ''.join(generateRandomStringUsing(self.size**2,
                                                   self._viable_pieces))
        
        self.setBoard(board_pieces)

    def _initializeMoves(self, params):

        try:
            moves = params['moves']
        except KeyError:
            moves = None
        
        if moves == 'all':
            temp_moves = []
            for i in range(self.size):
                for j in range(self.size):
                    if self.board[i][j] == '0':
                        continue
                    temp_moves.append([i, j])
            moves = temp_moves

        self.setMoves(moves)

            



    def _mapRoute(self, map, choices):

        routes = []

        for choice in choices:
            self.getPiece(choice)

        return True
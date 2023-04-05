from BoardGame import BoardGame
from copy import deepcopy
import Constants

class Hitori(BoardGame):
    """Classe che gestisce il gioco Hitori"""
    def __init__(self):
        self._w, self._h = 0, 0
        self._board, self._board_annotation, self._win_board = [], [], []
        self._bool_matrix = [[False for j in range(len(self._board_annotation))] for i in range(len(self._board_annotation))]

    def fill_annotation_board(self): self._board_annotation = [[Constants.CLEAR for j in range(0, self._h)] for i in range(0, self._w)]

    def fill_win_board(self): self._win_board = [[0 for j in range(0, self._h)] for i in range(0, self._w)]

    def fill_main_board(self, file_name):
        self._board = []
        with open(file_name, Constants.FILE_MODE) as f:
            for line in f:
                self._board.append([int (x) for x in line.split(',')])
            self._w, self._h = len(self._board[0]), len(self._board)
        return self._board

    def cols(self): return self._w

    def rows(self): return self._h

    def message(self): return Constants.FINAL_MESSAGE

    def board_annotation(self): return self._board_annotation

    def is_valid_position(self):
        """Verifica che non ci siano celle nere adiacenti"""
        black_lst = []
        for i in range(0, self._w):
            for j in range(0, self._h):
                if self._board_annotation[i][j] == Constants.BLACK: black_lst.append((i, j))
        for k in black_lst:
            for s in black_lst:
                blackTuples = tuple(map(lambda x ,y: abs(x - y), k, s))
                if blackTuples[0] == 0 and blackTuples[1] == 1 or blackTuples[1] == 0 and blackTuples[0] == 1: return False
        return True     

    def value_at(self, y, x): return str(self._board[y][x])

    def play_at(self, y, x):
        if self._board_annotation[y][x] == Constants.BLACK or self._board_annotation[y][x] == Constants.CIRCLE: self._board_annotation[y][x] = Constants.CLEAR
        else: self._board_annotation[y][x] = Constants.BLACK
            
    def flag_at(self, y, x):
        if self._board_annotation[y][x] == Constants.CIRCLE or self._board_annotation[y][x] == Constants.BLACK: self._board_annotation[y][x] = Constants.CLEAR
        else: self._board_annotation[y][x] = Constants.CIRCLE

    def solve(self):
        """Risolve automaticamente il gioco con BT"""
        self.fill_annotation_board()
        self.solve_recursive()

    def help(self):
        """Vengono forniti i suggerimenti per le mosse successive"""
        if not(self.wrong()): self.get_suggestion()
        else: return False
        
    def get_suggestion(self):
        """Suggerimenti: applicati entrambi gli automatismi, suggerisce la mossa successiva"""
        tmp_matrix = deepcopy(self._board_annotation)

        for i in range(0, self._w):
            for j in range(0, self._h):
                if self._board_annotation[i][j] == Constants.CLEAR:
                    self._board_annotation[i][j] = Constants.CIRCLE
                    self.circle_around_black_cells()
                    self.hover_cells()
                    if self.wrong(): self._board_annotation[i][j] = Constants.BLACK
                    matrix_tmp_circles = deepcopy(self._board_annotation)
                    self._board_annotation = deepcopy(tmp_matrix)

                    self._board_annotation[i][j] = Constants.BLACK
                    self.circle_around_black_cells()
                    self.hover_cells()
                    if self.wrong(): self._board_annotation[i][j] = Constants.CIRCLE
                    matrix_tmp_squares = deepcopy(self._board_annotation)
                    self._board_annotation = deepcopy(tmp_matrix)
                    if self.wrong(): self._board_annotation = deepcopy(tmp_matrix)
                    else:
                        for i in range(0, self._w):
                            for j in range(0, self._h):
                                if (matrix_tmp_squares[i][j] == Constants.BLACK and matrix_tmp_circles[i][j] == Constants.BLACK) and matrix_tmp_squares[i][j] != Constants.CLEAR and matrix_tmp_circles[i][j] != Constants.CLEAR:
                                    self._board_annotation[i][j] = matrix_tmp_squares[i][j]
                                if (matrix_tmp_squares[i][j] == Constants.CIRCLE and matrix_tmp_circles[i][j] == Constants.CIRCLE) and matrix_tmp_squares[i][j] != Constants.CLEAR and matrix_tmp_circles[i][j] != Constants.CLEAR:
                                    self._board_annotation[i][j] = matrix_tmp_squares[i][j]
                        tmp_matrix = deepcopy(self._board_annotation)

    def check_rows(self):
        """Controlla un eventuale vincita sulle righe"""
        for i in range (0, self._w):
            for j in range(0, self._h):
                if self._win_board[i].count(self._win_board[i][j]) > 1 and self._win_board[i][j] != Constants.BLACK: return False
        return True

    def check_cols(self):
        """Controlla un eventuale vincita sulle colonne"""
        lst = []                   
        for i in range(0, self._w):
            [lst.append(row[i]) for row in self._win_board]
            for j in range(0, len(lst)):
                if lst.count(lst[j]) > 1 and lst[j] != Constants.BLACK: return False
            lst = []
        return True
        
    def populate_win_matrix(self):
        for i in range(self._h):
            for j in range(self._w):
                if self._board_annotation[i][j] == Constants.BLACK: self._win_board[i][j] = Constants.BLACK
                else: self._win_board[i][j] = self._board[i][j]

    def find_first_white_cell(self):  
        """Ritorna la posizione della prima cella bianca, necessaria per la verifica dell'adiacenza delle celle bianche"""
        for i in range(0, len(self._board_annotation)):
            for j in range(0, len(self._board_annotation)):
                if self._board_annotation[i][j] == Constants.CLEAR or self._board_annotation[i][j] == Constants.CIRCLE: return (i, j)

    def find_first_white_cell_bt(self):  
        for i in range(0, len(self._board_annotation)):
            for j in range(0, len(self._board_annotation)):
                if self._board_annotation[i][j] == Constants.CLEAR: return (i, j)

    def circle_around_black_cells(self):
        """Automatismo 1: cerchia intorno alle celle nere"""
        lst = []    
        for i in range(0, self._h):
            for j in range(0, self._w):
                if self._board_annotation[i][j] == Constants.CLEAR: lst.append((i, j))
        for x in range(0, self._h):
            for y in range(0, self._h):
                if self._board_annotation[x][y] == Constants.BLACK:
                    for k in lst:
                        if (x, y + 1) == k: self._board_annotation[x][y + 1] = Constants.CIRCLE
                        elif (x, y - 1) == k: self._board_annotation[x][y - 1] = Constants.CIRCLE
                        elif(x + 1, y) == k: self._board_annotation[x + 1][y] = Constants.CIRCLE
                        elif(x - 1, y) == k: self._board_annotation[x - 1][y] = Constants.CIRCLE
    
    def hover_cells(self):  
        """Automatismo 2: annerisce gli stessi valori del numero cerchiato su riga e colonna"""
        value, pos = 0, (0, 0)
        for y in range(0, self._h):
            for x in range(0, self._w):
                if self._board_annotation[y][x] == Constants.CIRCLE:
                    pos = (y, x)
                    value = self._board[y][x]
                    for j in range(0, self._w):
                        if self._board[j][x] == value and (j, x) != pos: self._board_annotation[j][x] = Constants.BLACK
                        if self._board[y][j] == value and (y, j) != pos: self._board_annotation[y][j] = Constants.BLACK

    def count_true_cells(self):
        """Conta le celle della matrice booleana per l'adiacenza delle celle bianche"""
        n_bool_whites = 0
        for i in range (0, len(self._bool_matrix)): n_bool_whites += self._bool_matrix[i].count(True)
        return n_bool_whites

    def count_white_cells(self):
        """Conta le celle bianche effettive presenti"""
        n_whites = 0
        for i in range (0, len(self._bool_matrix)): n_whites += self._board_annotation[i].count(Constants.CLEAR); n_whites += self._board_annotation[i].count(Constants.CIRCLE)
        return n_whites

    def check_white_adjacency(self):
        """Se il valore torna True, allora nessuna cella bianca è isolata"""
        return self.count_true_cells() == self.count_white_cells()

    def wrong(self):
        """Controlla che la situazione di gioco sia corretta"""
        self._bool_matrix = [[False for j in range(len(self._board_annotation))] for i in range(len(self._board_annotation))]
        try:
            x, y = self.find_first_white_cell()
            self.find_white_adjacency(x, y)
        except: pass 
        return not(self.check_white_adjacency() and self.is_valid_position() and self.check_circle_on_line_cols())
    
    def find_white_adjacency(self, x, y): 
        """Ricorsione per l'adiacenza delle celle bianche"""
        self._bool_matrix[x][y] = True
        if y + 1 < self._w:
            if self._bool_matrix[x][y + 1] != True and (self._board_annotation[x][y + 1] == Constants.CLEAR or self._board_annotation[x][y + 1] == Constants.CIRCLE):
                self._bool_matrix[x][y + 1] = True 
                self.find_white_adjacency(x, y + 1)
        if y - 1 >= 0:
            if self._bool_matrix[x][y - 1] != True and (self._board_annotation[x][y - 1] == Constants.CLEAR or self._board_annotation[x][y - 1] == Constants.CIRCLE):
                self._bool_matrix[x][y - 1] = True
                self.find_white_adjacency(x, y - 1)
        if x + 1 < self._h:
            if self._bool_matrix[x + 1][y] != True  and (self._board_annotation[x + 1][y] == Constants.CLEAR or self._board_annotation[x + 1][y] == Constants.CIRCLE):
                self._bool_matrix[x + 1][y] = True 
                self.find_white_adjacency(x + 1, y)
        if x - 1 >= 0:
            if self._bool_matrix[x - 1][y] != True and (self._board_annotation[x - 1][y] == Constants.CLEAR or self._board_annotation[x - 1][y] == Constants.CIRCLE):
                self._bool_matrix[x - 1][y] = True 
                self.find_white_adjacency(x - 1, y)

    def solve_recursive(self):
        self.get_suggestion()
        if self.wrong(): return False

        first_white_cell = self.find_first_white_cell_bt()
        if first_white_cell != None and first_white_cell[0] < self._w and first_white_cell[1] < self._w:
            tmp_matrix = [row[:] for row in self._board_annotation]
            for tuples in (Constants.BLACK, Constants.CIRCLE):
                self._board_annotation[first_white_cell[0]][first_white_cell[1]] = tuples
                if self.solve_recursive(): return True
                self._board_annotation = [row[:] for row in tmp_matrix] 
        return self.finished()

    def check_circle_on_line_cols(self):
        """Metodo che fa parte del wrong: sbagliato se sono presenti due numeri cerchiati uguali sulla stessa riga o colonna"""
        value = 0
        pos = (0, 0)
        for y in range(0, self._h):
            for x in range(0, self._w):
                if self._board_annotation[y][x] == Constants.CIRCLE:
                    pos, value = (y, x), self._board[y][x]
                    for j in range(0, self._w):
                        if self._board[j][x] == value and (j, x) != pos and self._board_annotation[j][x] == Constants.CIRCLE: return False
                        if self._board[y][j] == value and (y, j) != pos and self._board_annotation[y][j] == Constants.CIRCLE: return False
        return True

    def finished(self):
        """Verifica la vittoria e la fine del gioco"""
        if self.wrong(): return False
        else:
            self.populate_win_matrix()
            if self.check_cols() and self.check_rows(): return True
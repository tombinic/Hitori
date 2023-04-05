from unittest import TestCase, main
import Constants
from Hitori import Hitori

class HitoriTest(TestCase): 
    def test_hitori_game(self):
        hitori = Hitori()
        matrix = hitori.fill_main_board("games/hitori-5x5.csv")
        hitori.fill_annotation_board()
        hitori.fill_win_board()
        test_values_play_at = ((0, 0), (0, 4), (2, 4), (3, 3), (0, 4))
        test_values_flag_at = ((0, 0), (0, 1))
        for param in test_values_play_at:
            y, x = param
            hitori.play_at(y, x)
            self.assertTrue(int(hitori.value_at(y, x)) == matrix[y][x])
        for param in test_values_flag_at:
            y, x = param
            hitori.flag_at(y, x)
            self.assertTrue(int(hitori.value_at(y, x)) == matrix[y][x])

    def test_finished(self):
        hitori = Hitori()
        matrix = hitori.fill_main_board("games/hitori-12x12.csv")
        hitori.fill_annotation_board()
        hitori.fill_win_board()

        #solve with backtracking
        hitori.solve_recursive()
        self.assertTrue(hitori.finished())

        hitori = Hitori()
        matrix = hitori.fill_main_board("games/hitori-5x5.csv")
        hitori.fill_annotation_board()
        hitori.fill_win_board()

        #solve by user
        test_finished = ((0, 0), (0, 4), (3, 1), (1, 1), (2, 4), (3, 3), (4, 0))
        for param in test_finished:
            y, x = param
            hitori.play_at(y, x)
        self.assertTrue(hitori.finished())

    def test_wrong(self):
        hitori = Hitori()
        matrix = hitori.fill_main_board("games/hitori-5x5.csv")
        hitori.fill_annotation_board()
        hitori.fill_win_board()
        test_wrong_squares = ((0, 0), (0, 1))
        test_wrong_circles = ((4, 1), (3, 1))
        test_wrong_white_adjancency = ((1, 0), (0, 1))
        #near squares
        for param in test_wrong_squares:
            y, x = param
            hitori.play_at(y, x)
        self.assertTrue(hitori.wrong())

        #near circles
        for param in test_wrong_circles:
            y, x = param
            hitori.flag_at(y, x)
        self.assertTrue(hitori.wrong())

        #white cells isolated
        for param in test_wrong_white_adjancency:
            y, x = param
            hitori.play_at(y, x)
        self.assertTrue(hitori.wrong())
    
    def test_auto(self):
        hitori = Hitori()
        matrix = hitori.fill_main_board("games/hitori-5x5.csv")
        hitori.fill_annotation_board()
        hitori.fill_win_board()
        
        #test circles
        hitori.play_at(1, 2)
        hitori.circle_around_black_cells()
        matrix = hitori.board_annotation()
        self.assertTrue(matrix[0][2] == Constants.CIRCLE and matrix[1][1] == Constants.CIRCLE and matrix[2][2] == Constants.CIRCLE and matrix[1][3] == Constants.CIRCLE)
    
        #test squares
        hitori.flag_at(3, 0)
        hitori.hover_cells()
        matrix = hitori.board_annotation()
        self.assertTrue(matrix[3][1] == Constants.BLACK)

if __name__ == '__main__':
    main()
import g2d
from BoardGame import BoardGame
from Menu import Menu
import Constants

class BoardGameGui:
    def __init__(self, g: BoardGame):
        self._menu = Menu()
        self._game = g

    def start_game(self, type_game):
        self._game.fill_main_board(type_game)
        self._game.fill_annotation_board()
        self._game.fill_win_board()
        g2d.init_canvas((self._game.cols() * Constants.W_CANVAS, self._game.rows() * Constants.H_CANVAS))
        self._menu.active_menu(False)
        self._menu.active_menu_levels(False)
        
    def tick(self):
        if self._menu.is_active_menu():
            self._menu.draw_menu()
            if g2d.key_pressed(Constants.ENTER): self._menu.active_menu(False); self._menu.active_menu_levels(True)
            elif g2d.key_pressed(Constants.C) or g2d.key_pressed(Constants.C_MIN): self._menu.active_menu_rules(True); g2d.init_canvas((Constants.X_BG_RULES, Constants.Y_BG_RULES))
        if self._menu.is_active_menu_rules():
            self._menu.draw_rules()
            if g2d.key_pressed(Constants.ESCAPE):
                g2d.init_canvas((Constants.X_BG, Constants.Y_BG))
                self._menu.active_menu(True)
                self._menu.active_menu_rules(False) 
                g2d.clear_canvas()
                g2d.update_canvas()
        if self._menu.is_active_menu_levels():
            g2d.init_canvas((Constants.X_BG_LEVELS, Constants.Y_BG_LEVELS))
            self._menu.draw_levels()
            if g2d.key_pressed(Constants.BTN_1): self.start_game(Constants.VERY_EASY)
            elif g2d.key_pressed(Constants.BTN_2): self.start_game(Constants.EASY)
            elif g2d.key_pressed(Constants.BTN_3): self.start_game(Constants.MEDIUM)
            elif g2d.key_pressed(Constants.BTN_4): self.start_game(Constants.HARD)
            elif g2d.key_pressed(Constants.BTN_5): self.start_game(Constants.VERY_HARD)
            elif g2d.key_pressed(Constants.BTN_6): self.start_game(Constants.IMPOSSIBLE)
            elif g2d.key_pressed(Constants.ESCAPE):
                g2d.init_canvas((Constants.X_BG, Constants.Y_BG))
                self._menu.active_menu(True)
                self._menu.active_menu_levels(False) 
                g2d.clear_canvas()
                g2d.update_canvas()
        if not(self._menu.is_active_menu()) and not(self._menu.is_active_menu_levels()):
            if g2d.key_pressed(Constants.ESCAPE):
                g2d.clear_canvas()
                g2d.update_canvas()
                g2d.init_canvas((Constants.X_BG, Constants.Y_BG))
                self._menu.active_menu(True)
            else:
                mouse = g2d.mouse_position()
                x, y = mouse[0] // Constants.W_CANVAS, mouse[1] // Constants.H_CANVAS
                if x >= 0 and x < self._game.rows() and y >= 0 and y < self._game.cols():
                    if g2d.key_pressed(Constants.MIDDLE_BUTTON): self._game.flag_at(y, x)
                    elif g2d.key_pressed(Constants.LEFT_BUTTON): self._game.play_at(y, x)
                    elif g2d.key_pressed(Constants.F_MIN) or g2d.key_pressed(Constants.F): self._game.solve()
                    elif g2d.key_pressed(Constants.H_MIN) or g2d.key_pressed(Constants.H): self._game.help()
                    elif g2d.key_pressed(Constants.R_MIN) or g2d.key_pressed(Constants.R): self._game.fill_annotation_board()
                    self.update_buttons()

    def update_buttons(self):
        g2d.clear_canvas()
        g2d.set_color((0, 0, 0))
        cols, rows = self._game.cols(), self._game.rows()

        for y in range(1, rows):
            g2d.draw_line((0, y * Constants.H_CANVAS), (cols * Constants.W_CANVAS, y * Constants.H_CANVAS))
        for x in range(1, cols):
            g2d.draw_line((x * Constants.W_CANVAS, 0), (x * Constants.W_CANVAS, rows * Constants.H_CANVAS))
        for y in range(rows):
            for x in range(cols):
                center =  x * Constants.W_CANVAS + Constants.W_CANVAS//2, y * Constants.H_CANVAS + Constants.H_CANVAS//2
                if(self._game.board_annotation()[y][x] == Constants.BLACK): g2d.fill_rect((x * Constants.W_CANVAS, y * Constants.H_CANVAS, Constants.W_CANVAS, Constants.H_CANVAS))
                elif(self._game.board_annotation()[y][x] == Constants.CIRCLE):
                    g2d.set_color((255, 0, 0))
                    g2d.fill_circle((center), Constants.W_CANVAS / 2)
                    g2d.set_color((0, 0, 0))  
                    value = self._game.value_at(y, x)       
                    g2d.draw_text_centered(value, center, Constants.H_CANVAS // 2) 
                else:
                    value = self._game.value_at(y, x)       
                    g2d.draw_text_centered(value, center, Constants.H_CANVAS // 2)
        g2d.update_canvas()
        if self._game.finished():
            g2d.alert(self._game.message())
            self._menu.active_menu(True)
            self._menu.active_menu_levels(False)
            self._menu.active_menu_rules(False)
            g2d.init_canvas((Constants.X_BG, Constants.Y_BG))

def gui_play(game: BoardGame):
    g2d.init_canvas((Constants.X_BG, Constants.Y_BG))
    ui = BoardGameGui(game)
    g2d.main_loop(ui.tick)
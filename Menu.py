import g2d
import Constants

class Menu:
    def __init__(self):
        self._menu_active, self._menu_levels_active, self._menu_rules_active = True, False, False

    def is_active_menu(self): return self._menu_active

    def active_menu(self, state): self._menu_active = state

    def is_active_menu_levels(self): return self._menu_levels_active

    def active_menu_levels(self, state): self._menu_levels_active = state
    
    def is_active_menu_rules(self): return self._menu_rules_active

    def active_menu_rules(self, state): self._menu_rules_active = state

    def draw_menu(self):
        img_menu = g2d.load_image(Constants.IMG_BG)
        g2d.draw_image_clip(img_menu, (0, 0, Constants.X_BG, Constants.Y_BG), (0, 0, Constants.X_BG, Constants.Y_BG)) 
    
    def draw_levels(self):
        img_menu_levels = g2d.load_image(Constants.IMG_LEVELS)
        g2d.draw_image_clip(img_menu_levels, (0, 0, Constants.X_BG_LEVELS, Constants.Y_BG_LEVELS), (0, 0, Constants.X_BG_LEVELS, Constants.Y_BG_LEVELS)) 

    def draw_rules(self):
        img_menu_rules = g2d.load_image(Constants.IMG_RULES)
        g2d.draw_image_clip(img_menu_rules, (0, 0, Constants.X_BG_RULES, Constants.Y_BG_RULES), (0, 0, Constants.X_BG_RULES, Constants.Y_BG_RULES)) 
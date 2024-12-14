class DarkMode:
    def __init__(self):
        self.is_dark_mode = False

    def toggle(self):
        self.is_dark_mode = not self.is_dark_mode
        return self.is_dark_mode

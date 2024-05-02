class Colors:

    grey = (26, 31, 40)
    green = (47, 230, 23)
    red = (232, 18, 23)
    orange = (226, 116, 17)
    yellow = (237, 234, 4)
    purple = (116, 0, 247)
    cyan = (21, 204, 209)
    blue = (13, 64, 216)

    @classmethod
    def get_cell_colors(cls):
        return [cls.grey, cls.green, cls.red, cls.orange, cls.yellow, cls.purple, cls.cyan, cls.blue]
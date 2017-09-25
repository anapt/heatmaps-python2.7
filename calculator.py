class Calculate:

    def __init__(self):
        self.screen_width = 1366  # pixels
        self.screen_height = 768  # pixels

        self.pic_width = 747  # pixels
        self.pic_height = 536  # pixels
        self.upper_left = []  # used.
        self.upper_right = []
        self.lower_left = []

        self.upper_left.append((self.screen_width - self.pic_width) / 2)
        self.upper_left.append((self.screen_height - self.pic_height) / 2)

        self.upper_right = []
        self.upper_right.append(self.upper_left[0] + self.pic_width)  # used.
        # upper_right[1] = upper_left[1]

        self.lower_left.append(self.upper_left[0])
        self.lower_left.append(self.upper_left[1] + self.pic_height)  # used.

        # lower_right = []
        # lower_right[0] = upper_right[0]
        # lower_right[1] = lower_right[1]


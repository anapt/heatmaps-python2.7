from heatmap import Heatmap
import Image
from calculator import Calculate
import pandas as pd


class Heatmaps:

    def __init__(self):
        self.calculate = Calculate()
        self.l = []
        self.x_coords = []
        self.y_coords = []
        self.my_dpi = 1.17

    def init_list(self):
        datafile = './datafiles/random_coords_birds.csv'
        df = pd.read_csv(datafile)
        i = len(df['X'])
        for _ in range(i):
            x = df['X'][_]
            y = df['Y'][_]
            if (y > self.calculate.upper_left[1]) and (y < self.calculate.lower_left[1]) \
                    and (x > self.calculate.upper_left[0]) and (x < self.calculate.upper_right[0]):
                self.l.append((df['X'][_], df['Y'][_]))

        self.x_coords = [self.x_coords[0] for self.x_coords in self.l]
        self.y_coords = [self.y_coords[1] for self.y_coords in self.l]

    def read_txt(self):
        lines = [line.rstrip('\n').strip().strip('[').strip(']') for line in open('./datafiles/SECOND.txt')]
        self.l = [line.split(',') for line in lines]
        self.l = [[float(coord[0]), float(coord[1])] for coord in self.l]
        # self.x_coords = [self.x_coords[0] for self.x_coords in self.l]
        # self.y_coords = [self.y_coords[1] for self.y_coords in self.l]

    def generate_heatmap_layer(self):
        hm = Heatmap()
        foreground = hm.heatmap(self.l, area=((self.calculate.upper_left[0], self.calculate.lower_left[1]),
                                              (self.calculate.upper_right[0], self.calculate.upper_left[1])), scheme='green-red')
        foreground.save("foreground.png")

    def merge_photos(self):
        foreground = Image.open("./foreground.png")
        foreground = foreground.resize((self.calculate.pic_width, self.calculate.pic_height))
        foreground.save("foreground.png")

        # foreground = foreground.transform((self.w, self.h), Image.EXTENT, (self.upper_left[0], self.upper_left[1], self.upper_right[0], self.lower_left[1]))
        # foreground.save("foreground.png")

        # path to image
        picture = "./pictures/stop_please.png"
        background = Image.open(picture)
        background = background.resize((self.calculate.pic_width, self.calculate.pic_height))
        foreground = Image.open("./foreground.png")

        background.paste(foreground, (0, 0), foreground)
        background.save("birds.png")

if __name__ == "__main__":
    map = Heatmaps()
    map.init_list()
    # map.read_txt()
    map.generate_heatmap_layer()
    map.merge_photos()

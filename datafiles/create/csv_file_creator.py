import pymouse
import time
import csv

l = []
mouse = pymouse.PyMouse()

f = open('./datafiles/dataset.csv', 'wt')
writer = csv.writer(f)
writer.writerow(('X', 'Y'))
time.sleep(5)
try:
    while len(l) < 50:
        temp = list(mouse.position())
        l.append((temp[0], temp[1]))
        writer.writerow((temp[0], temp[1]))
        print len(l)
        print ("Move mouse")
        time.sleep(0.5)
finally:
    f.close()

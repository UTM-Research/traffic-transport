# z in code baraye  kharej kardane recorde  khas bekar  mire.
import csv
lines = list()
satr = 0
with open("path") as f:
        data = list(csv.reader(f))
with open("path", newline='') as m1:
        writer = csv.writer(m1)
        for row in data:
            satr = satr + 1
            print(satr)

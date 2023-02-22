import datetime
import csv
from datetime import datetime
with open("path") as f:
    data = list(csv.reader(f))
with open("path", newline='') as m1:
    writer = csv.writer(m1)
    for row in data:
        timestamp=row[0]
        row[19]=datetime.fromtimestamp(int(timestamp))
        writer.writerow(row)
import csv
satr=0
list=[]
file = open("path")
for line in file:
    fields = line.split(",")
    songTitle = fields[2]
    satr=satr+1
    print(satr)
    if songTitle=="Cargo" or songTitle=="tanker":
        list.append(line)

with open("path") as m1:
    writer = csv.writer(m1)
    writer.writerow(list)
#############################################################
with open("path") as f:
    with open("path") as f1:
        for line in f:
            if "input" in line:
                f1.write(line)
                print(line)
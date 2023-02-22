import csv
list0=[]
list=[]
list1=[]
line1=temp.split(",")
################################
def printme( mmis):
    latd=[]
    longd=[]
    with open("path") as f:
        for line in f:
            if mmis in line:
                fields = line.split(",")
                lat=int(float(fields[2]))
                long = int(float(fields[3]))
                latd.append(lat)
                longd.append(long)
    latd.sort()
    longd.sort()
    latd_smal=latd[0]
    latd_big=latd[len(latd)-1]
    long_smal=longd[0]
    long_big=longd[len(longd)-1]
    albedo=0
    albvisdf=0
    count=1
    with open("path") as f1:
        for line1 in f1:
            field = line1.split(",")
            x1=float(field[2])
            lat = int(x1)
            y1=float(field[3])
            long = int(y1)
            if (lat>=latd_smal and lat<=latd_big) and (long>=long_smal and long<=long_big):
                albedo = albedo + float(field[5])
                albvisdf =  albvisdf + float(field[5])
                count=count+1
                print(mmis)
    with open("path") as f2:
        for line3 in f2:
            if mmis in line3:
                field4 = line3.split(",")
                field4[26] = albedo / count
                field4[27] = albvisdf / count
                with open("path") as file_object:
                    mak = ','.join(map(str, field4))
                    file_object.write(mak)
    return;
for mmis in list:
    printme(mmis)
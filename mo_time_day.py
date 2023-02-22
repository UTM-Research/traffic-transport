import datetime
list=[]
def season(dat):
    s = dat
    date=s.split(" ")
    month=date[0].split("/")[1]
    hour=date[1].split(":")[0]
    if month in ['03','04','05']:
        add=1
    elif month in ['06','07','08']:
        add=2
    elif month in ['09','10','11']:
        add=3
    elif month in ['12','01','02']:
        add=4

    if hour>='00' and hour<='06':
        time=1
    elif hour>'06' and hour<='12':
        time=2
    elif hour>'12' and hour<='18':
        time=3
    elif hour>'18' and hour<='24':
        time=4
    return add, time

def printme( mmis):
    with open("") as f2:
        for line3 in f2:
            if mmis in line3:
                fields = line3.split(",")
                line1 = temp.split(",")
                line1[0] = fields[0]
                line1[1] = fields[1]
                x,y= season(fields[0])
                line1[2] = x
                line1[3] = y
                line1[4] = fields[4]
                line1[5] = fields[5]
                line1[6] = fields[6]
                line1[7] = fields[7]
                line1[8] = fields[8]
                line1[9] = fields[9]
                line1[10] = fields[10]
                line1[11] = fields[11]
                line1[12] = fields[12]
                line1[13] = fields[13]
                line1[14] = fields[14]
                line1[15] = fields[15]
                line1[16] = fields[16]
                line1[17] = fields[17]
                line1[18] = fields[18]
                line1[19] = fields[19]
                line1[20] = fields[20]
                line1[21] = fields[21]
                line1[22] = fields[22]
                line1[23] = fields[23]
                line1[24] = fields[24]
                line1[25] = fields[25]
                line1[26] = fields[26]
                line1[27] = fields[27]
                line1[28] = fields[28]
                line1[29] = fields[29]
                line1[30] = fields[30]
                line1[31] = fields[31]
                line1[32] = fields[32]
                line1[33] = fields[33]
                line1[34] = fields[34]
                line1[35] = fields[35]
                line1[36] = fields[36]
                line1[37] = fields[37]
                line1[38] = fields[38]
                line1[39] = fields[39]
                line1[40] = fields[40]
                line1[41] = fields[41]
                line1[42] = fields[42]
                with open("path") as file_object:
                    mak = ','.join(map(str, line1))
                    file_object.write(mak)
    return;
for mmis in list:
    printme(mmis)
    print(mmis)
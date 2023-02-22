import csv
list0=[]
list=[]
list1=[]
line1=temp.split(",")
def printme( mmis):
    count=1
    with open("path") as f2:
        for line3 in f2:
            if mmis in line3:
                count=count+1
    return count
for mmis in list:
    k=printme(mmis)
    list0.append(k)
    print(mmis,': ', k)
list0.sort()
latd_smal=list0[0]
latd_big=list0[len(list0)-1]
print(latd_smal)
print(latd_big)
##################################################
# fit model
model.fit(x, y, epochs=200, verbose=0)
yhat = model.predict(x1, verbose=0)
print(yhat)
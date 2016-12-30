import csv

f = open('INSERT_YOUR_FILENAME.csv', 'rb')
csv_f = csv.reader(f)
output = open('DESIRED_OUTPUT_FILENAME.csv', 'wb')
writer = csv.writer(output, delimiter = ',')

time=[]
csv_f.next()

row1=next(csv_f)
origin=(row1[22])

n_origin=float(row1[22])
tr= (float(row1[22])-n_origin)+(float(row1[23])/1000.0)
time.append(tr)

for row in csv_f:
    del row[16:22]
    writer.writerow(row[2:16])
    tloop= float(row[16])-n_origin+(float(row[17])/1000.0)
    time.append(tloop)
    


for row in time:
    writer.writerow([row])
     
f.close()
output.close()

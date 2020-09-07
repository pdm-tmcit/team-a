import csv

f = open('village_g10.csv', 'r')
fp = open('test.txt','a')

reader = csv.reader(f)
header = next(reader)
for row in reader:
    print(row,'\n\n')
    fp.write(str(row[0]+' ,'+str(row[1])+'\n\n'))

f.close()
fp.close()

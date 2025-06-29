from bs4 import BeautifulSoup
import re
import os
import csv

resultFile = "results.csv"
header = ['date','name','id','result','won','lost']
files = []

datadir = "../data/"

print(os.listdir(datadir))

for file in os.listdir(datadir):
    if file.startswith("stats_"):
        files.append(file)

with open(datadir+resultFile,'w',encoding='UTF8',newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)

    for file in files:

        with open(datadir+file) as fp:
            soup = BeautifulSoup(fp)
            body = soup.table.tbody

            rowData=[]
            for row in body('tr'):
                date = row.td.find(text=re.compile('[0-9][0-9][.][0-9][0-9][.][0-9][0-9]'))
                name = row("td")[1].span.text.replace('/n','')
                id = row("td")[1].a.attrs['class'][0].replace("person","")
                result = row("td")[3].a.text
                wonSets,lostSets = result.split(":")
                won = 1 if wonSets > lostSets else 0
                lost = 1 if wonSets < lostSets else 0

                row = [date,name,id,result,won,lost]

                rowData.append(row)
                
            fp.close()
        
            writer.writerows(rowData)
    f.close()


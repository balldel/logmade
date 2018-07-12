import csv
import os, sys
from datetime import datetime
from datetime import timedelta

def dmk() :
    place = "CEI_T2_UP"
    month = "04"
    lastdateofmonth = 30

    dirpath = os.getcwd()
    path = dirpath+"/"+place+"/"
    os.makedirs( path, 493 )
    
    filename = []
    with open('test.csv', 'r') as k:
        reader = csv.reader(k)
        for row in reader:
            filename.append({'no': row[0] ,'file': row[1], 'duration': int(row[2])})


    for x in range(1,lastdateofmonth+1):
        x = str(x)
        startdatetime = datetime.strptime( "2018/"+month+"/"+x+" 04:00:00", "%Y/%m/%d %H:%M:%S")
        stopdatetime = datetime.strptime( "2018/"+month+"/"+x+" 21:59:59", "%Y/%m/%d %H:%M:%S")
        
        with open(path +x+"_"+month+"_2018_"+place+".csv", "w", newline="") as f:
            fw = csv.writer(f)
            fw.writerow(["Type","Start time","End time","Content Type","Content Name"])

            while startdatetime < stopdatetime:

                for m in filename:
                    mfile = m['file'].strip()
                    enddatetime = startdatetime + timedelta(seconds=m['duration'])

                    sdatetime = datetime.strftime(startdatetime, "%Y/%m/%d %H:%M:%S" )
                    edatetime = datetime.strftime(enddatetime, "%Y/%m/%d %H:%M:%S" )
                    
                    fw.writerow(["Z=Video","S="+sdatetime,"E="+edatetime,"I=video","N="+mfile+".mp4"])

                    startdatetime = enddatetime             

dmk()
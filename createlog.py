import csv
import os, sys
from datetime import datetime
from datetime import timedelta

def dmk() :
    place = "DMK_DIR55_S1-6"
    month = "05"
    lastdateofmonth = 31

    dirpath = os.getcwd()
    path = dirpath+"/"+place+"/"
    os.makedirs( path, 493 )
    
    filename = []
    with open('test.csv', 'r') as k:
        reader = csv.reader(k)
        for row in reader:
            filename.append({'file': row[0], 'duration': int(row[1])})


    for x in range(1,lastdateofmonth+1):
        x = str(x)
        startdatetime = datetime.strptime( "2018/"+month+"/"+x+" 00:00:00", "%Y/%m/%d - %H:%M:%S")
        stopdatetime = datetime.strptime( "2018/"+month+"/"+x+" 23:59:59", "%Y/%m/%d - %H:%M:%S")
        
        with open(path+x+"_"+month+"_"+place+".csv", "w", newline="") as f:
            fw = csv.writer(f)
            fw.writerow(["Type","Start time","End time","Content Type","Content Name"])

            while startdatetime < stopdatetime:

                for m in filename:
                    enddatetime = startdatetime + timedelta(seconds=m['duration'])

                    sdatetime = datetime.strftime(startdatetime, "%Y/%m/%d - %H:%M:%S" )
                    edatetime = datetime.strftime(enddatetime, "%Y/%m/%d - %H:%M:%S" )
                    playtime = str(m['duration'])
                    
                    fw.writerow(["Z=Video","S="+sdatetime,"e="+edatetime,"I=video","N="+m['file']+"_V1-"+playtime+"s."+m['file']+".mp4"])

                    startdatetime = enddatetime             

dmk()
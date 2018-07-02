import csv
from datetime import datetime
from datetime import timedelta

def dmk() :
    place = "DMK_S1"
    month = "05"
    lastdateofmonth = 2
    
    filename = []
    with open('test.csv', 'r') as k:
        reader = csv.reader(k)
        for row in reader:
            filename.append({'file': row[0], 'duration': int(row[1])})


    for x in range(1,lastdateofmonth+1):
        x = str(x)
        startdatetime = datetime.strptime( x+"/"+month+"/06 - 00:00:00", "%d/%m/%y - %H:%M:%S")
        stopdatetime = datetime.strptime( x+"/"+month+"/06 - 23:59:59", "%d/%m/%y - %H:%M:%S")
        
        with open(x+"_"+month+"_"+place+".csv", "w", newline="") as f:
            fw = csv.writer(f)
            fw.writerow(["Type","Start time","End time","Content Type","Content Name"])

            while startdatetime < stopdatetime:

                for m in filename:
                    enddatetime = startdatetime + timedelta(seconds=m['duration'])

                    sdatetime = datetime.strftime(startdatetime, "%d/%m/%y - %H:%M:%S" )
                    edatetime = datetime.strftime(enddatetime, "%d/%m/%y - %H:%M:%S" )
                    
                    fw.writerow(["Z=Video","S="+sdatetime,"e="+edatetime,"I=video","N="+place+"/"+m['file']+".mp4"])

                    startdatetime = enddatetime             

dmk()
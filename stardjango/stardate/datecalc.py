from datetime import datetime

def calc(startdate,enddate):
    startdate = datetime.strptime(startdate,"%Y-%m-%d")
    enddate = datetime.strptime(enddate,"%Y-%m-%d")
    delta = enddate - startdate
    steps = delta.days
    return steps

if __name__ == '__main__':
    calc(startdate,enddate)

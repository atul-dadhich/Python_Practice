import sys
import subprocess
import time

arglen = len(sys.argv)

if arglen < 4:

    print "Please provide arguments [Usage]: [Username] [Host IP Address] [Interval in sec]""\n""Eg: $ python Monitor_Host.py centos 52.209.192.69 60"

else:

    """Host to Monitor"""
    host = sys.argv[1] + "@" + sys.argv[2]

    file_ = open(sys.argv[2] + ".txt", "w+")

    """Time Interval in Seconds"""
    interval = float(sys.argv[3])
    top5process = "ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%mem | head -6"
    topprocess = "ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%mem | head -6 |sed -n '1p' ; ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%mem | head -6 |sed -n '2p'"

    topprocessutilization = subprocess.Popen(["ssh", "-i", "centos.pem", host, topprocess], stdout=subprocess.PIPE)
    utilization = topprocessutilization.stdout.read()
    print "Process with Highest Resource Utilization is Mentioned Below, Refer Log File for rest""\n", utilization

    subprocess.call(["ssh", "-i", "centos.pem", host, "ps -ef | wc -l"], stdout=file_, shell=True)
    subprocess.call(["ssh", "-i", "centos.pem", host, top5process], stdout=file_, shell=True)

    processcount = subprocess.Popen(["ssh", "-i", "centos.pem", host, "ps -ef | wc -l"], stdout=subprocess.PIPE)
    countbefore = processcount.stdout.read()
    print "Total Number of Processes Running During Last Monitoring", countbefore

    time.sleep(interval)

    processcount1 = subprocess.Popen(["ssh", "-i", "centos.pem", host, "ps -ef | wc -l"], stdout=subprocess.PIPE)
    countafter = processcount1.stdout.read()
    print "Total Number of Processes Running Now", countafter

    if countbefore == countafter:
        print "No change in Process count"
    else:
        countchange = int(countafter) - int(countbefore)
        if countchange < 0:
            print "There is a Decrease in Process count by", abs(countchange)
        else:
            print "There is a Increase in Process count by", countchange
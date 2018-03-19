def hmsToSec(str_time):
    list_time = str_time.split(':')
    h = int(list_time[0])
    m = int(list_time[1])
    s = int(list_time[2])
    return 3600*h + 60*m + s

def secToHms(sec):
    h = sec // 3600
    m = (sec % 3600)//60
    s = (sec % 60)
    return str(h) + ":" + str(m) + ":"+ str(s)


time_sec = hmsToSec("1:32:45")
print(time_sec)
print(secToHms(time_sec))
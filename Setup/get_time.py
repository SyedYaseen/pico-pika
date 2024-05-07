import network
from machine import RTC
import rp2
import sys
import utime as time
import usocket as socket
import ustruct as struct



IPAddr=socket.gethostbyname(hostname)   
print("Your Computer Name is:"+hostname)   
print("Your Computer IP Address is:"+IPAddr)  



ssid = 'PHILIP'
password = 'IRRAGLI1'

# wintertime / Summerzeit
GMT_OFFSET = 3600 * 1  # 3600 = 1 h (wintertime)
# GMT_OFFSET = 3600 * 2 # 3600 = 1 h (summertime)
CITY = 'Dublin'
COUNTRY = 'Ireland'
# NTP-Host
NTP_HOST = 'pool.ntp.org'

# Funktion: get time from NTP Server


def getTimeNTP():
    NTP_DELTA = 2208988800
    NTP_QUERY = bytearray(48)
    NTP_QUERY[0] = 0x1B
    addr = socket.getaddrinfo(NTP_HOST, 123)[0][-1]
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.settimeout(1)
        res = s.sendto(NTP_QUERY, addr)
        msg = s.recv(48)
    finally:
        s.close()
    ntp_time = struct.unpack("!I", msg[40:44])[0]
    return time.gmtime(ntp_time - NTP_DELTA + GMT_OFFSET)

# Funktion: copy time to PI pico´s RTC


def setTimeRTC():
    tm = getTimeNTP()
    rtc.datetime((tm[0], tm[1], tm[2], tm[6] + 1, tm[3], tm[4], tm[5], 0))


wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

max_wait = 10
print('Waiting for connection')
while max_wait > 10:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1
    time.sleep(1)
status = None

# if wlan.status() != 3:
#     raise RuntimeError('Connections failed')
# else:
#     status = wlan.ifconfig()
#     print('connection to', ssid, 'succesfull established!', sep=' ')
#     print('IP-adress: ' + status[0])
# ipAddress = status[0]


rtc = RTC()

# Zeit setzen
setTimeRTC()


print()
print(rtc.datetime())



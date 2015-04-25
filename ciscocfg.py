import telnetlib
import getpass
from thread import start_new
ip=[]
for i in range(StartIP,EndIP,1):    #Create The IPs to connect
    ip.append("xx.xx.xx."+str(i))
password = "MY_PASS"
def sw_con(ipaddr):
    try:
        tn = telnetlib.Telnet(ipaddr)
        if tn :
            tn.write (password + "\n")
            print(tn.read_until(">")),
            tn.write("enable\n")
            print(tn.read_until("Password:")),
            tn.write(password + "\n")
            print(tn.read_until("#")),
            tn.write("conf t\n")
            print(tn.read_until("#")),
            tn.write("int ran gi 0/1 - 2\n")
            print(tn.read_until("#")),
            tn.write("sw mo t\n")
            print(tn.read_until("#")),
            tn.write("exit\n")
            print(tn.read_until("#")),
            tn.write("exit\n")
            print(tn.read_until("#")),
            tn.write("wr\n")
            print(tn.read_until("#")),
            tn.write("logout\n")
            print(tn.read_until(">")),
            tn.close()
    except:
        print "\nFailed connecting to  "+ipaddr

for ipaddr in ip:
    start_new(sw_con,(ipaddr)) # for connecting to all devices at same time!


import os
import subprocess

goodPing = "1 received"

os.chdir("/home/vagrant/lingi2142")
#subprocess.call(["sudo","./create_network.sh","project_topo"])
t=subprocess.Popen("ls",stdout=subprocess.PIPE)
print(t.communicate())
locations = ["SH1C","HALL","PYTH","STEV","CARN","MICH"]

prefixA = "fd00:3:0f"

print("--Start ping--")

for loc in locations :
    with open("test/list_ip.txt") as list :
        ip = list.readline()
    	print("----------------------------"+loc+"-------------------------------")
        while ip:
            p = subprocess.Popen("sudo test/ping.sh %s %s" % (loc, ip), stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE, shell=True)
            output, err = p.communicate()
            if (output.find(goodPing)==-1): print(loc+" ---> " +ip)
            ip = list.readline()
            #res = subprocess.Popen(["sudo ip netns exec "+loc+" ping6 "+ ip+ " -c 1 -n -W 1 -q"],
            #             shell=True)
            #res = subprocess.Popen("sudo ip netns exec %s ping6 %s -c 1 -n -W 1" % (loc,ip),  stdout=subprocess.PIPE,
            #             stderr=subprocess.PIPE,shell=True)
            #output,error = res.communicate()
            #output = res.stdout.decode("utf-8")
            #output = subprocess.check_output(["sudo ip netns exec "+loc+" ping6 "+ ip+ " -c 1 -n -W 1 -q"])
            #if (output.find(gPing)==-1) : print(ip+error)
            #else : print("OK")
            #ip = list.readline()
        #    ip = prefixA+str(i)+str(j)+"::"+str(j)
        #    res = subprocess.Popen("ip netns exec %s ping6 %s -c 1 -n -W 1" % (loc,ip), stdout=subprocess.PIPE,
        #                 stderr=subprocess.PIPE, shell=True)
        #    output,error = res.communicate()
        #    if (output.find(gPing)==-1) : print(ip)

#subprocess.call(["sudo","./cleanup.sh"])

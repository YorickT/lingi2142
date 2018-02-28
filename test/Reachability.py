
import os
import subprocess

gPing = "1 recieved"

os.chdir("..")

#subprocess.call(["sudo","./create_network.sh","project_topo"])

locations = ["SH1C","HALL","PYTH","STEV","CARN","MICH"]

prefixA = "fd00:3:0f"

print("--Start ping--")

for loc in locations :
    with open("lingi2142/test/list_ip.txt") as list :
        ip = list.readline()
    	print(loc)
        while ip:
            #res = subprocess.Popen("sudo ip netns exec %s ping6 %s -c 1 -n -W 1" % (loc,ip), stdout=subprocess.PIPE,
            #             stderr=subprocess.PIPE,shell=True)
            #output,error = res.communicate()
            #output = res.stdout.decode("utf-8")
            output = subprocess.check_output("sudo ip netns exec %s ping6 %s -c 1 -n -W 1" % (loc,ip))
            if (output.find(gPing)==-1) : print(ip+error)
            #else : print("OK" + error)
            ip = list.readline()
        #    ip = prefixA+str(i)+str(j)+"::"+str(j)
        #    res = subprocess.Popen("ip netns exec %s ping6 %s -c 1 -n -W 1" % (loc,ip), stdout=subprocess.PIPE,
        #                 stderr=subprocess.PIPE, shell=True)
        #    output,error = res.communicate()
        #    if (output.find(gPing)==-1) : print(ip)

#subprocess.call(["sudo","./cleanup.sh"])

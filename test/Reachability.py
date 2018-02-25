
import os
import subprocess

os.chdir("..")
out = os.Popen('ls')
o = out.read()
print(o)

call(["sudo","./create_network.sh","project_topo"])

locations = ["SH1C","HALL","PYTH","STEV","CARN","MICH"]

prefixA = "fd00:3:0f"

for loc in location :
    call(["sudo","./connect_to.sh","project_cfg/",loc])

    for i in range(1,7) :
        for j in range(1,7):

#            call(["ping6",prefixA+str(i)+str(j)+"::"+str(i),"-c","1"])
#            call(["ping6",prefixA+str(i)+str(j)+"::"+str(j),"-c","1"])

            ip = prefixA+str(i)+str(j)+"::"+str(i)
            res = subprocess.Popen("ping6 %s -c 1 -n -W 1" % (host, command), stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE, shell=True)
            if (res.returncode) : print(ip)

            ip = prefixA+str(i)+str(j)+"::"+str(j)
            res = subprocess.Popen("ping6 %s -c 1 -n -W 1" % (host, command), stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE, shell=True)
            if (res.returncode) : print(ip)

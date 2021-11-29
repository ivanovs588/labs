import os, re
import threading
import random
import time
import sys

def thread_ip():
    with lock: 
    
        global suffix
        old_suffix = suffix
        ip = "192.168.178." + str(suffix)
        suffix = old_suffix + 1
        ping_out = os.popen("ping -q -c2 " + ip, "r")  
        print("... pinging ", ip)
        while True:
            line = ping_out.readline()
            if not line:
                break
            n_received = received_packages.findall(line)
            if n_received:
                print(ip + ": " + status[int(n_received[0])])
    


lock = threading.Lock()
suffix = 20
received_packages = re.compile(r"(\d) received")
status = ("no response", "alive but losses", "alive")
threads = [threading.Thread(target=thread_ip) for _ in range(20,30)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

import os, subprocess, signal, time

print("[+] started api server, web server, scraper, database loader, graph loader, download loader") 
a = subprocess.Popen("cd ./DataBase/inventory; python cron.py", shell=True, stdout=subprocess.PIPE)
b = subprocess.Popen("python ./FlaskApp/server.py", shell=True, stdout=subprocess.PIPE)
c = subprocess.Popen("cd DataBase; uvicorn api:app", shell=True, stdout=subprocess.PIPE)

print "\n"
while True:
    com = raw_input("enter end to term all processes> ")
    if (com == "end"):
        os.killpg(os.getpgid(a.pid), signal.SIGTERM)
        os.killpg(os.getpgid(b.pid), signal.SIGTERM)
        os.killpg(os.getpgid(c.pid), signal.SIGTERM)
        break
time.sleep(1)

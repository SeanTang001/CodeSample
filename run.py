import os, subprocess, signal, time

os.system("mkdir ./FlaskApp/static/safeway/")
os.system("mkdir ./FlaskApp/static/target/")
os.system("mkdir ./FlaskApp/static/walmart/")
print("[+] started api server, web server, scraper, database loader, graph loader, download loader") 
a = subprocess.Popen("cd ./DataBase/inventory; python2 cron.py", shell=True)
b = subprocess.Popen("python2 ./FlaskApp/server.py", shell=True)
c = subprocess.Popen("cd DataBase; uvicorn api:app", shell=True)

print "\n"
while True:
    com = raw_input("enter end to term all processes> ")
    if (com == "end"):
        os.killpg(os.getpgid(a.pid), signal.SIGTERM)
        os.killpg(os.getpgid(b.pid), signal.SIGTERM)
        os.killpg(os.getpgid(c.pid), signal.SIGTERM)
        break
time.sleep(1)

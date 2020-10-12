import os
x = os.system("ls")
print x
import time
import db_loader, inventory, graph_loader, download_loader

#run ../inventory/load_db every 1 hr

counter = 0
while True:

    res = inventory.main()
    db_loader.db_load(res)
    download_loader.download_load()
    graph_loader.graph_load()

    if (counter == 24):
        graph_loader.addDate()
        counter = 0

    counter = counter + 1
    time.sleep(60*60)
# Schedules job_function to be run once each minute
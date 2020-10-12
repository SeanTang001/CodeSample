import os
import time
import db_loader, inventory, graph_loader

#run ../inventory/load_db every 1 hr
counter = 0
while True:
    res = inventory.main()
    db_loader.parse_by_store(res)
    db_loader.parse_by_type(res)
    
    if (counter = 24):
        graph_loader.addDate()
        counter = 0

    counter = counter + 1
    time.sleep(60*60)
# Schedules job_function to be run once each minute
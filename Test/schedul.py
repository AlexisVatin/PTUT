import schedule
import time

def todo():
    print ("Hello")

schedule.every().day.at("12:00").do(todo())
schedule.every().day.at("18:00").do(todo())
schedule.every().day.at("19:45").do(todo())

while True :
    schedule.run_pending()
    time.sleep(1)
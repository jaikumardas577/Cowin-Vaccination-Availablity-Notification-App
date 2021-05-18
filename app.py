#  importing Libraries
from colorama import init
init()
from cowin_api import CoWinAPI
from fake_useragent import UserAgent
import datetime
import os
import sys
from twilio.rest import Client
import pdb
import json
from tabulate import tabulate
from terminaltables import AsciiTable
from colorama import Fore, Back, Style
import requests
import time
import atexit
from flask import Flask
from flask_apscheduler import APScheduler
from apscheduler.schedulers.background import BackgroundScheduler


class Config:
    SCHEDULER_API_ENABLED = True
    JOBS = [
    {
        "id": "job1",
        "func": "app:getSlotDetailsByPin",
        "args": ("782103","14-05-2021",18),
        "trigger": "interval",
        "seconds": 50,
    },
        {
        "id": "job2",
        "func": "app:getSlotDetailsByPin",
        "args": ("786001","14-05-2021",18),
        "trigger": "interval",
        "seconds": 50,
    }
    ]


cowin = CoWinAPI()
recipients = {
"phone_number_list" : {"782103": ["8638151279","8638787934","8472832644","8622422198"],"786001":["8472832644"]},
"whatsapp_number_list":{"782103":["8402063413","8638787934","8812914584","8472832644"],"786001":["8472832644"]}
}
with open('config.json') as f:
  config  = json.load(f)


with open('district.json') as f:
  district_json  = json.load(f)



def genererate_template(age,name,district,block_name,dates,slots,pin):
    template_message  = f"Over Age {age} years , Slot for district {district} is available at block {block_name} pin No. {pin} in {name} ; date {dates}. slots are {slots}"
    return template_message


def genererate_template_pin(age,name,district,block_name,start_time,end_time,pin,date):
    template_message  = f"Hi Billa, Over Age {age} years , Slot for district {district} is available at block {block_name} pin No. {pin} in {name} ; from {start_time} to {end_time}.Date {date}"
    return template_message


def sent_text_message(config,recipeint_number,age,name,district,block_name,dates,slots,pin,template_message):

    account_sid = config['TWILIO_ACCOUNT_SID']
    auth_token = config['TWILIO_AUTH_TOKEN']

    client = Client(account_sid, auth_token)

    client.api.account.messages.create(
    to=f"+91{recipeint_number}",
    from_="+19195900206",
    body=template_message)
    return 1

def sent_whatapp_message(config,recipeint_whatsapp_number,age,name,district,block_name,dates,slots,pin,template_message):

    account_sid = config['TWILIO_ACCOUNT_SID']
    auth_token = config['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)
    from_whatsapp_number='whatsapp:+14155238886'
    to_whatsapp_number=f'whatsapp:+91{recipeint_whatsapp_number}'

    client.messages.create(body=template_message,
                        from_=from_whatsapp_number,
                        to=to_whatsapp_number)
    return 1


def getDatesAndSlots(cowin_response):
    __ = [d_["date"] for d_ in cowin_response["sessions"]]
    dates = ",".join(__)
    slots_ = [d_["slots"] for d_ in cowin_response["sessions"]]
    slots = ",".join(slots_[0])
    return (dates,slots)


def getDatesAndSlotsSession(sessions_response):
    dates,slots_ = sessions_response["date"],",".join(sessions_response["slots"])
    return (dates,slots_)

def getSlotDetailsByPin(pin_no,date,min_age_limit = 45):
    user_agent = UserAgent()
    headers = {'User-Agent': user_agent.random}
    URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={}&date={}".format(pin_no, date)
    available_centers =  json.loads(requests.get(URL,headers = headers).text)
    print(available_centers)
    if len(available_centers["sessions"]) < 1:
        print(f"Slots not available for date {date} at pin no {pin_no}")
        return 0
    else:
        for _ in available_centers["sessions"]:
            if  _["min_age_limit"] != min_age_limit:
                continue
            (start_time,end_time) = _["to"],_["from"]
            row = [[_["name"]],[_["district_name"]],[_["pincode"]],[_["block_name"]],start_time,end_time,[_["pincode"]]]
            print(tabulate(row))
            age,name,district,block_name,dates,slots,pin = _["min_age_limit"], _["name"], _["district_name"], _["block_name"], start_time,end_time, _["pincode"]
            print(Fore.GREEN + Style.DIM + genererate_template_pin(age,name,district,block_name,start_time,end_time,pin,date))
            template_message = genererate_template_pin(age,name,district,block_name,start_time,end_time,pin,date)
            print(Style.RESET_ALL)
            # Sending SMS 
            for number in recipients["phone_number_list"][pin]:
                sent_text_message(config,number,age,name,district,block_name,dates,slots,pin,template_message)
            for num in recipients["whatsapp_number_list"][pin]:
                sent_whatapp_message(config,num,age,name,district,block_name,dates,slots,pin,template_message)
            # sent_text_message(config,"8472832644",age,name,district,block_name,dates,slots,pin,template_message)
            # sent_whatapp_message(config,"8472832644",age,name,district,block_name,dates,slots,pin,template_message)
        return 1


def getSlotDetailsByDistrictId(district_name,date,min_age_limit = 45):
    if district_name not in district_json[0].keys():
        print(f"Invalid District Name. Available district are {','.join(list(district_json[0].keys()))}")
        return 0
    district_id = district_json[0][district_name]
    available_centers = cowin.get_availability_by_district(district_id, date, min_age_limit)
    if len(available_centers["centers"]) < 1:
        print(f"Slots not available for date {date} at district id for minimum age {min_age_limit}, {district_name}")
        return 0
    else:
        for _ in available_centers["centers"]:
            for session in _["sessions"]:
                print(session)
                if  session["min_age_limit"]!= min_age_limit:
                    continue 
                else:
                    (dates,slots) =getDatesAndSlotsSession(session)
                    row = [[_["name"]],[_["district_name"]],[_["pincode"]],[_["block_name"]],[dates],[slots],[_["pincode"]]]
                    print(tabulate(row))
                    age,name,district,block_name,dates,slots,pin = session["min_age_limit"], _["name"], _["district_name"], _["block_name"], dates,slots, _["pincode"]
                    print(Fore.GREEN + Style.DIM + genererate_template(age,name,district,block_name,dates,slots,pin))
                    template_message = genererate_template(age,name,district,block_name,dates,slots,pin)
                    print(Style.RESET_ALL)
                    # sent_text_message(config,"8472832644",age,name,district,block_name,dates,slots,pin,template_message)
                    # sent_whatapp_message(config,"8472832644",age,name,district,block_name,dates,slots,pin,template_message)         
        return 1

numdays = 7
base = datetime.datetime.today()
date_list = [base + datetime.timedelta(days=x) for x in range(numdays)]
date_str = [x.strftime("%d-%m-%Y") for x in date_list]




print(date_str)
state_id = 4  # for Assam

# getSlotDetailsByPin("782103",date_str[0],45)
# getSlotDetailsByDistrictId("Nagaon",date_str[0],min_age_limit = 18)
# districts = cowin.get_districts(state_id)



# Shut down the scheduler when exiting the app
# atexit.register(lambda: scheduler.shutdown())

if __name__ == "__main__":
    app = Flask(__name__)
    app.config.from_object(Config())
    scheduler = APScheduler()
    # scheduler.add_job(func=getSlotDetailsByPin, trigger="interval", seconds=60)
    scheduler.init_app(app)
    scheduler.start()
    app.run()








import json
import requests
from telebot import TeleBot,types,util
from telebot.types import InlineKeyboardMarkup,InlineKeyboardButton
from telebot.util import user_link

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.9,de;q=0.8,ru;q=0.7,am;q=0.6',
    'Access-Control-Allow-Credentials': 'true',
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJKV1RfQ1VSUkVOVF9VU0VSIjoiQW5vbnltb3VzQGV0aGlvcGlhbmFpcmxpbmVzLmNvbSIsIm5iZiI6MTcwNzk3NTA2MSwiZXhwIjoxNzE4MzQzMDYxLCJpYXQiOjE3MDc5NzUwNjF9.aquS-r53e1mTyr_CFhiSFks6kyNwTnItblMc6pin6_E',
    'Connection': 'keep-alive',
    'Origin': 'https://www.ethiopianpassportservices.gov.et',
    'Referer': 'https://www.ethiopianpassportservices.gov.et/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

BOT_TOKEN = "<YOU API>"
bot = TeleBot(BOT_TOKEN,parse_mode="HTML")

button = InlineKeyboardMarkup()
group = InlineKeyboardButton(text="Group",url="t.me/neuralg")
channel = InlineKeyboardButton(text="Channel",url="t.me/neuralp")
button.add(group,channel)


@bot.message_handler(commands=["start"])
def startMsg(msg):
    user = msg.from_user
    bot.reply_to(msg,f"Hey {user_link(user)} Send me Application number that starts with a letter\'M'.",reply_markup=button)

@bot.message_handler(func=lambda m:True)
def checkPassportStatus(msg):
    userMsg = msg.text

    try:
        params = {
            'applicationNumber': userMsg,
        }

        response = requests.get(
            'https://epassportservicesaddt.azurewebsites.net/Request/api/V1.0/Request/GetRequestsByApplicationNumber',
            params=params,
            headers=headers,
        )

        data = json.loads(response.text)
        #print(data)
        # return the application number 
        applicationNumber = data["serviceRequest"]["personResponses"]["applicationNumber"]
        # return the person's first name 
        firstName = data["serviceRequest"]["personResponses"]["firstName"]
        # return the person's father name
        middleName = data["serviceRequest"]["personResponses"]["middleName"]
        # return the person's grand pa's name huh
        lastName = data["serviceRequest"]["personResponses"]["lastName"]
        # return the payments status
        paymentStatus = data["serviceRequest"]["requestStatus"]
        # return whether it's paid or not
        isPaid = data["serviceRequest"]["personResponses"]["personStatus"]

        # return the passport's page
        passportPage = data["serviceRequest"]["personResponses"]["passportRes"]["passportPage"]
        # return the appointment date
        appointmentDate = data["serviceRequest"]["appointmentResponse"]["date"]
        # return the appointment office
        appointmentOffice = data["serviceRequest"]["office"]
        # return the delivery date
        deliveryDate = data["serviceRequest"]["deliveryDateDisplay"]
        # return the passport delivery site or place
        deliverySite = data["serviceRequest"]["deliverySite"]

        beautify = "*"
        userData = f"""\nApplication number: <code>{applicationNumber}</code>\nFull Name: <b>{firstName} {middleName} {lastName}</b>  {beautify*50}\nPayment Status:{paymentStatus}<b> {isPaid} </b> \nPassport page: {passportPage}\nAppointment date: <b>{appointmentDate} GC\nAppointment place:</b> {appointmentOffice}\nDelivery date: {deliveryDate} GC \nDelivery site/place: {deliverySite} {beautify*50}"""
        bot.send_message(msg.chat.id,userData,reply_markup=button,parse_mode="HTML")

    except Exception as e:
        bot.reply_to(msg,text="Something went wrong!",reply_markup=button)


bot.infinity_polling()


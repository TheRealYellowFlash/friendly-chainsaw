import telebot
import requests
import re

bot = telebot.TeleBot('5356567096:AAEVmMFaeBGQXx4ayiao-ba1yA3AwDPabmo')

def extract_arg(arg):
    return arg.split()[1:]

@bot.message_handler(commands=['gd'])
def gdtot(message):
    link = extract_arg(message.text)
    gdlink = gdtot_new(link[0])
    bot.reply_to(message,gdlink)
    
def gdtot_new(url):
    url = url.replace('https://new7.gdtot.cfd/file/','https://new7.gdtot.cfd/ddl/')
    response = requests.get('https://new7.gdtot.cfd/ddl/8712629207')
    gdrive_link = re.findall(r'https:\/\/drive.google.com\/u\/0\/uc\?id\=[a-zA-Z1-90_&=-]+',response.text)[0]
    return gdrive_link

bot.infinity_polling(timeout=10, long_polling_timeout = 5)

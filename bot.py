from telegram.ext import Updater, CommandHandler
import requests


url = 'YOUR-URL-HERE/GET'
data = requests.get(url) # requests data from API
data = data.json() # converts return data to json

# Retrieve values from API
curr_temp = data['curr_temp']
cad_rate = data['usd_rates']['CAD']
eur_rate = data['usd_rates']['EUR']
zar_rate = data['usd_rates']['ZAR']


def r_saludo():
    return "hola"

def r_napias():
    return "Napias cabron"

def r_version():
    return "1.0.0"

def saludo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=r_saludo())

def napias(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=r_napias())

def version(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=r_version())

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Hi! I respond to /napias or /version or /saludo. Try these!')

def main():
    import os
    TOKEN = os.getenv('BOTAPIKEY')
    
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    handler_saludo = CommandHandler('saludo', saludo)
    handler_version = CommandHandler('version', version)
    handler_napias = CommandHandler('napias', napias)
    start_handler = CommandHandler('start',start)

    dispatcher.add_handler(handler_saludo)
    dispatcher.add_handler(handler_version)
    dispatcher.add_handler(handler_napias)
    dispatcher.add_handler(start_handler)

    PORT = int(os.environ.get('PORT', '443'))
    HOOK_URL = 'YOUR-CODECAPSULES-URL-HERE' + '/' + TOKEN
    updater.start_webhook(listen='0.0.0.0', port=PORT, url_path=TOKEN, webhook_url=HOOK_URL)
    updater.idle()

if __name__ == '__main__':
    main()

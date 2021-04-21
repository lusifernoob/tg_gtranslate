from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext,Filters,MessageHandler
from google_trans_new import google_translator 

updater = Updater('your bot token',use_context = True )

def key1():
  keyboard = [InlineKeyboardButton("Join Telegram channel", url='https://t.me/OMG_info')],[
            InlineKeyboardButton("creator ", url='https://t.me/shado_hackers')]
  return keyboard         
  
def start(updater,context):
   msg_id = updater.effective_message.message_id
   keyboard = key1()
   reply_markup = InlineKeyboardMarkup(keyboard)
   context.bot.send_message(updater.effective_message.chat_id,text='''👋 hello IAM Google Translater bot 
I can translate any language to you selected language😜
Made with love by @OMG_info ''',reply_to_message_id=msg_id,reply_markup=reply_markup)

def key2():
 keyboard = [
        [
            InlineKeyboardButton("हिंदी", callback_data='hi'),
            InlineKeyboardButton("ಕನ್ನಡ", callback_data='kn'),
            InlineKeyboardButton("ગુજરાતી",callback_data ='gu')
        ],
        [   InlineKeyboardButton("বাংলা", callback_data='bn'),
        InlineKeyboardButton("മലയാളം", callback_data='ml'),
        InlineKeyboardButton("English",callback_data = 'en')
        ],
    ]
 return keyboard
 
def echo(updater,context):
 msg_id= updater.effective_message.message_id
 chat_id = updater.effective_message.chat_id
 keyboard = key2()
 usr_msg = updater.effective_message.text
 reply_markup = InlineKeyboardMarkup(keyboard)
 context.bot.send_message( chat_id = chat_id,text=usr_msg,reply_to_message_id=msg_id,reply_markup=reply_markup)
 
  
def button(updater,context):
    query = updater.callback_query
    sel_data = f'{query.data}'
    query.answer()
    texted=updater.effective_message.text
    translator=google_translator()
    translate_text=translator.translate(texted,lang_tgt=sel_data)
    query.edit_message_text(translate_text)
 
dp =updater.dispatcher.add_handler
dp(CommandHandler('start',start))
dp(MessageHandler(Filters.text,echo))
dp(CallbackQueryHandler(button))

updater.start_polling()
updater.idle()

import sqlite3

from telegram.ext import (Updater, CommandHandler, MessageHandler, ConversationHandler, Filters)
from sold_loads import city1_name, city2_name, time1, time2, notes
from users_list import (t_list, f_list, a_list, n_list, sirdarya_users, jizzakh_users, samarkand_users, bukhara_users,
                        navoi_users, kashkadarya_users, surkhandarya_users, xorezm_users, karakalpak_users)
from buttons import load_buttons, button_to_back


def search_loads(update, context):
    update.message.reply_text(text="Quyidagi knopkalardan birini tanlang", reply_markup=load_buttons)
    text = update.message.text
    user_id = update.message.from_user.id
    if text == "Ortga":
        if user_id in t_list:
            t_list.remove(user_id)
        elif user_id in a_list:
            a_list.remove(user_id)
        elif user_id in f_list:
            f_list.remove(user_id)


def Tashkent_loads(update, context):
    update.message.reply_text('Endi men sizga Toshkent dagi yuklarni yuborib turaman 😊',
                              reply_markup=button_to_back)
    t_list.add(update.message.from_user.id)
    print(t_list)


def Andijan_loads(update, context):
    update.message.reply_text('Endi men sizga Andijon dagi yuklarni yuborib turaman 😊',
                              reply_markup=button_to_back)
    a_list.add(update.message.from_user.id)
    print(a_list)


def Ferghana_loads(update, context):
    update.message.reply_text('Endi men sizga Farg\'ona dagi yuklarni yuborib turaman 😊',
                              reply_markup=button_to_back)
    f_list.add(update.message.from_user.id)
    print(f_list)

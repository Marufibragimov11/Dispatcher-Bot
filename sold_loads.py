from telegram.ext import (Updater, CommandHandler, MessageHandler, ConversationHandler, Filters)
from buttons import back_button
from users_list import (t_list, f_list, a_list, n_list, sirdarya_users, jizzakh_users, samarkand_users, bukhara_users,
                        navoi_users, kashkadarya_users, surkhandarya_users, xorezm_users, karakalpak_users)


def start_conversation(update, text):
    update.message.reply_text(text="Qaysi shaxardan yukni olish kerak🏬")
    return 1


def pu_city(update, context):
    global PickUp_city
    PickUp_city = update.message.text
    update.message.reply_text(text="Qaysi shaxarga yukni yetkazish kerak🏬")
    return 2


def del_city(update, context):
    global del_cities
    del_cities = update.message.text
    update.message.reply_text(text="Qaysi vaqtda yukni olish kerak⏰ \n"
                                   "kun/oy/yil formatida yozing \n"
                                   "Misol: 31.12.2022")
    return 3


def pu_time(update, context):
    global time_to_pu
    time_to_pu = update.message.text
    update.message.reply_text(text="Qaysi vaqtda yukni yetkazish kerak⏰ \n"
                                   "kun/oy/yil formatida yozing \n"
                                   "Misol: 31.12.2022"
                              )
    return 4


def del_time(update, context):
    global time_to_del
    time_to_del = update.message.text
    update.message.reply_text(text="🚚 Kerakli yuk mashinasinini kiriting")
    return 5


def truck(update, context):
    global truck_type
    truck_type = update.message.text
    update.message.reply_text(text="📋Qo'shimcha ma'lumotlarni va telefon raqamingizni yozib qoldiring")
    return 6


def note(update, context):
    global notebook
    user = update.message.chat.username
    notebook = update.message.text
    update.message.reply_text(f"Ma'lumotlaringizni tekshiring va to'g'riligini tasdiqlang✅ \n"
                              f"\n🏬Yuk olinadigan manzil: *{PickUp_city}* \n"
                              f"\n⏰Yuk olish vaqti: *{time_to_pu}* \n"
                              f"\n🏬Yukni yetkazib berish manzili: *{del_cities}* \n"
                              f"\n⏰Yukni yetkazib berish vaqti: *{time_to_del}* \n"
                              f"\n🚚Kerakli yuk mashinasi: {truck_type}"
                              f"\n📋Yuk oluvchi uchun qo'shimcha ma'lumotlar: *{notebook}*",
                              parse_mode="Markdown",
                              reply_markup=back_button)
    if PickUp_city == "Toshkent":
        for tst in t_list:
            update.message.bot.send_message(chat_id=tst,
                                            text=f"\n🏬Yuk olinadigan manzil: *{PickUp_city}* \n"
                                                 f"\n⏰Yuk olish vaqti: *{time_to_pu}* \n"
                                                 f"\n🏬Yukni yetkazib berish manzili: *{del_cities}* \n"
                                                 f"\n⏰Yukni yetkazib berish vaqti: *{time_to_del}* \n"
                                                 f"\n🚚Kerakli yuk mashinasi: {truck_type} \n"
                                                 f"\n📋Yuk oluvchi uchun qo'shimcha ma'lumotlar: *{notebook}* \n"
                                                 f"\n👤Yuk sotuvchining telegram username: {user}",
                                            parse_mode="Markdown")
    elif PickUp_city == "Andijon":
        for ast in a_list:
            update.message.bot.send_message(chat_id=ast,
                                            text=f"\n🏬Yuk olinadigan manzil: *{PickUp_city}* \n"
                                                 f"\n⏰Yuk olish vaqti: *{time_to_pu}* \n"
                                                 f"\n🏬Yukni yetkazib berish manzili: *{del_cities}* \n"
                                                 f"\n⏰Yukni yetkazib berish vaqti: *{time_to_del}* \n"
                                                 f"\n🚚Kerakli yuk mashinasi: {truck_type} \n"
                                                 f"\n📋Yuk oluvchi uchun qo'shimcha ma'lumotlar: *{notebook}*",
                                            parse_mode="Markdown")
    elif PickUp_city == "Farg'ona":
        for fst in f_list:
            update.message.bot.send_message(chat_id=fst,
                                            text=f"\n🏬Yuk olinadigan manzil: *{PickUp_city}* \n"
                                                 f"\n⏰Yuk olish vaqti: *{time_to_pu}* \n"
                                                 f"\n🏬Yukni yetkazib berish manzili: *{del_cities}* \n"
                                                 f"\n⏰Yukni yetkazib berish vaqti: *{time_to_del}* \n"
                                                 f"\n🚚Kerakli yuk mashinasi: {truck_type} \n"
                                                 f"\n📋Yuk oluvchi uchun qo'shimcha ma'lumotlar: *{notebook}*",
                                            parse_mode="Markdown")

    return ConversationHandler.END

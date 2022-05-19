from telegram import ReplyKeyboardRemove
from telegram.ext import (Updater, CommandHandler, MessageHandler, ConversationHandler, Filters)
from buttons import back_button, city_buttons, main_menu
from users_list import (t_list, f_list, a_list, n_list, sirdarya_users, jizzakh_users, samarkand_users, bukhara_users,
                        navoi_users, kashkadarya_users, surkhandarya_users, xorezm_users, karakalpak_users)


def start_conversation(update, text):
    update.message.reply_text(text="*Qaysi davlat yoki shaxardan yukni olish kerak*🧐",
                              parse_mode="Markdown",
                              reply_markup=city_buttons)
    return 1


def pu_location(update, context):
    global pick_location
    pick_location = update.message.text
    update.message.reply_text(text=f"*{pick_location}ning aynan qaysi tumanidan yoki shaxaridan yukni olish kerak*🧐",
                              parse_mode="Markdown",
                              reply_markup=ReplyKeyboardRemove())
    return 2


def pu_city(update, context):
    global PickUp_city
    PickUp_city = update.message.text
    update.message.reply_text(text="*Qaysi davlat yoki shaxarga yukni yetkazish kerak*🧐",
                              parse_mode="Markdown",
                              reply_markup=city_buttons)
    return 3


def del_location(update, context):
    global delivery_location
    delivery_location = update.message.text
    update.message.reply_text(
        text=f"*{delivery_location}ning aynan qaysi tumaniga yoki shaxariga yukni yetkazish kerak*🧐",
        parse_mode="Markdown",
        reply_markup=ReplyKeyboardRemove())
    return 4


def del_city(update, context):
    global del_cities
    del_cities = update.message.text
    update.message.reply_text(text="*Qaysi vaqtda yukni olish kerak*🧐 \n"
                                   "kun/oy/yil formatida yozing \n"
                                   "Misol: 31.12.2022",
                              parse_mode="Markdown")
    return 5


def pu_time(update, context):
    global time_to_pu
    time_to_pu = update.message.text
    update.message.reply_text(text="*Qaysi vaqtda yukni yetkazish kerak*🧐 \n"
                                   "kun/oy/yil formatida yozing \n"
                                   "Misol: 31.12.2022",
                              parse_mode="Markdown")
    return 6


def del_time(update, context):
    global time_to_del
    time_to_del = update.message.text
    update.message.reply_text(text="*Kerakli yuk mashinasinini kiriting*🚚",
                              parse_mode="Markdown")
    return 7


def truck(update, context):
    global truck_type
    truck_type = update.message.text
    update.message.reply_text(text="*Qo'shimcha ma'lumotlarni va telefon raqamingizni yozib qoldiring*📋",
                              parse_mode="Markdown")
    return 8


def note(update, context):
    global notebook
    global user
    user = update.message.chat.username
    notebook = update.message.text
    update.message.reply_text(f"Ma'lumotlaringizni tekshiring va to'g'riligini tasdiqlang✅ \n"
                              f"\n📌Yuk olinadigan manzil: *{pick_location} - {PickUp_city}* \n"
                              f"🕘Yuk olish vaqti: *{time_to_pu}* \n"
                              f"\n📌Yukni yetkazib berish manzili: *{delivery_location} - {del_cities}* \n"
                              f"🕘Yukni yetkazib berish vaqti: *{time_to_del}* \n"
                              f"\n🚚Kerakli yuk mashinasi: {truck_type} \n"
                              f"\n📋Yuk oluvchi uchun qo'shimcha ma'lumotlar: *{notebook}*",
                              parse_mode="Markdown",
                              reply_markup=back_button)
    return 9


def submit(update, context):
    update.message.reply_text(text=f"*Sizning postingiz {PickUp_city}dagi haydovchilarga yuborildi😉* \n",
                              parse_mode="Markdown",
                              reply_markup=main_menu)
    return ConversationHandler.END

    # if pick_location == "🇺🇿Toshkent":
    #     update.message.bot.send_message(chat_id=t_list,
    #                                     text=f"\n📌Yuk olinadigan manzil: *{pick_location} - {PickUp_city}* \n"
    #                                          f"🕘Yuk olish vaqti: *{time_to_pu}* \n"
    #                                          f"\n📌Yukni yetkazib berish manzili: *{delivery_location} - {del_cities}* \n"
    #                                          f"🕘Yukni yetkazib berish vaqti: *{time_to_del}* \n"
    #                                          f"\n🚚Kerakli yuk mashinasi: {truck_type} \n"
    #                                          f"\n📋Yuk oluvchi uchun qo'shimcha ma'lumotlar: *{notebook}* \n"
    #                                          f"\n👤Yuk sotuvchining telegram username: {user}",
    #                                     parse_mode="Markdown")

    # elif PickUp_city == "Andijon":
    #     for ast in a_list:
    #         update.message.bot.send_message(chat_id=ast,
    #                                         text=f"\n🏬Yuk olinadigan manzil: *{PickUp_city}* \n"
    #                                              f"\n⏰Yuk olish vaqti: *{time_to_pu}* \n"
    #                                              f"\n🏬Yukni yetkazib berish manzili: *{del_cities}* \n"
    #                                              f"\n⏰Yukni yetkazib berish vaqti: *{time_to_del}* \n"
    #                                              f"\n🚚Kerakli yuk mashinasi: {truck_type} \n"
    #                                              f"\n📋Yuk oluvchi uchun qo'shimcha ma'lumotlar: *{notebook}*",
    #                                         parse_mode="Markdown")
    # elif PickUp_city == "Farg'ona":
    #     for fst in f_list:
    #         update.message.bot.send_message(chat_id=fst,
    #                                         text=f"\n🏬Yuk olinadigan manzil: *{PickUp_city}* \n"
    #                                              f"\n⏰Yuk olish vaqti: *{time_to_pu}* \n"
    #                                              f"\n🏬Yukni yetkazib berish manzili: *{del_cities}* \n"
    #                                              f"\n⏰Yukni yetkazib berish vaqti: *{time_to_del}* \n"
    #                                              f"\n🚚Kerakli yuk mashinasi: {truck_type} \n"
    #                                              f"\n📋Yuk oluvchi uchun qo'shimcha ma'lumotlar: *{notebook}*",
    #                                         parse_mode="Markdown")

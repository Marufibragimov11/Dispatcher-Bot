from telegram import ReplyKeyboardRemove
from telegram.ext import ConversationHandler
from buttons import back_button, city_buttons, main_menu
from users_list import (t_list, f_list, a_list, n_list, sirdarya_users, jizzakh_users, samarkand_users, bukhara_users,
                        navoi_users, kashkadarya_users, surkhandarya_users, xorezm_users, karakalpak_users,
                        kirgizistan_users, tajikistan_users, kazakstan_users, rossia_users, turkey_users, china_users,
                        yevropa_users)


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
                              f"🕘Yukni olish vaqti: *{time_to_pu}* \n"
                              f"\n📌Yukni yetkazib berish manzili: *{delivery_location} - {del_cities}* \n"
                              f"🕘Yukni yetkazib berish vaqti: *{time_to_del}* \n"
                              f"\n🚚Kerakli yuk mashinasi: {truck_type} \n"
                              f"\n📋Yuk oluvchi uchun qo'shimcha ma'lumotlar: *{notebook}*",
                              parse_mode="Markdown",
                              reply_markup=back_button)
    return 9


def submit(update, context):
    update.message.reply_text(text=f"*Sizning postingiz {pick_location}dagi haydovchilarga yuborildi😉* \n",
                              parse_mode="Markdown",
                              reply_markup=main_menu)
    update.message.bot.send_message(chat_id="@yuklar_asia_usb",
                                    text=f"📌Yuk olinadigan manzil: *{pick_location} - {PickUp_city}* \n"
                                         f"🕘Yuk olish vaqti: *{time_to_pu}* \n"
                                         f"\n📌Yukni yetkazib berish manzili: *{delivery_location} - {del_cities}* \n"
                                         f"🕘Yukni yetkazib berish vaqti: *{time_to_del}* \n"
                                         f"\n🚚Kerakli yuk mashinasi: {truck_type} \n"
                                         f"\n📋Yuk oluvchi uchun qo'shimcha ma'lumotlar: *{notebook}*",
                                    parse_mode="Markdown")
    if pick_location == "🇺🇿Toshkent":
        for tst in t_list:
            update.message.bot.send_message(chat_id=tst,
                                            text=f"\n📌Yuk olinadigan manzil: <b>{pick_location} - {PickUp_city}</b> \n"
                                                 f"🕘Yuk olish vaqti: <b>{time_to_pu}</b> \n"
                                                 f"\n📌Yukni yetkazib berish manzili: <b>{delivery_location} - {del_cities}</b> \n"
                                                 f"🕘Yukni yetkazib berish vaqti: <b>{time_to_del}</b> \n"
                                                 f"\n🚚Kerakli yuk mashinasi: <b>{truck_type}</b>\n"
                                                 f"\n📋Yuk oluvchi uchun qo'shimcha ma'lumotlar: <b>{notebook}</b> \n"
                                                 f"\n👤Yuk sotuvchining telegram username: @{user}",
                                            parse_mode="html")
    elif pick_location == "🇺🇿Andijon":
        for ast in a_list:
            update.message.bot.send_message(chat_id=ast,
                                            text=f"\n📌Yuk olinadigan manzil: <b>{pick_location} - {PickUp_city}</b> \n"
                                                 f"🕘Yuk olish vaqti: <b>{time_to_pu}</b> \n"
                                                 f"\n📌Yukni yetkazib berish manzili: <b>{delivery_location} - {del_cities}</b> \n"
                                                 f"🕘Yukni yetkazib berish vaqti: <b>{time_to_del}</b> \n"
                                                 f"\n🚚Kerakli yuk mashinasi: <b>{truck_type}</b>\n"
                                                 f"\n📋Yuk oluvchi uchun qo'shimcha ma'lumotlar: <b>{notebook}</b> \n"
                                                 f"\n👤Yuk sotuvchining telegram username: @{user}",
                                            parse_mode="html")
    elif pick_location == "🇺🇿Farg'ona":
        for fst in f_list:
            update.message.bot.send_message(chat_id=fst,
                                            text=f"\n📌Yuk olinadigan manzil: <b>{pick_location} - {PickUp_city}</b> \n"
                                                 f"🕘Yuk olish vaqti: <b>{time_to_pu}</b> \n"
                                                 f"\n📌Yukni yetkazib berish manzili: <b>{delivery_location} - {del_cities}</b> \n"
                                                 f"🕘Yukni yetkazib berish vaqti: <b>{time_to_del}</b> \n"
                                                 f"\n🚚Kerakli yuk mashinasi: <b>{truck_type}</b>\n"
                                                 f"\n📋Yuk oluvchi uchun qo'shimcha ma'lumotlar: <b>{notebook}</b> \n"
                                                 f"\n👤Yuk sotuvchining telegram username: @{user}",
                                            parse_mode="html")
    elif pick_location == "🇺🇿Namangan":
        for nam in n_list:
            update.message.bot.send_message(chat_id=nam,
                                            text=f"\n📌Yuk olinadigan manzil: <b>{pick_location} - {PickUp_city}</b> \n"
                                                 f"🕘Yuk olish vaqti: <b>{time_to_pu}</b> \n"
                                                 f"\n📌Yukni yetkazib berish manzili: <b>{delivery_location} - {del_cities}</b> \n"
                                                 f"🕘Yukni yetkazib berish vaqti: <b>{time_to_del}</b> \n"
                                                 f"\n🚚Kerakli yuk mashinasi: <b>{truck_type}</b>\n"
                                                 f"\n📋Yuk oluvchi uchun qo'shimcha ma'lumotlar: <b>{notebook}</b> \n"
                                                 f"\n👤Yuk sotuvchining telegram username: @{user}",
                                            parse_mode="html")
    elif pick_location == "🇺🇿Sirdaryo":
        for sir in sirdarya_users:
            update.message.bot.send_message(chat_id=sir,
                                            text=f"\n📌Yuk olinadigan manzil: <b>{pick_location} - {PickUp_city}</b> \n"
                                                 f"🕘Yuk olish vaqti: <b>{time_to_pu}</b> \n"
                                                 f"\n📌Yukni yetkazib berish manzili: <b>{delivery_location} - {del_cities}</b> \n"
                                                 f"🕘Yukni yetkazib berish vaqti: <b>{time_to_del}</b> \n"
                                                 f"\n🚚Kerakli yuk mashinasi: <b>{truck_type}</b>\n"
                                                 f"\n📋Yuk oluvchi uchun qo'shimcha ma'lumotlar: <b>{notebook}</b> \n"
                                                 f"\n👤Yuk sotuvchining telegram username: @{user}",
                                            parse_mode="html")
    elif pick_location == "🇺🇿Jizzax":
        for jiz in jizzakh_users:
            update.message.bot.send_message(chat_id=jiz,
                                            text=f"\n📌Yuk olinadigan manzil: <b>{pick_location} - {PickUp_city}</b> \n"
                                                 f"🕘Yuk olish vaqti: <b>{time_to_pu}</b> \n"
                                                 f"\n📌Yukni yetkazib berish manzili: <b>{delivery_location} - {del_cities}</b> \n"
                                                 f"🕘Yukni yetkazib berish vaqti: <b>{time_to_del}</b> \n"
                                                 f"\n🚚Kerakli yuk mashinasi: <b>{truck_type}</b>\n"
                                                 f"\n📋Yuk oluvchi uchun qo'shimcha ma'lumotlar: <b>{notebook}</b> \n"
                                                 f"\n👤Yuk sotuvchining telegram username: @{user}",
                                            parse_mode="html")
    elif pick_location == "🇺🇿Samarqand":
        for sam in samarkand_users:
            update.message.bot.send_message(chat_id=sam,
                                            text=f"\n📌Yuk olinadigan manzil: <b>{pick_location} - {PickUp_city}</b> \n"
                                                 f"🕘Yuk olish vaqti: <b>{time_to_pu}</b> \n"
                                                 f"\n📌Yukni yetkazib berish manzili: <b>{delivery_location} - {del_cities}</b> \n"
                                                 f"🕘Yukni yetkazib berish vaqti: <b>{time_to_del}</b> \n"
                                                 f"\n🚚Kerakli yuk mashinasi: <b>{truck_type}</b>\n"
                                                 f"\n📋Yuk oluvchi uchun qo'shimcha ma'lumotlar: <b>{notebook}</b> \n"
                                                 f"\n👤Yuk sotuvchining telegram username: @{user}",
                                            parse_mode="html")
    elif pick_location == "🇺🇿Buxoro":
        for buk in bukhara_users:
            update.message.bot.send_message(chat_id=buk,
                                            text=f"\n📌Yuk olinadigan manzil: <b>{pick_location} - {PickUp_city}</b> \n"
                                                 f"🕘Yuk olish vaqti: <b>{time_to_pu}</b> \n"
                                                 f"\n📌Yukni yetkazib berish manzili: <b>{delivery_location} - {del_cities}</b> \n"
                                                 f"🕘Yukni yetkazib berish vaqti: <b>{time_to_del}</b> \n"
                                                 f"\n🚚Kerakli yuk mashinasi: <b>{truck_type}</b>\n"
                                                 f"\n📋Yuk oluvchi uchun qo'shimcha ma'lumotlar: <b>{notebook}</b> \n"
                                                 f"\n👤Yuk sotuvchining telegram username: @{user}",
                                            parse_mode="html")
    elif pick_location == "🇺🇿Navoi":
        for nav in navoi_users:
            update.message.bot.send_message(chat_id=nav,
                                            text=f"\n📌Yuk olinadigan manzil: <b>{pick_location} - {PickUp_city}</b> \n"
                                                 f"🕘Yuk olish vaqti: <b>{time_to_pu}</b> \n"
                                                 f"\n📌Yukni yetkazib berish manzili: <b>{delivery_location} - {del_cities}</b> \n"
                                                 f"🕘Yukni yetkazib berish vaqti: <b>{time_to_del}</b> \n"
                                                 f"\n🚚Kerakli yuk mashinasi: <b>{truck_type}</b>\n"
                                                 f"\n📋Yuk oluvchi uchun qo'shimcha ma'lumotlar: <b>{notebook}</b> \n"
                                                 f"\n👤Yuk sotuvchining telegram username: @{user}",
                                            parse_mode="html")
    elif pick_location == "🇺🇿Qashqadaryo":
        for kas in kashkadarya_users:
            update.message.bot.send_message(chat_id=kas,
                                            text=f"\n📌Yuk olinadigan manzil: <b>{pick_location} - {PickUp_city}</b> \n"
                                                 f"🕘Yuk olish vaqti: <b>{time_to_pu}</b> \n"
                                                 f"\n📌Yukni yetkazib berish manzili: <b>{delivery_location} - {del_cities}</b> \n"
                                                 f"🕘Yukni yetkazib berish vaqti: <b>{time_to_del}</b> \n"
                                                 f"\n🚚Kerakli yuk mashinasi: <b>{truck_type}</b>\n"
                                                 f"\n📋Yuk oluvchi uchun qo'shimcha ma'lumotlar: <b>{notebook}</b> \n"
                                                 f"\n👤Yuk sotuvchining telegram username: @{user}",
                                            parse_mode="html")
    elif pick_location == "🇺🇿Surxondaryo":
        for sur in surkhandarya_users:
            update.message.bot.send_message(chat_id=sur,
                                            text=f"\n📌Yuk olinadigan manzil: <b>{pick_location} - {PickUp_city}</b> \n"
                                                 f"🕘Yuk olish vaqti: <b>{time_to_pu}</b> \n"
                                                 f"\n📌Yukni yetkazib berish manzili: <b>{delivery_location} - {del_cities}</b> \n"
                                                 f"🕘Yukni yetkazib berish vaqti: <b>{time_to_del}</b> \n"
                                                 f"\n🚚Kerakli yuk mashinasi: <b>{truck_type}</b>\n"
                                                 f"\n📋Yuk oluvchi uchun qo'shimcha ma'lumotlar: <b>{notebook}</b> \n"
                                                 f"\n👤Yuk sotuvchining telegram username: @{user}",
                                            parse_mode="html")
    elif pick_location == "🇺🇿Xorazm":
        for xor in xorezm_users:
            update.message.bot.send_message(chat_id=xor,
                                            text=f"\n📌Yuk olinadigan manzil: <b>{pick_location} - {PickUp_city}</b> \n"
                                                 f"🕘Yuk olish vaqti: <b>{time_to_pu}</b> \n"
                                                 f"\n📌Yukni yetkazib berish manzili: <b>{delivery_location} - {del_cities}</b> \n"
                                                 f"🕘Yukni yetkazib berish vaqti: <b>{time_to_del}</b> \n"
                                                 f"\n🚚Kerakli yuk mashinasi: <b>{truck_type}</b>\n"
                                                 f"\n📋Yuk oluvchi uchun qo'shimcha ma'lumotlar: <b>{notebook}</b> \n"
                                                 f"\n👤Yuk sotuvchining telegram username: @{user}",
                                            parse_mode="html")
    elif pick_location == "🇺🇿Qoraqolpoqston":
        for kar in karakalpak_users:
            update.message.bot.send_message(chat_id=kar,
                                            text=f"\n📌Yuk olinadigan manzil: <b>{pick_location} - {PickUp_city}</b> \n"
                                                 f"🕘Yuk olish vaqti: <b>{time_to_pu}</b> \n"
                                                 f"\n📌Yukni yetkazib berish manzili: <b>{delivery_location} - {del_cities}</b> \n"
                                                 f"🕘Yukni yetkazib berish vaqti: <b>{time_to_del}</b> \n"
                                                 f"\n🚚Kerakli yuk mashinasi: <b>{truck_type}</b>\n"
                                                 f"\n📋Yuk oluvchi uchun qo'shimcha ma'lumotlar: <b>{notebook}</b> \n"
                                                 f"\n👤Yuk sotuvchining telegram username: @{user}",
                                            parse_mode="html")
    elif pick_location == "🇰🇬Qirg'iziston":
        for kir in kirgizistan_users:
            update.message.bot.send_message(chat_id=kir,
                                            text=f"\n📌Yuk olinadigan manzil: <b>{pick_location} - {PickUp_city}</b> \n"
                                                 f"🕘Yuk olish vaqti: <b>{time_to_pu}</b> \n"
                                                 f"\n📌Yukni yetkazib berish manzili: <b>{delivery_location} - {del_cities}</b> \n"
                                                 f"🕘Yukni yetkazib berish vaqti: <b>{time_to_del}</b> \n"
                                                 f"\n🚚Kerakli yuk mashinasi: <b>{truck_type}</b>\n"
                                                 f"\n📋Yuk oluvchi uchun qo'shimcha ma'lumotlar: <b>{notebook}</b> \n"
                                                 f"\n👤Yuk sotuvchining telegram username: @{user}",
                                            parse_mode="html")
    elif pick_location == "🇹🇯Tojikiston":
        for taj in tajikistan_users:
            update.message.bot.send_message(chat_id=taj,
                                            text=f"\n📌Yuk olinadigan manzil: <b>{pick_location} - {PickUp_city}</b> \n"
                                                 f"🕘Yuk olish vaqti: <b>{time_to_pu}</b> \n"
                                                 f"\n📌Yukni yetkazib berish manzili: <b>{delivery_location} - {del_cities}</b> \n"
                                                 f"🕘Yukni yetkazib berish vaqti: <b>{time_to_del}</b> \n"
                                                 f"\n🚚Kerakli yuk mashinasi: <b>{truck_type}</b>\n"
                                                 f"\n📋Yuk oluvchi uchun qo'shimcha ma'lumotlar: <b>{notebook}</b> \n"
                                                 f"\n👤Yuk sotuvchining telegram username: @{user}",
                                            parse_mode="html")
    elif pick_location == "🇰🇿Qozoqston":
        for kaz in kazakstan_users:
            update.message.bot.send_message(chat_id=kaz,
                                            text=f"\n📌Yuk olinadigan manzil: <b>{pick_location} - {PickUp_city}</b> \n"
                                                 f"🕘Yuk olish vaqti: <b>{time_to_pu}</b> \n"
                                                 f"\n📌Yukni yetkazib berish manzili: <b>{delivery_location} - {del_cities}</b> \n"
                                                 f"🕘Yukni yetkazib berish vaqti: <b>{time_to_del}</b> \n"
                                                 f"\n🚚Kerakli yuk mashinasi: <b>{truck_type}</b>\n"
                                                 f"\n📋Yuk oluvchi uchun qo'shimcha ma'lumotlar: <b>{notebook}</b> \n"
                                                 f"\n👤Yuk sotuvchining telegram username: @{user}",
                                            parse_mode="html")
    elif pick_location == "🇷🇺Rossiya":
        for ros in rossia_users:
            update.message.bot.send_message(chat_id=ros,
                                            text=f"\n📌Yuk olinadigan manzil: <b>{pick_location} - {PickUp_city}</b> \n"
                                                 f"🕘Yuk olish vaqti: <b>{time_to_pu}</b> \n"
                                                 f"\n📌Yukni yetkazib berish manzili: <b>{delivery_location} - {del_cities}</b> \n"
                                                 f"🕘Yukni yetkazib berish vaqti: <b>{time_to_del}</b> \n"
                                                 f"\n🚚Kerakli yuk mashinasi: <b>{truck_type}</b>\n"
                                                 f"\n📋Yuk oluvchi uchun qo'shimcha ma'lumotlar: <b>{notebook}</b> \n"
                                                 f"\n👤Yuk sotuvchining telegram username: @{user}",
                                            parse_mode="html")
    elif pick_location == "🇹🇷Turkiya":
        for tur in turkey_users:
            update.message.bot.send_message(chat_id=tur,
                                            text=f"\n📌Yuk olinadigan manzil: <b>{pick_location} - {PickUp_city}</b> \n"
                                                 f"🕘Yuk olish vaqti: <b>{time_to_pu}</b> \n"
                                                 f"\n📌Yukni yetkazib berish manzili: <b>{delivery_location} - {del_cities}</b> \n"
                                                 f"🕘Yukni yetkazib berish vaqti: <b>{time_to_del}</b> \n"
                                                 f"\n🚚Kerakli yuk mashinasi: <b>{truck_type}</b>\n"
                                                 f"\n📋Yuk oluvchi uchun qo'shimcha ma'lumotlar: <b>{notebook}</b> \n"
                                                 f"\n👤Yuk sotuvchining telegram username: @{user}",
                                            parse_mode="html")
    elif pick_location == "🇨🇳Xitoy":
        for chn in china_users:
            update.message.bot.send_message(chat_id=chn,
                                            text=f"\n📌Yuk olinadigan manzil: <b>{pick_location} - {PickUp_city}</b> \n"
                                                 f"🕘Yuk olish vaqti: <b>{time_to_pu}</b> \n"
                                                 f"\n📌Yukni yetkazib berish manzili: <b>{delivery_location} - {del_cities}</b> \n"
                                                 f"🕘Yukni yetkazib berish vaqti: <b>{time_to_del}</b> \n"
                                                 f"\n🚚Kerakli yuk mashinasi: <b>{truck_type}</b>\n"
                                                 f"\n📋Yuk oluvchi uchun qo'shimcha ma'lumotlar: <b>{notebook}</b> \n"
                                                 f"\n👤Yuk sotuvchining telegram username: @{user}",
                                            parse_mode="html")
    elif pick_location == "🇺🇳Yevropa":
        for yev in yevropa_users:
            update.message.bot.send_message(chat_id=yev,
                                            text=f"\n📌Yuk olinadigan manzil: <b>{pick_location} - {PickUp_city}</b> \n"
                                                 f"🕘Yuk olish vaqti: <b>{time_to_pu}</b> \n"
                                                 f"\n📌Yukni yetkazib berish manzili: <b>{delivery_location} - {del_cities}</b> \n"
                                                 f"🕘Yukni yetkazib berish vaqti: <b>{time_to_del}</b> \n"
                                                 f"\n🚚Kerakli yuk mashinasi: <b>{truck_type}</b>\n"
                                                 f"\n📋Yuk oluvchi uchun qo'shimcha ma'lumotlar: <b>{notebook}</b> \n"
                                                 f"\n👤Yuk sotuvchining telegram username: @{user}",
                                            parse_mode="html")
    return ConversationHandler.END

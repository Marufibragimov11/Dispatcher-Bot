from users_list import (t_list, f_list, a_list, n_list, sirdarya_users, jizzakh_users, samarkand_users, bukhara_users,
                        navoi_users, kashkadarya_users, surkhandarya_users, xorezm_users, karakalpak_users,
                        kirgizistan_users, tajikistan_users, kazakstan_users, rossia_users, turkey_users, china_users,
                        yevropa_users)
from buttons import city_buttons, button_to_back


def search_loads(update, context):
    update.message.reply_text(text="Quyidagi knopkalardan birini tanlang", reply_markup=city_buttons)
    text = update.message.text
    user_id = update.message.from_user.id
    if text == "↩️Ortga":
        if user_id in t_list:
            t_list.remove(user_id)
        elif user_id in a_list:
            a_list.remove(user_id)
        elif user_id in f_list:
            f_list.remove(user_id)
        elif user_id in n_list:
            n_list.remove(user_id)
        elif user_id in sirdarya_users:
            sirdarya_users.remove(user_id)
        elif user_id in jizzakh_users:
            jizzakh_users.remove(user_id)
        elif user_id in samarkand_users:
            samarkand_users.remove(user_id)
        elif user_id in bukhara_users:
            bukhara_users.remove(user_id)
        elif user_id in navoi_users:
            navoi_users.remove(user_id)
        elif user_id in kashkadarya_users:
            kashkadarya_users.remove(user_id)
        elif user_id in surkhandarya_users:
            surkhandarya_users.remove(user_id)
        elif user_id in xorezm_users:
            xorezm_users.remove(user_id)
        elif user_id in karakalpak_users:
            karakalpak_users.remove(user_id)
        elif user_id in kirgizistan_users:
            kirgizistan_users.remove(user_id)
        elif user_id in tajikistan_users:
            tajikistan_users.remove(user_id)
        elif user_id in kazakstan_users:
            kazakstan_users.remove(user_id)
        elif user_id in rossia_users:
            rossia_users.remove(user_id)
        elif user_id in turkey_users:
            turkey_users.remove(user_id)
        elif user_id in china_users:
            china_users.remove(user_id)
        elif user_id in yevropa_users:
            yevropa_users.remove(user_id)


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


def Namangan_loads(update, context):
    update.message.reply_text('Endi men sizga Namangan dagi yuklarni yuborib turaman 😊',
                              reply_markup=button_to_back)
    n_list.add(update.message.from_user.id)
    print(n_list)


def Sirdarya_loads(update, context):
    update.message.reply_text('Endi men sizga Sirdaryo dagi yuklarni yuborib turaman 😊',
                              reply_markup=button_to_back)
    sirdarya_users.add(update.message.from_user.id)
    print(sirdarya_users)


def Jizzakh_loads(update, context):
    update.message.reply_text('Endi men sizga Jizzax dagi yuklarni yuborib turaman 😊',
                              reply_markup=button_to_back)
    jizzakh_users.add(update.message.from_user.id)
    print(jizzakh_users)


def Samarkand_loads(update, context):
    update.message.reply_text('Endi men sizga Samarqand dagi yuklarni yuborib turaman 😊',
                              reply_markup=button_to_back)
    samarkand_users.add(update.message.from_user.id)
    print(samarkand_users)


def Bukhara_loads(update, context):
    update.message.reply_text('Endi men sizga Buxoro dagi yuklarni yuborib turaman 😊',
                              reply_markup=button_to_back)
    bukhara_users.add(update.message.from_user.id)


def Navoi_loads(update, context):
    update.message.reply_text('Endi men sizga Navoi dagi yuklarni yuborib turaman 😊',
                              reply_markup=button_to_back)
    navoi_users.add(update.message.from_user.id)


def Kashkadarya_loads(update, context):
    update.message.reply_text('Endi men sizga Qashqadaryo dagi yuklarni yuborib turaman 😊',
                              reply_markup=button_to_back)
    kashkadarya_users.add(update.message.from_user.id)


def Surkhandarya_loads(update, context):
    update.message.reply_text('Endi men sizga Surxondaryo dagi yuklarni yuborib turaman 😊',
                              reply_markup=button_to_back)
    surkhandarya_users.add(update.message.from_user.id)


def Xorazm_loads(update, context):
    update.message.reply_text('Endi men sizga Xorazm dagi yuklarni yuborib turaman 😊',
                              reply_markup=button_to_back)
    xorezm_users.add(update.message.from_user.id)


def Karakalpak_loads(update, context):
    update.message.reply_text('Endi men sizga Qoraqolpoqston dagi yuklarni yuborib turaman 😊',
                              reply_markup=button_to_back)
    karakalpak_users.add(update.message.from_user.id)


def Kirgizistan_loads(update, context):
    update.message.reply_text('Endi men sizga Qirg\'iziston dagi yuklarni yuborib turaman 😊',
                              reply_markup=button_to_back)
    kirgizistan_users.add(update.message.from_user.id)


def Tajikistan_loads(update, context):
    update.message.reply_text('Endi men sizga Tojikiston dagi yuklarni yuborib turaman 😊',
                              reply_markup=button_to_back)
    tajikistan_users.add(update.message.from_user.id)


def Kazakstan_loads(update, context):
    update.message.reply_text('Endi men sizga Qozoqiston dagi yuklarni yuborib turaman 😊',
                              reply_markup=button_to_back)
    kazakstan_users.add(update.message.from_user.id)


def Russia_loads(update, context):
    update.message.reply_text('Endi men sizga Rossiya dagi yuklarni yuborib turaman 😊',
                              reply_markup=button_to_back)
    rossia_users.add(update.message.from_user.id)


def Turkey_loads(update, context):
    update.message.reply_text('Endi men sizga Turkiya dagi yuklarni yuborib turaman 😊',
                              reply_markup=button_to_back)
    turkey_users.add(update.message.from_user.id)


def China_loads(update, context):
    update.message.reply_text('Endi men sizga Xitoy dagi yuklarni yuborib turaman 😊',
                              reply_markup=button_to_back)
    china_users.add(update.message.from_user.id)


def Europe_loads(update, context):
    update.message.reply_text('Endi men sizga Yevropa dagi yuklarni yuborib turaman 😊',
                              reply_markup=button_to_back)
    yevropa_users.add(update.message.from_user.id)

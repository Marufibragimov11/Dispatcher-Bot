from telegram import Bot
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters)

# Local files --------------------------------------------------------------------------------------------------
from cities import (fergana_name, andijon_name, tashkent_name, namangan_name, sirdarya_name, jizzakh_name,
                    samarkand_name, bukhara_name, navoi_name)
from Keyboards import main_buttons

STATE_CALENDAR = 1
bot = Bot

t_list = set()
f_list = set()
a_list = set()
n_list = set()
sirdarya_users = set()
jizzakh_users = set()
samarkand_users = set()
bukhara_users = set()
navoi_users = set()
kashkadarya_users = set()


def start(update, context):
    user = update.message.from_user
    print(context.user_data)
    update.message.reply_html(
        "Salom <b>{}!</b>\n "
        "<b>Men sizga kerakli shaxardan yuklarni ko'rsatib beraman</b>\n "
        "<b>Quyidagi knopkalardan birini tanlang: </b>".
            format(user.first_name), reply_markup=main_buttons)

    return STATE_CALENDAR


def Tashkent_loads(update, context):
    if update.message.chat.type == "private":
        update.message.reply_text(
            'Endi men sizga Toshkent dagi yuklarni yuborib turaman 😊')
        t_list.add(update.message.from_user.id)
        print(t_list)
    elif update.message.chat.type == "supergroup":
        # print(update.message.from_user.id)
        # context.user_data["hudud"] = "Tashkent"
        for lst in t_list:
            print(lst)
            for tosh in tashkent_name:
                if tosh in update.message.text:
                    update.message.bot.forward_message(chat_id=lst,
                                                       from_chat_id="@asdfghsgda",
                                                       message_id=update.message.message_id)
        print(update.message['text'])


def Andijan_loads(update, context):
    if update.message.chat.type == "private":
        update.message.reply_text(
            'Endi men sizga Andijon dagi yuklarni yuborib turaman 😊')
        a_list.add(update.message.from_user.id)
        print(a_list)
    elif update.message.chat.type == "supergroup":
        # print(update.message.from_user.id)
        # context.user_data["hudud"] = "Tashkent"
        for ast in a_list:
            print(ast)
            for andijan in andijon_name:
                if andijan in update.message.text:
                    update.message.bot.forward_message(chat_id=ast,
                                                       from_chat_id="@asdfghsgda",
                                                       message_id=update.message.message_id)


def Ferghana_loads(update, context):
    if update.message.chat.type == "private":
        update.message.reply_text(
            'Endi men sizga Farg\'ona dagi yuklarni yuborib turaman 😊')
        f_list.add(update.message.from_user.id)
        print(f_list)
    elif update.message.chat.type == "supergroup":
        # print(update.message.from_user.id)
        # context.user_data["hudud"] = "Tashkent"
        for fst in f_list:
            print(fst)
            for fergana in fergana_name:
                if fergana in update.message.text:
                    update.message.bot.forward_message(chat_id=fst,
                                                       from_chat_id="@asdfghsgda",
                                                       message_id=update.message.message_id)


def Namangan_loads(update, context):
    if update.message.chat.type == "private":
        update.message.reply_text(
            'Endi men sizga Namangan dagi yuklarni yuborib turaman 😊')
        n_list.add(update.message.from_user.id)
    elif update.message.chat.type == "supergroup":
        for nst in n_list:
            for namangan in namangan_name:
                if namangan in update.message.text:
                    update.message.bot.forward_message(chat_id=nst,
                                                       from_chat_id="@asdfghsgda",
                                                       message_id=update.message.message_id)


def Sirdarya_loads(update, context):
    if update.message.chat.type == "private":
        update.message.reply_text(
            'Endi men sizga Sirdaryo dagi yuklarni yuborib turaman 😊')
        sirdarya_users.add(update.message.from_user.id)
    elif update.message.chat.type == "supergroup":
        for sir_lst in sirdarya_users:
            for sirdarya in sirdarya_name:
                if sirdarya in update.message.text:
                    update.message.bot.forward_message(chat_id=sir_lst,
                                                       from_chat_id="@asdfghsgda",
                                                       message_id=update.message.message_id)


def Djizzak_loads(update, context):
    if update.message.chat.type == "private":
        update.message.reply_text(
            'Endi men sizga Jizzax dagi yuklarni yuborib turaman 😊')
        jizzakh_users.add(update.message.from_user.id)
    elif update.message.chat.type == "supergroup":
        for jiz_list in jizzakh_users:
            for jizzakh in jizzakh_name:
                if jizzakh in update.message.text:
                    update.message.bot.forward_message(chat_id=jiz_list,
                                                       from_chat_id="@asdfghsgda",
                                                       message_id=update.message.message_id)


def Samarkand_loads(update, context):
    if update.message.chat.type == "private":
        update.message.reply_text(
            'Endi men sizga Samarqand dagi yuklarni yuborib turaman 😊')
        samarkand_users.add(update.message.from_user.id)
    elif update.message.chat.type == "supergroup":
        for sam_list in samarkand_users:
            for samarkand in samarkand_name:
                if samarkand in update.message.text:
                    update.message.bot.forward_message(chat_id=sam_list,
                                                       from_chat_id="@asdfghsgda",
                                                       message_id=update.message.message_id)


def Bukhara_loads(update, context):
    if update.message.chat.type == "private":
        update.message.reply_text(
            'Endi men sizga Buxoro dagi yuklarni yuborib turaman 😊')
        bukhara_users.add(update.message.from_user.id)
    elif update.message.chat.type == "supergroup":
        for bukhara_list in bukhara_users:
            for bukhara in bukhara_name:
                if bukhara in update.message.text:
                    update.message.bot.forward_message(chat_id=bukhara_list,
                                                       from_chat_id="@asdfghsgda",
                                                       message_id=update.message.message_id)


def Navoi_loads(update, context):
    if update.message.chat.type == "private":
        update.message.reply_text(
            'Endi men sizga Navoi dagi yuklarni yuborib turaman 😊')
        navoi_users.add(update.message.from_user.id)
    elif update.message.chat.type == "supergroup":
        for navoi_list in navoi_users:
            for navoi in navoi_name:
                if navoi in update.message.text:
                    update.message.bot.forward_message(chat_id=navoi_list,
                                                       from_chat_id="@asdfghsgda",
                                                       message_id=update.message.message_id)


def Kashkadarya_loads(update, context):
    if update.message.chat.type == "private":
        update.message.reply_text(
            'Endi men sizga Navoi dagi yuklarni yuborib turaman 😊')
        navoi_users.add(update.message.from_user.id)
    elif update.message.chat.type == "supergroup":
        for navoi_list in navoi_users:
            for navoi in navoi_name:
                if navoi in update.message.text:
                    update.message.bot.forward_message(chat_id=navoi_list,
                                                       from_chat_id="@asdfghsgda",
                                                       message_id=update.message.message_id)


def Surkhandarya_loads(update, context):
    update.message.reply_text(
        'Endi men sizga Surxondaryo dagi yuklarni yuborib turaman 😊')


def Xorezm_loads(update, context):
    update.message.reply_text(
        'Endi men sizga Xorazm dagi yuklarni yuborib turaman 😊')


def Karakalpak_loads(update, context):
    update.message.reply_text(
        'Endi men sizga Qoraqolpoqiston dagi yuklarni yuborib turaman 😊')


updater = Updater(token='5382011252:AAFKaNGc0_KR4rzYtpa2nf8jOFn1zxfT7p0', use_context=True)
dispatcher = updater.dispatcher


def main():
    dispatcher.add_handler(CommandHandler('start', start))
    for tash_name in tashkent_name:
        dispatcher.add_handler(MessageHandler(Filters.regex('(' + tash_name + ')'), Tashkent_loads))
    for anjan_name in andijon_name:
        dispatcher.add_handler(MessageHandler(Filters.regex('(' + anjan_name + ')'), Andijan_loads))
    for ferg_name in fergana_name:
        dispatcher.add_handler(MessageHandler(Filters.regex('(' + ferg_name + ')'), Ferghana_loads))
    for naman_name in namangan_name:
        dispatcher.add_handler(MessageHandler(Filters.regex('(' + naman_name + ')'), Namangan_loads))
    for sirdar_name in sirdarya_name:
        dispatcher.add_handler(MessageHandler(Filters.regex('(' + sirdar_name + ')'), Sirdarya_loads))
    for jizza_name in jizzakh_name:
        dispatcher.add_handler(MessageHandler(Filters.regex('(' + jizza_name + ')'), Djizzak_loads))
    for sam_name in samarkand_name:
        dispatcher.add_handler(MessageHandler(Filters.regex('(' + sam_name + ')'), Samarkand_loads))

    #     conv_handler = ConversationHandler(
    #         entry_points=[CommandHandler('start', start),
    #                       MessageHandler(Filters.regex('^(' + Tashkent + ')$'), Tashkent_loads),
    # ],
    #         states={
    #             STATE_CALENDAR: [
    #                 MessageHandler(Filters.regex('^(' + Tashkent + ')$'), Tashkent_loads),
    #             ],
    #         },
    #         fallbacks=[CommandHandler('start', start)]
    #
    #     )
    #
    #     dispatcher.add_handler(conv_handler)

    updater.start_polling()
    updater.idle()


main()

# updated by Maruf
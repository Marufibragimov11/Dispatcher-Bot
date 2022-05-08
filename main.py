from telegram import Bot
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters)
from cities import fergana_name, andijon_name, tashkent_name
from Keyboards import main_buttons

STATE_CALENDAR = 1
bot = Bot

t_list = set()
f_list = set()
a_list = set()


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
        # for tosh in toshkent:
        #     re_text = re.findall(tosh, update.message.message_id)
        #     print(re)


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
    update.message.reply_text(
        'Endi men sizga Namangan dagi yuklarni yuborib turaman 😊')


def Sirdarya_loads(update, context):
    update.message.reply_text(
        'Endi men sizga Sirdaryo dagi yuklarni yuborib turaman 😊')


def Djizzak_loads(update, context):
    update.message.reply_text(
        'Endi men sizga Jizzax dagi yuklarni yuborib turaman 😊')


def Samarkan_loads(update, context):
    update.message.reply_text(
        'Endi men sizga Samarkand dagi yuklarni yuborib turaman 😊')


def Bukhara_loads(update, context):
    update.message.reply_text(
        'Endi men sizga Buxoro dagi yuklarni yuborib turaman 😊')


def Navoi_loads(update, context):
    update.message.reply_text(
        'Endi men sizga Navoi dagi yuklarni yuborib turaman 😊')


def Kashkadarya_loads(update, context):
    update.message.reply_text(
        'Endi men sizga Qashqadaryo dagi yuklarni yuborib turaman 😊')


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

    #     conv_handler = ConversationHandler(
    #         entry_points=[CommandHandler('start', start),
    #                       MessageHandler(Filters.regex('^(' + Tashkent + ')$'), Tashkent_loads),
    # ],
    #         states={
    #             STATE_CALENDAR: [
    #                 MessageHandler(Filters.regex('^(' + Tashkent + ')$'), Tashkent_loads),
    #                 MessageHandler(Filters.regex('^(' + Andijan + ')$'), Andijan_loads),
    #                 MessageHandler(Filters.regex('^(' + Ferghana + ')$'), Ferghana_loads),
    #                 MessageHandler(Filters.regex('^(' + Namangan + ')$'), Namangan_loads),
    #                 MessageHandler(Filters.regex('^(' + Sirdarya + ')$'), Sirdarya_loads),
    #                 MessageHandler(Filters.regex('^(' + Djizzak + ')$'), Djizzak_loads),
    #                 MessageHandler(Filters.regex('^(' + Samarkand + ')$'), Samarkan_loads),
    #                 MessageHandler(Filters.regex('^(' + Bukhara + ')$'), Bukhara_loads),
    #                 MessageHandler(Filters.regex('^(' + Navoi + ')$'), Navoi_loads),
    #                 MessageHandler(Filters.regex('^(' + Kashkadarya + ')$'), Kashkadarya_loads),
    #                 MessageHandler(Filters.regex('^(' + Surhandarya + ')$'), Surkhandarya_loads),
    #                 MessageHandler(Filters.regex('^(' + Horezm + ')$'), Xorezm_loads),
    #                 MessageHandler(Filters.regex('^(' + Karakalpakistan + ')$'), Karakalpak_loads)
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

# Bu proyekt Burxon tomonidan yangilandi

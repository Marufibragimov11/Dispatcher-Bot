from telegram import ReplyKeyboardMarkup, Bot
from telegram.ext import (Updater, CommandHandler, ConversationHandler, MessageHandler, Filters)

Tashkent = "Toshkent"
Andijan = "Andijon"
Ferghana = "Farg'ona"
Namangan = "Namangan"
Sirdarya = "Sirdaryo"
Djizzak = "Jizzax"
Samarkand = "Samarqand"
Bukhara = "Buxoro"
Navoi = "Navoi"
Kashkadarya = "Qashqadaryo"
Surhandarya = "Surxondaryo"
Horezm = "Xorazm"
Karakalpakistan = "Qoraqolpoqston"

toshkent = ["Tashkent", "Toshkent", "Tawkent", "Toshkend", "Tashkend", "Tashkendan"]

main_buttons = ReplyKeyboardMarkup([
    [Tashkent, Sirdarya, Djizzak], [Andijan, Ferghana, Namangan], [Samarkand, Bukhara, Navoi],
    [Kashkadarya, Surhandarya, Horezm], [Karakalpakistan]
], resize_keyboard=True)

STATE_CALENDAR = 1
bot = Bot


def start(update, context):
    user = update.message.from_user
    print(context.user_data)
    update.message.reply_html(
        "Salom <b>{}!</b>\n "
        "<b>Men sizga kerakli shaxardan yuklarni ko'rsatib beraman</b>\n "
        "<b>Quyidagi knopkalardan birini tanlang: </b>".
            format(user.first_name), reply_markup=main_buttons)

    return STATE_CALENDAR


t_list = []


def Tashkent_loads(update, context):
    if update.message.chat.type == "private":
        update.message.reply_text(
            'Endi men sizga Toshkent dagi yuklarni yuborib turaman 😊')
        t_list.append(update.message.from_user.id)
        print(t_list)
    elif update.message.chat.type == "supergroup":
        print(update.message.from_user.id)
        context.user_data["hudud"] = "Toshkent"
        for lst in t_list:
            print(lst)
            update.message.bot.forward_message(chat_id=lst,
                                               from_chat_id="@asdfghsgda",
                                               message_id=update.message.message_id)
            # context.bot.send_message(chat_id=lst, text=update.message.text)

    # update.message.bot.forward_message(chat_id=update.message.chat_id,
    # from_chat_id=-1926801217,
    # message_id=update.message.message_id)

    # chat_id = update.message.chat_id
    # message_id = update.message.message_id
    # for tosh in toshkent:
    #     if tosh == "Toshkent":
    #         print("salom")
    #         update.message.bot.forward_message(update.message.chat_id, "@asdfghsgda", update.message.message_id)
    #
    # update.message.bot.forward_message(chat_id=update.effective_message.chat_id,
    #                                    from_chat_id="@asdfghsgda",
    #                                    message_id=update.message.message_id)
    # update.message.bot.delete_message(chat_id=update.message.chat_id,
    #                                   message_id=update.message.message_id)

    # if update.message.chat.type == "private":
    #     bot.reply_to(update.message, update.message.text)
    # elif update.message.chat.type == "group":
    #     bot.reply_to(update.message, "Hello to all!")


def Andijan_loads(update, context):
    update.message.reply_text(
        'Endi men sizga Andijon dagi yuklarni yuborib turaman 😊')


def Ferghana_loads(update, context):
    update.message.reply_text(
        'Endi men sizga Farg\'ona dagi yuklarni yuborib turaman 😊')


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


updater = Updater('5382011252:AAFKaNGc0_KR4rzYtpa2nf8jOFn1zxfT7p0', use_context=True)


def main():
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(MessageHandler(Filters.regex('^(' + Tashkent + ')$'), Tashkent_loads))
    dispatcher.add_handler(MessageHandler(Filters.regex('^(' + Andijan + ')$'), Andijan_loads))
    dispatcher.add_handler(MessageHandler(Filters.regex('^(' + Ferghana + ')$'), Ferghana_loads))

    # dispatcher.add_handler(CallbackQueryHandler(inline_callback))

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

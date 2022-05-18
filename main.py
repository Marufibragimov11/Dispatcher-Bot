from telegram.ext import (Updater, CommandHandler, MessageHandler, ConversationHandler, Filters)

from buttons import start_buttons, back_button
from sold_loads import (city1_name, city2_name, time1, time2, notes,
                        start_conversation, pu_city, del_city, del_time, pu_time, truck, note)
from book_loads import (search_loads, Tashkent_loads, Ferghana_loads, Andijan_loads)

users_list = set()


def start(update, context):
    user = update.message.from_user
    update.message.reply_html(
        "Salom <b>{}!</b>\n "
        "<b>Men sizga kerakli shaxardan yuklarni ko'rsatib beraman</b>\n "
        "<b>Quyidagi knopkalardan birini tanlang: </b>".format(user.first_name),
        reply_markup=start_buttons)
    users_list.add(update.message.chat.id)
    update.message.bot.send_message(chat_id="@asdfghsgda",
                                    text="Guruhda yangi a'zo bor 😊 \n"
                                         f"Ismi: {update.message.chat.first_name} \n"
                                         f"Familiyasi: {update.message.chat.last_name} \n"
                                         f"Username: {update.message.chat.username}\n"
                                         f"Chat_id: {update.message.chat.id} \n"
                                         f"\nUmumiy foydalanuvchilar soni: {len(users_list)}")


def main():
    updater = Updater(token='5382011252:AAFKaNGc0_KR4rzYtpa2nf8jOFn1zxfT7p0', use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(
        ConversationHandler(
            entry_points=[MessageHandler(Filters.regex('^(Yuk sotaman)$'), start_conversation)],
            states={
                1: [MessageHandler(Filters.text, pu_city)],
                2: [MessageHandler(Filters.text, del_city)],
                3: [MessageHandler(Filters.text, pu_time)],
                4: [MessageHandler(Filters.text, del_time)],
                5: [MessageHandler(Filters.text, truck)],
                6: [MessageHandler(Filters.text, note)],
            },
            fallbacks=[CommandHandler('stop', start)]
        )
    )
    dispatcher.add_handler(MessageHandler(Filters.regex('(Tasdiqlash✅)'), start))
    dispatcher.add_handler(MessageHandler(Filters.regex('(Yuk olaman)'), search_loads))
    dispatcher.add_handler(MessageHandler(Filters.regex('(Ortga)'), search_loads))
    dispatcher.add_handler(MessageHandler(Filters.regex('(Toshkent)'), Tashkent_loads))
    dispatcher.add_handler(MessageHandler(Filters.regex('(Andijon)'), Andijan_loads))
    dispatcher.add_handler(MessageHandler(Filters.regex("(Farg'ona)"), Ferghana_loads))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()

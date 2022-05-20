from telegram.ext import (Updater, CommandHandler, MessageHandler, ConversationHandler, Filters)

from buttons import start_buttons
from sold_loads import (start_conversation, pu_location, pu_city, del_location, del_city, del_time, pu_time, truck,
                        note, submit)
from book_loads import (search_loads, Tashkent_loads, Ferghana_loads, Andijan_loads, Namangan_loads, Sirdarya_loads,
                        Jizzakh_loads, Samarkand_loads, Bukhara_loads, Navoi_loads, Kashkadarya_loads,
                        Surkhandarya_loads, Xorazm_loads, Karakalpak_loads, Kirgizistan_loads, Tajikistan_loads,
                        Kazakstan_loads, Russia_loads, China_loads, Turkey_loads, Europe_loads)
from users_list import users_list


def start(update, context):
    user = update.message.from_user
    update.message.reply_html(
        "Salom <b>{}!</b>\n "
        "<b>Yukingiz bo'lsa yoki yuk kerak bo'lsa men xizmatingizdaman</b>\n "
        "<b>Quyidagi knopkalardan birini tanlang:👇 </b>".format(user.first_name),
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
            entry_points=[MessageHandler(Filters.regex('(🚛Yuk bor)'), start_conversation)],
            states={
                1: [MessageHandler(Filters.text, pu_location)],
                2: [MessageHandler(Filters.text, pu_city)],
                3: [MessageHandler(Filters.text, del_location)],
                4: [MessageHandler(Filters.text, del_city)],
                5: [MessageHandler(Filters.text, pu_time)],
                6: [MessageHandler(Filters.text, del_time)],
                7: [MessageHandler(Filters.text, truck)],
                8: [MessageHandler(Filters.text, note)],
                9: [MessageHandler(Filters.text, submit)]
            },
            fallbacks=[CommandHandler('stop', start)]
        )
    )
    # dispatcher.add_handler(MessageHandler(Filters.regex('(❌Bekor qilish)'), start))
    dispatcher.add_handler(MessageHandler(Filters.regex('(🏠Bosh menu)'), start))
    dispatcher.add_handler(MessageHandler(Filters.regex('(🚛Yuk kerak)'), search_loads))
    dispatcher.add_handler(MessageHandler(Filters.regex('(↩️Ortga)'), search_loads))
    dispatcher.add_handler(MessageHandler(Filters.regex('(Toshkent)'), Tashkent_loads))
    dispatcher.add_handler(MessageHandler(Filters.regex('(Andijon)'), Andijan_loads))
    dispatcher.add_handler(MessageHandler(Filters.regex("(Farg'ona)"), Ferghana_loads))
    dispatcher.add_handler(MessageHandler(Filters.regex("(Namangan)"), Namangan_loads))
    dispatcher.add_handler(MessageHandler(Filters.regex("(Sirdaryo)"), Sirdarya_loads))
    dispatcher.add_handler(MessageHandler(Filters.regex("(Jizzax)"), Jizzakh_loads))
    dispatcher.add_handler(MessageHandler(Filters.regex("(Samarqand)"), Samarkand_loads))
    dispatcher.add_handler(MessageHandler(Filters.regex("(Buxoro)"), Bukhara_loads))
    dispatcher.add_handler(MessageHandler(Filters.regex("(Navoi)"), Navoi_loads))
    dispatcher.add_handler(MessageHandler(Filters.regex("(Qashqadaryo)"), Kashkadarya_loads))
    dispatcher.add_handler(MessageHandler(Filters.regex("(Surxondaryo)"), Surkhandarya_loads))
    dispatcher.add_handler(MessageHandler(Filters.regex("(Xorazm)"), Xorazm_loads))
    dispatcher.add_handler(MessageHandler(Filters.regex("(Qoraqolpoqston)"), Karakalpak_loads))
    dispatcher.add_handler(MessageHandler(Filters.regex("(Qirg'iziston)"), Kirgizistan_loads))
    dispatcher.add_handler(MessageHandler(Filters.regex("(Tojikiston)"), Tajikistan_loads))
    dispatcher.add_handler(MessageHandler(Filters.regex("(Qozoqston)"), Kazakstan_loads))
    dispatcher.add_handler(MessageHandler(Filters.regex("(Rossiya)"), Russia_loads))
    dispatcher.add_handler(MessageHandler(Filters.regex("(Turkiya)"), Turkey_loads))
    dispatcher.add_handler(MessageHandler(Filters.regex("(Xitoy)"), China_loads))
    dispatcher.add_handler(MessageHandler(Filters.regex("(Yevropa)"), Europe_loads))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()

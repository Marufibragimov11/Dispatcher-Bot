from telegram import ReplyKeyboardMarkup

start_buttons = ReplyKeyboardMarkup([
    ["Yuk sotaman", "Yuk olaman"]
], resize_keyboard=True)

back_button = ReplyKeyboardMarkup([
    ["Tasdiqlash✅"]
], resize_keyboard=True)

load_buttons = ReplyKeyboardMarkup([
    ["Toshkent", "Sirdaryo", "Jizzax"], ["Andijon", "Farg'ona", "Namangan"], ["Samarqand", "Buxoro", "Navoi"],
    ["Qashqadaryo", "Surxondaryo", "Xorazm"], ["Qoraqolpoqston"]
], resize_keyboard=True)

button_to_back = ReplyKeyboardMarkup([
    ["Ortga"]
], resize_keyboard=True)
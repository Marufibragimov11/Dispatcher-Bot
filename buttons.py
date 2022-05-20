from telegram import ReplyKeyboardMarkup

start_buttons = ReplyKeyboardMarkup([
    ["🚛Yuk bor", "🚛Yuk kerak"]
], resize_keyboard=True)

main_menu = ReplyKeyboardMarkup([
    ["🏠Bosh menu"]
], resize_keyboard=True)

back_button = ReplyKeyboardMarkup([
    ["✅Tasdiqlash"]
], resize_keyboard=True)

button_to_back = ReplyKeyboardMarkup([
    ["↩️Ortga"]
], resize_keyboard=True)

city_buttons = ReplyKeyboardMarkup([
    ["🇺🇿Toshkent", "🇺🇿Sirdaryo", "🇺🇿Jizzax"], ["🇺🇿Andijon", "🇺🇿Farg'ona", "🇺🇿Namangan"],
    ["🇺🇿Samarqand", "🇺🇿Buxoro", "🇺🇿Navoi"],
    ["🇺🇿Qashqadaryo", "🇺🇿Surxondaryo", "🇺🇿Xorazm"], ["🇺🇿Qoraqolpoqston"],
    ["🇰🇬Qirg'iziston", "🇹🇯Tojikiston", "🇰🇿Qozoqston"],
    ["🇷🇺Rossiya", "🇹🇷Turkiya", "🇨🇳Xitoy"], ["🇺🇳Yevropa"], ["🏠Bosh menu"]
], resize_keyboard=True)

# , "❌Bekor qilish"

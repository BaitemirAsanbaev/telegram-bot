
import telebot

bot = telebot.TeleBot('5057939340:AAFn_HtzHgt6ci3LAeAsGtHLJHzJc8HQGqk')

keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('Привет', 'Пока', 'йоу')


@bot.message_handler(commands=['start'])


def start_message(message):
    bot.send_message(message.chat.id, 'Приветсвую', reply_markup=keyboard1)


@bot.message_handler(content_types=['text'])


def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, "Привет")
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, "Адьёс")
    elif message.text.lower() == 'как дела':
        bot.send_message(message.chat.id, "хорошо, как у тебя")
    elif message.text.lower() == 'отлично':
        bot.send_message(message.chat.id, ":relaxed:")
    elif message.text.lower() == 'кто тебя создал':
        bot.send_message(message.chat.id, "Великий и неповторимый Байтемир")
    elif message.text.lower() == 'зачем ты существуешь':
        bot.send_message(message.chat.id, "Да так, просто")
    elif message.text.lower() == 'как тебя зовут':
        bot.send_message(message.chat.id, "Алукард")
    elif message.text.lower() == 'йоу':
        bot.send_sticker(message.chat.id, 'CAACAgQAAxkBAAEBBg1gWL5B6D96QBjvOEv34Ny30dbgXwACgu8sAAGV22IvtNGpCMLDzXoeBA')
    else:
        bot.send_message(message.chat.id, "wtf")


bot.polling()



# -*- coding: utf8 -*-
import random

import telebot
from telebot import types

bot = telebot.TeleBot('1391636304:AAHi8xB0iryw6a0oWulGmzySobSGpUOAnLo');

hb = ["поздравляю с Днем рождения!", "поздравляю тебя с этим прекрасным праздником - с Днем рождения!","от всей души прими мои самые искренние поздравления с Днем рождения!"]
ny = ["хочу поздравить с Новым годом!", "хочу поздравить с наступающим праздником"]
march8 = ['хочу поздравить тебя с 8 Марта! ','от всей души поздравляю с 8 Марта!',"поздравляю с Международным женским днем!"]
f23 = ["поздравляю с 23 февраля!"," поздравляю с Днем защитника Отечества!","поздравляю с празником мужества и отваги, смелости и храбрости! С 23 февраля! "]

pictures_hp = ['https://img11.postila.ru/data/af/d1/e8/29/afd1e8291d67398c6105134c4337acb8f122862a2d0b972a442a49b4fc1db831.jpg','https://club.season.ru/uploads/post/33194/615/post-33194-1483000615.jpeg','https://funik.ru/wp-content/uploads/2019/05/21e16e89fea0dbaa3874-4.jpg','https://kartinki-life.ru/articles/2018/09/24/krasivye-otkrytki-c-dnem-rozhdeniya-dlya-zhenshhin-chast-19-aya-5.jpg','https://i2.wp.com/pavlyxa.ru/wp-content/uploads/2014/12/Открытки-с-Днем-Рождения-бесплатно.gif']
pictures_ny = ['https://img-fotki.yandex.ru/get/196631/27156178.189/0_196abd_732ea414_XL.jpg','http://gifq.ru/wp-content/uploads/2018/12/gif_1513222358.gif','https://prisnilos.su/uploads/image/otkrytki-kollegam-s-novym-2019-godom-1.gif','https://molperm.ru/wp-content/uploads/2017/12/a5.gif']
pictures_March8 = ['https://avatars.mds.yandex.net/get-pdb/964102/4d9f4cbc-e794-428d-98b6-aada873e280c/s1200?webp=false','https://www.beesona.ru/upload/383/3293b5a1140529c85164afc8528a0153.jpg','https://мойбизнес32.рф/upload/iblock/e77/e77665983d4c9e1e9a63c995192cef8f.jpg','https://avatars.mds.yandex.net/get-pdb/1811460/c4d23ee9-02a4-43f5-8fbe-a9a54b48931e/orig','https://avatars.mds.yandex.net/get-pdb/906476/56483ebd-411e-4db7-898a-d6100463a6b8/s1200?webp=false']
pictures_23f = ['https://sun9-71.userapi.com/c841521/v841521534/73128/QpWP8apevgE.jpg','https://otkrytkivsem.ru/wp-content/uploads/2018/10/otkrytka-pozdravlenie-k-dnyu-zaschitnika-otechestva.jpg','https://kopilohka.ru/wp-content/uploads/2019/02/23fevralya0036-768x768.jpg']
holiday2 = [
    "Пускай за любым поворотом судьбы ждут потрясающе события, которые принесут вам и достаток, благополучие и уверенность в завтрашнем дне!",
    "  Желаю добра, света, мира, улыбок, отличного настроения. Пусть всё плохое обходит стороной, жизненные невзгоды преодолеваются с легкостью, а каждый день будет наполнен радостью и счастьем. И конечно, светлой веры, огромной надежды, бесконечной любви. ",
    "  Желаю каждый день улыбаться, просыпаться с хорошим настроением, наслаждаться жизнью и с полной уверенностью в себе. Пусть мечты никогда не покидают тебя и превращаются в реальность.”,”  Пусть жизнь будет беспрерывным потоком счастливых дней и прекрасных мгновений. Желаю назад оглядываться только лишь с хорошими воспоминаниями, вперёд смотреть с уверенностью в собственных силах и доброй надеждой, а в настоящем всегда оставаться замечательным человеком с любящим сердцем и открытой душой!"]

holiday = [
    "Очень много теплых слов хочется сегодня тебе сказать. Я желаю, чтобы твои мечты всегда сбывались, чтобы радостные, приятные моменты присутствовали в твоей жизни каждый день, чтобы друзья были только надежные, готовые всегда помочь или разделить радость.",
    " Желаю домашнего уюта, благополучия в семье, стабильности в бизнесе. Желаю, чтобы фортуна стала лучшим другом.",
    " Я желаю тебе крепкого здоровья, финансовой стабильности, гармонии во всем, любви во всех ее проявлениях, мирного неба над головой.",
    " Здоровья вам и простого, такого нужного всем нам человеческого счастья!",
    " Пусть по жизни сопутствует удача и успех, тебя окружают близкие по духу люди, а каждый твой день сияет новыми радужными красками!"]


@bot.message_handler(commands=['help'])
def help(message):
    if message.text == '/help':
        bot.send_message(message.from_user.id,
                         "Этот бот создан для того, чтобы генерировать поздравление человеку под выбранный Вами праздник.");
        bot.send_message(message.from_user.id, "Напишите /start, чтобы начать");
        bot.register_next_step_handler(message, start);
    else:
        bot.send_message(message.from_user.id, 'Я Вас не понимаю. Напишите /help.');

@bot.message_handler(commands=['start'])
def start(message):
    if message.text.lower() == "/start":
        bot.send_message(message.from_user.id, "Привет! Напиши имя человека, которого хочешь поздравить!");
        bot.register_next_step_handler(message, get_name);
    else:
        bot.send_message(message.from_user.id, 'Я тебя не понимаю. Напиши /help.');

def get_name(message):
    global name;
    name = message.text;
    keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
    keyboard.row('Сгенерировать')
    bot.send_message(message.from_user.id, 'Отлично!', reply_markup=keyboard)
    bot.register_next_step_handler(message, gener);

@bot.message_handler(content_types=['text'])
def gener(message):
    if message.text == 'Сгенерировать':
        bot.send_message(message.from_user.id, "Сейчас я сгенерирую поздравление")
        keyboard = types.InlineKeyboardMarkup()
        key_hp = types.InlineKeyboardButton(text='День рождения', callback_data='hb')
        keyboard.add(key_hp)
        key_ny = types.InlineKeyboardButton(text='Новый год', callback_data='ny')
        keyboard.add(key_ny)
        key_8 = types.InlineKeyboardButton(text='Международный женский день', callback_data='8')
        keyboard.add(key_8)
        key_23 = types.InlineKeyboardButton(text='День защитника Отечества', callback_data='23')
        keyboard.add(key_23)
        bot.send_message(message.from_user.id, text='осталось только выбрать праздник', reply_markup=keyboard)
    elif message.text == 'Да':
        bot.send_message(message.from_user.id, 'Отлично! С Вами приятно работать! Напишите /start, если хотите сгенерировать еще одно поздравление.');
        bot.register_next_step_handler(message, start);
    elif message.text == 'Нет':
        keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard.row('Сгенерировать')
        bot.send_message(message.from_user.id, 'Очень жаль, что Вам не понравилось. Может попробуем еще раз?', reply_markup=keyboard);
        bot.register_next_step_handler(message, gener);
    else:
        bot.send_message(message.from_user.id, 'Я Вас не понимаю. Напишите /help.');

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "hb":
        msg = name + ", " + random.choice(hb) + ' ' + random.choice(holiday)+ '' + random.choice(holiday2)
        bot.send_photo(call.message.chat.id, random.choice(pictures_hp), msg)
    if call.data == "ny":
        msg = name + ", " + random.choice(ny) + ' ' + random.choice(holiday)+ '' + random.choice(holiday2)
        bot.send_photo(call.message.chat.id, random.choice(pictures_ny),msg)
    if call.data == "8":
        msg = 'Дорогая ' + name + ", " + random.choice(march8) + ' ' + random.choice(holiday) + '' + random.choice(holiday2)
        bot.send_photo(call.message.chat.id, random.choice(pictures_March8),msg)
    if call.data == "23":
        msg = 'Дорогой ' + name + ", " + random.choice(f23) + ' ' + random.choice(holiday) + '' + random.choice(holiday2)
        bot.send_photo(call.message.chat.id, random.choice(pictures_23f),msg)
    keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
    keyboard.row('Да','Нет')
    bot.send_message(call.message.chat.id, "Подходит?", reply_markup=keyboard);
    bot.register_next_step_handler(call.message, gener);

bot.polling()

from pytimeparse import parse

import ptbot
import config


BOT = ptbot.Bot(config.TG_TOKEN)


def message_for_timer(chat_id, message):
    message = "Время вышло"
    
    BOT.send_message(chat_id=chat_id, message=message)


def timer(chat_id, message):
    time = parse(message)

    BOT.create_timer(time, message_for_timer, chat_id=chat_id, message=message)


def countdown(chat_id, message):
    time = parse(message)

    main_notify_message = "Осталось {} секунд!".format(time)
    message_id = BOT.send_message(chat_id=chat_id, message=main_notify_message)
    

    BOT.create_countdown(time, notify_progress, chat_id=chat_id, message_id=message_id)
    BOT.create_timer(time, message_for_timer, chat_id=chat_id, message=message)


def notify_progress(secs_left, chat_id, message_id):
    bar = render_progressbar(total=secs_left, iteration=1)

    main_notify_message = "Осталось {} секунд! \n {}".format(secs_left, bar)
    BOT.update_message(chat_id=chat_id, message_id=message_id, new_message=main_notify_message)


def render_progressbar(total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)


def main():
    BOT.send_message(config.TG_CHAT_ID, "Бот запущен")
    BOT.reply_on_message(countdown)
    BOT.run_bot()


if __name__=="__main__":
    main()
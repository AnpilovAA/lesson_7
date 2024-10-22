from pytimeparse import parse

import ptbot
import config


def message_for_timer(chat_id, message):
    message = "Время вышло"
    bot.send_message(chat_id=chat_id, message=message)


def countdown(chat_id, message):
    time = parse(message)
    main_notify_message = "Осталось {} секунд!".format(time)
    message_id = bot.send_message(chat_id=chat_id, message=main_notify_message)

    bot.create_countdown(
        time,
        notify_progress,
        chat_id=chat_id,
        message_id=message_id
        )
    bot.create_timer(time, message_for_timer, chat_id=chat_id, message=message)


def notify_progress(secs_left, chat_id, message_id):
    bar = render_progressbar

    if secs_left != 0:
        notify_message = f"Осталось {secs_left} секунд! \n {bar(secs_left, 0.9)}"
    else:
        notify_message = f"Осталось {0} секунд! \n {bar(1, 1)}"

    bot.update_message(
        chat_id=chat_id,
        message_id=message_id,
        new_message=notify_message
        )


def render_progressbar(total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)


def main():
    bot.send_message(config.TG_CHAT_ID, "Бот запущен")
    bot.reply_on_message(countdown)
    bot.run_bot()


if __name__ == "__main__":
    bot = ptbot.Bot(config.TG_TOKEN)
    main()

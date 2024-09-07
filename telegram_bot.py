import time
import requests
import telepot


def server_push_notifications(message_content):
    try:
        url = f"https://api.telegram.org/bot7355623583:AAGKeiusZvOrtMTlr1X7MiMDNt3w3Jl7XO0/sendMessage"
        response = requests.post(
            url=url,
            params={'chat_id': -4524627260, 'text': f"{message_content}", 'parse_mode': 'Markdown'}
            )
        bot = telepot.Bot('7355623583:AAGKeiusZvOrtMTlr1X7MiMDNt3w3Jl7XO0')
        bot.sendPhoto(-4524627260, photo=open('accident_frame/accident_img.jpg', 'rb'))
        print(url, response.json())
        time.sleep(10)
    except KeyboardInterrupt:
        return 

    


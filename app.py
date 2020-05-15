from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage
)
import random
app = Flask(__name__)

line_bot_api = LineBotApi('d4RG9WGjc104ouvQ1TTczvV9Xa962ub5SabRCqI/DnnXkJOd4OOqI0I/R2Pl1C5egytXWyhBS9fV5+sK+th9+/iWaCODN5JgrZe3bBEgGP48sYcXeoLWOjziZWaoBgtI25Lr+x+2dnX+8aSkO6VHXgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('59e11fc48798f3384e056e1086b9e18a')


def imgur_ran():
    while True:
        u1 = ''.join(random.choice(string.ascii_letters + string.digits) for x in range(5))
        image_file = 'https://i.imgur.com/'+u1+'.jpg'
        img = Image.open(urllib.request.urlopen(image_file))
        width, height = img.size
        if width != 161:
            break
        else:
            continue  
  
    return image_file


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    if '摸頭' in msg:
        image_file = imgur_ran()
        img = ImageSendMessage(
            original_content_url = image_file,
            preview_image_url = image_file
        )
        line_bot_api.reply_message(
        event.reply_token, img)
        return

    if  msg == '爸爸': 
        r = '摸頭!好乖!'
    line_bot_api.reply_message(
    event.reply_token,
    TextSendMessage(text=r))
    




        

if __name__ == "__main__":
    app.run()
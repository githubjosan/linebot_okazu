from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, LocationMessage
)
import os
from menu import Menu

# Menuインスタンス生成
# TODO:辞書型を修正する予定
menu = Menu()

app = Flask(__name__)

# 環境変数取得
LINE_CHANNEL_ACCESS_TOKEN = os.environ["LINE_CHANNEL_ACCESS_TOKEN"]
LINE_CHANNEL_SECRET = os.environ["LINE_CHANNEL_SECRET"]

line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(LINE_CHANNEL_SECRET)


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    print("body:", body)

    # handle webhook body
    try:
        handler.handle(body, signature)

    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.message.text == "今日のランチ":
        line_bot_api.reply_message(
            event.reply_token,
            [
                TextSendMessage(text='君が来るの待っていた♪～'),
                TextSendMessage(text='今日のランチは:'),
                TextSendMessage(text=(menu.okazu())),
            ]
        )
    elif event.message.text == "位置情報":
        line_bot_api.reply_message(
            event.reply_token,
            [
                TextSendMessage(text='位置情報を教えてください。'),
                TextSendMessage(text='line://nv/location')
            ]
        )

    else:
        line_bot_api.reply_message(
            event.reply_token,
            [
                TextSendMessage(text='「今日のランチ」って言ってくれたらいいものあげるよ♪'),
            ]
        )


@handler.add(MessageEvent, message=LocationMessage)
def handle_location(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(
            text="{}\n{}\n{}".format(event.message.address, event.message.latitude, event.message.longitude)),

    )


if __name__ == "__main__":
    #    app.run()
    port = int(os.getenv("PORT"))
    app.run(host="0.0.0.0", port=port)

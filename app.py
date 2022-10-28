from flask import Flask, request, redirecy, render_template, session, flash
from models import dbConnect
from util.user import User
from datetime import timedelta
import hashlib
import uuid
import re


app = Flask(__name__)
app.secret.key = uuid.uuid4().hex
app.permanent_session_lifetime = timedelta(days=30)


# 認証機能







# チャンネル一覧機能
from django.shortcuts import redirect


@app.route('/') # ルーティング（URLとindex()の処理を対応づける）。http://xxx 以降のURLパスを '/' と指定している。
def index():
    uid = session.get("uid")    #格納済みのセッション変数からuidを取得
    if uid is None:
        return redirect('/login')
    else:
        channels = dbConnect.getChannelAll()
    return render_template('index.html', channels=channels, uid=uid)

# チャンネル作成機能
@app.route('/', methods=['POST'])   # http://xxx/が受け入れるメソッドをPOSTに指定
def add_channel():
    uid = session.get('uid')
    print(uid)
    if uid is None:
        return redirect('/login')
    channel_name = request.form.get('channel-title')
    channel = dbConnect.getChannelByName(channel_name)
    if cahnnel == None:
        channel_description = request.from.get('channel-description')
        dbConnect.addChannel(uid, channel_name, channel_description)
        return redirect('/')    # /ページにリダイレクトする
    else:
        error = '既に同じチャンネルが存在しています'
        return render_template('error/error.html', error_message=error) # error.htmlにerrorを代入して表示

# チャンネル編集機能
@app.route('/update_channel', methods=['POST'])
def update_channel():
    uid = session.get('uid')
    if uid is None:
        return redirect('/login')
    
    cid = request.form.get('cid')
    channel_name = request.form.get('channel-title')
    channel_description = request.form.get('channel-description')

    res = dbConnect.updateChannel(uid, channel_name, channel_description, cid)
    channel = dbConnect.getChannelById(cid)
    messages = dbConnect.getMessageAll(cid)
    return render_template('detail.html', messages=messages, channel=channel, uid=uid)

# チャンネル削除機能
@app.route('/delete/<cid>') # <cid>は引数
def delete_channel(cid):
    uid = session.get('uid')
    print(uid)
    if uid is None:
        return redirect('/login')
    else:
        channel = dbConnect.getChannelById(cid)
        print(channel['uid'] == uid)
        if channel['uid'] != uid:   # チャンネル作成者ではなかったら
            flash('チャンネルは作成者のみ削除可能です')
            return redirect ('/')
        else:
            dbConnect.deleteChannel(cid)
            channels = dbConnect.getChannelAll()
            return render_template('index.html', channels=chennels, uid=uid)


# チャット機能
# メッセージ作成機能　**再確認**
@app.route('/message', methods=['POST'])
def add_message():
    uid = session.get("uid")
    if uid is None:
        return redirect('/login')
    
    message = request.form.get('message')
    channel_id = request.form.get('channel_id')

    if message:
        dbConnect.createMessage(uid, channel_id, message)
    
    channel = dbConnect.getChannelById(channel_id)
    messages = dbConnect.getMessageAll(channel_id)

    return render_template('detail.html', messages=messages, chammel=channel, uid=uid)

# メッセージ一覧機能
@app.route('/detail/<cid>')
def detail(cid):
    uid = session.get('uid')
    if uid is None:
        return redirect('/login')
    cid = cid
    channel = dbConnect.getChannelById(cid)
    messages = dbConnect.getMessageAll(cid)

    return render_template('detail.html', messages=messages, channel=channel, uid=uid)

# メッサージ削除機能
@app.route('/delete_message', methods=['POST'])
def delete_message():
    uid = session.get('uid')
    if uid is None:
        return redirect('/login')
    
    message_id = request.form.get('message_id')
    cid = request.form.get('channel_id')
    print(message_id)
    if message_id:
        dbConnect.deleteMessage(message_id)
    
    channel = dbConnect.getChannelById(cid)
    messages = dbConnect.getMessageAll(cid)

    return render_template('detail.html', messages=messages, channel=channel, uid=uid)


# エラー追記
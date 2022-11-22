from flask import Flask, request, redirect, render_template, session, flash # モジュールのインポート
from models import dbConnect
from util.user import User
from datetime import timedelta
import hashlib  # ハッシュ化
import uuid # 世界で一意な識別子（Universally Unique Identifier）
import re  # 正規表現モジュール


app = Flask(__name__)   # Webアプリ作成。Flaskクラスのインスタンスを作成し、それをappに代入。__name__はグローバル変数。
app.secret_key = uuid.uuid4().hex   
app.permanent_session_lifetime = timedelta(days=30)


# 認証機能
@app.route('/signup')
def signup():
    return render_template('registration/signup.html')

@app.route('/signup', methods=['POST'])
def userSignup():
    name = request.form.get('name')
    email = request.form.get('email')
    password1 = request.form.get('password1')
    password2 = request.form.get('password2')

    pattern = "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

    if name == '' or email == '' or password1 == '' or password2 == '':
        flash('空のフォームがあるようです')
    elif password1 != password2:
        flash('二つのパスワードの値が間違っています')
    elif re.match(pattern, email) is None:
        flash('正しいメールアドレスの形式ではありません')
    else:
        uid = uuid.uuid4()  # uuid4はOS固有の乱数でランダムなUUIDを生成
        password = hashlib.sha256(password1.encode('utf-8')).hexdigest()    # encode：utf-8方式で文字列をバイト列に変換。hexdigest：16進形式文字列に。
        user = User(uid, name, email, password)
        DBuser = dbConnect.getUser(email)   # emailが重複していないか確認

        if DBuser != None:
            flash('既に登録されているようです')
        else:
            dbConnect.createUser(user)
            UserId = str(uid)
            session['uid'] = UserId
            return redirect('/')
    return redirect('/signup')

@app.route('/login')
def login():
    return render_template('registration/login.html')

@app.route('/login', methods=['POST'])
def userLogin():
    email = request.form.get('email')
    password = request.form.get('password')

    if email == '' or password == '':
        flash('空のフォームがあるようです')
    else:
        user = dbConnect.getUser(email)
        if user is None:
            flash('このユーザーは存在しません')
        else:
            hashPassword = hashlib.sha256(password.encode(utf-8)).hexdigest()
            if hashPassword != user["password"]:
                flash('パスワードが間違っています！')
            else:
                session['uid'] = user["uid"]
                return redirect('/')
    return redirect('/login')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')


# チャンネル機能
# チャンネル一覧機能
@app.route('/') # ルーティング（URLにアクセスするとindex()の関数が実行される）。http://xxx 以降のURLパスを '/' と指定している。
def index():
    uid = session.get('uid')    #格納済みのセッション変数からuidを取得
    if uid is None:
        return redirect('/login')
    else:
        chatrooms = dbConnect.getChatroomAll()
    return render_template('index.html', chatrooms=chatrooms, uid=uid)

# チャンネル作成機能
@app.route('/', methods=['POST'])   # http://xxx/が受け入れるメソッドをPOSTに指定
def add_chatroom():
    uid = session.get('uid')
    if uid is None:
        return redirect('/login')
    chatroom_name = request.form.get('chatroom-title')    # チャンネル名を取得
    chatroom = dbConnect.getChatroomByName(chatroom_name)  
    if chatroom == None:
        chatroom_description = request.form.get('chatroom-description')   # チャンネルの説明を取得
        dbConnect.addChatroom(uid, chatroom_name, chatroom_description) 
        return redirect('/')    # /ページにリダイレクトする
    else:
        error = '既に同じチャンネルが存在しています'
        return render_template('error/error.html', error_message=error) # error.htmlにerrorを代入して表示

# チャンネル編集機能
@app.route('/update_chatroom', methods=['POST'])
def update_chatroom():
    uid = session.get('uid')
    if uid is None:
        return redirect('/login')
    
    cid = request.form.get('cid')
    chatroom_name = request.form.get('chatroom-title')
    chatroom_description = request.form.get('chatroom-description')

    dbConnect.updateChatroom(uid, chatroom_name, chatroom_description, cid)  # res???
    chatroom = dbConnect.getChatroomById(cid)
    messages = dbConnect.getMessageAll(cid)
    return render_template('detail.html', messages=messages, chatroom=chatroom, uid=uid)

# チャンネル削除機能
@app.route('/delete/<cid>') # <cid>は引数
def delete_chatroom(cid):
    uid = session.get('uid')
    if uid is None:
        return redirect('/login')
    else:
        chatroom = dbConnect.getChatroomById(cid)
        if chatroom['uid'] != uid:   # チャンネル作成者ではなかったら
            flash('チャンネルは作成者のみ削除可能です')
            return redirect ('/')
        else:
            dbConnect.deleteChatroom(cid)
            chatrooms = dbConnect.getChatroomAll()
            return render_template('index.html', chatrooms=chatrooms, uid=uid)

# チャット機能
# メッセージ一覧機能
# uidもmessageと一緒に返す（？）
@app.route('/detail/<cid>')
def detail(cid):
    uid = session.get('uid')
    if uid is None:
        return redirect('/login')
    cid = cid
    chatroom = dbConnect.getChatroomById(cid)
    messages = dbConnect.getMessageAll(cid)

    return render_template('detail.html', messages=messages, chatroom=chatroom, uid=uid)

# メッセージ作成機能
@app.route('/message', methods=['POST'])
def add_message():
    uid = session.get("uid")
    if uid is None:
        return redirect('/login')
    
    message = request.form.get('message')
    chatroom_id = request.form.get('chatroom_id')

    if message:     # ???
        dbConnect.createMessage(uid, chatroom_id, message)
    
    chatroom = dbConnect.getChatroomById(chatroom_id)
    messages = dbConnect.getMessageAll(chatroom_id)

    return render_template('detail.html', messages=messages, chatroom=chatroom, uid=uid)

# メッサージ削除機能
@app.route('/delete_message', methods=['POST'])
def delete_message():
    uid = session.get('uid')
    if uid is None:
        return redirect('/login')
    
    message_id = request.form.get('message_id')
    cid = request.form.get('chatroom_id')
    if message_id:  #None以外の場合？
        dbConnect.deleteMessage(message_id)
    
    chatroom = dbConnect.getChatroomById(cid)
    messages = dbConnect.getMessageAll(cid)

    return render_template('detail.html', messages=messages, chatroom=chatroom, uid=uid)


# エラー処理
@app.errorhandler(404)
def show_error404(error):
    return render_template('error/404.html')


@app.errorhandler(500)
def show_error500(error):
    return render_template('error/500.html')


# Webアプリ起動。
if __name__ == '__main__':  # ifプログラムが直接実行されたか
    app.run(debug=True)     # run関数


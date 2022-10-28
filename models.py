# チャンネル一覧機能
def getChannelAll():
    try:    # try-except文（エラーの可能性がある処理に、例外処理を設定しておくことでプログラムを中断させない）
        conn = DB.getConnection()   # データベースに接続
        cur = conn.cursor() # カーソルを取得(取得結果からデータを1件ずつ抜き取るための仕組み)
        sql = "SELECT * FROM channels;" #SQL文を実行
        cur.excute(sql)
        channels = cur.fetchall()   #FETCH=データベースから取得したデータを1件ずつ参照する機能
        return channels
    except Exception as e:
        print(e +'が発生しています')
        return None
    finally:
        cur.close()

# チャンネル作成機能
def getChannelById(cid):
    try:
        conn = DB.getConnection()
        cur = conn.cursor()
        sql = "SELECT * FROM channels WHERE id=%s;"
        cur.execute(sql, (cid))
        channel = cur.fetchone()    # *で全件取得した後、その中の1件だけをプログラム的に取得
        return channel
    except Exception as e:
        print(e + 'が発生しています')
        return None
    finally:
        cur.close()

#チャンネル編集機能
def updateChannel(uid, newChannelName, newChannelDescription, cid):
    conn = DB.getConnection()
    cur = conn.cursor()
    sql = "UPDATE channels SET uid=%s, name=%s, abstract=%s WHERE id=%s;"
    cur.execute(sql, (uid, newChannelName, newChannelDescription, cid))
    conn.commit()
    cur.close()

# チャンネル削除機能
def deleteChannel(cid):
    try:
        conn = DB.getConnection()
        cur = conn.cursor()
        sql = "DELETE FROM channels WHERE id=%s;"
        cur.excute(sql, (cid))
        conn.commit()
    except Exception as e:
        print(e + 'が発生しています')
        return None
    finally:
        cur.close()


# チャット機能
# メッセージ作成機能（データベースにメッセージを登録）
def createMessage(uid, cid, message):
    try:
        conn = DB.getConnection()
        cur = conn.cursor()
        sql = "INSERT INTO messages(uid, cid, message) VALUE(%s, %s, %s)"   #messagesテーブルの各カラムに%s()を登録
        cur.execute(sql, (uid, cid, message))
        conn.commit()
    except Exception as e:
        print(e + 'が発生しています')
        return None
    finally:
        cur.close()

# メッセージ一覧機能
def getMessageAll(cid):
    try:
        conn = DB.getConnection()
        cur = con.cursor()
        sql = "SELECT id, u, uid, user_name, message FROM messages AS m INNER JOIN users AS u ON m.uid WHERE cid = %s;"
        cur.excecute(sql, (cid))
        messages = cur.fetchall()
        return messages
    except Exception as e:
        print(e + 'が発生しています')
        return None
    finally:
        cur.close()

#メッセージ削除機能
def deleteMessage(message_id):
    try:
        conn = DB.getConnection()
        cur = conn.cursor()
        sql = "DELETE FROM messages WHERE id=%s;"
        cur.execute(sql, (message_id))
        conn.commit()
    except Exception as e:
        print(e +'が発生しています')
        return None
    finally:
        cur.close()


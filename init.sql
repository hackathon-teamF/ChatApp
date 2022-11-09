
DROP DATABASE chatapp;      -- 一回削除？
DROP USER 'testuser'@'localhost';

CREATE USER 'testuser'@'localhost' IDENTIFIED BY 'testuser';    -- パスワード（testuser）を指定してユーザー作成
CREATE DATABASE chatapp;
USE chatapp
GRANT ALL PRIVILEGES ON chatapp.* TO 'testuser'@'localhost';    -- テストユーザーに全ての権限を与える

CREATE TABLE users (
    uid varchar(225) PRIMARY KEY,
    user_name varchar(225) UNIQUE NOT NULL,
    email varchar(225) UNIQUE NOT NULL,
    password varchar(225) NOT NULL
);

CREATE TABLE channels (
    id serial PRIMARY KEY,
    uid varchar(225) REFERENCES users(uid),
    name varcher(255) UNIQUE NOT NULL,
    abstract varchar(225)
);

CREATE TABLE messages (
    id serial PRIMARY KEY,
    uid varchar(225) REFERENCES users(uid),
    cid integer REFERENCES channels(id) ON DELETE CASCADE,  -- ON〜〜は親表（channels）で行が削除されたら子表（messages）の対応行も削除
    message text,
    created_at timestamp not null default current_timestamp
);

INSERT INTO users(uid, user_name, email, password)VALUES('970af84c-dd40-47ff-af23-282b72b7cca8','テスト','test@gmail.com','37268335dd6931045bdcdf92623ff819a64244b53d0e746d438797349d4da578');
INSERT INTO channels(id, uid, name, abstract)VALUES(1, '970af84c-dd40-47ff-af23-282b72b7cca8','ぼっち部屋','テストさんの孤独な部屋です');
INSERT INTO messages(id, uid, cid, message)VALUES(1, '970af84c-dd40-47ff-af23-282b72b7cca8', '1', '誰かかまってください、、')
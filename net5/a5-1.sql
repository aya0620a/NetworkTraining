.open a5-1.db
.mode box
DROP TABLE IF EXISTS events;

-- データベースの作成
CREATE DATABASE event_db;
USE event_db;

-- テーブルの作成
CREATE TABLE events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_name VARCHAR(255) NOT NULL,
    event_date DATE NOT NULL,
    city VARCHAR(255) NOT NULL
);

-- イベントの登録
INSERT INTO events (event_name, event_date, city) VALUES
('東京オリンピック', '2021-07-23', '東京'),
('サマーソニック', '2021-08-20', '東京'),
('大阪フェスティバル', '2021-09-10', '大阪'),
('名古屋マラソン', '2021-10-15', '名古屋'),
('札幌雪まつり', '2022-02-05', '札幌'),
('誕生日会', '2024-08-27', '兵庫'),
('クリスマスパーティ', '2024-12-25', '和歌山');


-- (a) 登録したイベントの情報を全て表示せよ
SELECT * FROM events;

-- (b) 部分的なイベント名検索を行え
-- 例えば、"Festival"で検索する場合
SELECT * FROM events WHERE event_name LIKE '%フェスティバル%';

-- (c) 未来のイベントの検索を行え
SELECT * FROM events WHERE event_date > CURRENT_DATE;

-- (d) 複合検索を行え
-- 例えば、「過去のTokyo」の検索
SELECT * FROM events WHERE event_name LIKE '%東京%' AND event_date < CURRENT_DATE;

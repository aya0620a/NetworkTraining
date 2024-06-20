.open a5-2.db
.mode box
DROP TABLE IF EXISTS events;

CREATE TABLE events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_name TEXT,
    event_date DATE,
    event_place TEXT
);

INSERT INTO events (event_name, event_date, event_place) VALUES
('東京オリンピック', '2021-07-23', '東京'),
('ロンドンオリンピック', '2012-07-27', 'ロンドン'),
('東京マラソン', '2021-10-17', '東京'),
('大阪マラソン', '2021-11-28', '大阪'),
('名古屋マラソン', '2021-12-12', '名古屋'),
('大学卒業', '2026-03-31', '兵庫'),
('誕生日会', '2024-08-27', '自宅'),
('札幌マラソン', '2022-08-28', '札幌'),
('サマーソニック', '2021-08-20', '東京'),
('大阪フェスティバル', '2021-09-10', '大阪'),
('名古屋フェスティバル', '2021-10-15', '名古屋'),
('名古屋マラソン', '2021-10-15', '名古屋'),
('大阪万博', '2025-05-03', '大阪'),
('大学卒業', '2026-03-31', '兵庫');

SELECT * FROM events;
SELECT * FROM events WHERE event_name LIKE '%フェスティバル%';
SELECT * FROM events WHERE event_date > CURRENT_DATE;
SELECT * FROM events WHERE event_name LIKE '%東京%' AND event_date < CURRENT_DATE;

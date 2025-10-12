create table if not exists banks(
    id integer primary key autoincrement,
    name text,
    account text,
    balance integer,
    description text
);
create table if not exists payments(
     id integer primary key autoincrement,
    document_type text,
    transaction_type text,
    date_time text,
    customer_id integer,
    total_amount text,
    items_list text,
    description text
);

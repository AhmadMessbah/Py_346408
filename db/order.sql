create table if not exists orders (
    id integer primary key autoincrement ,
    order_type text,
    customer_id text ,
    employee_id text ,
    datetime text,
    payment_id text,
    warehouse_transaction_id text,
    tax real,
    total_discount real,
    total_amount real
) ;

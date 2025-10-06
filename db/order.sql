create table if not exists orders (
    id integer primary key autoincrement ,
    customer text ,
    employee text ,
    order_item_list text ,
    datetime text
) ;

import requests
import sqlite3

class BankRequest :

        def craete_table () :
            connection = sqlite3.connect( "db/bank.db" )
            connection.cursor().execute( "CREATE TABLE "reports" IF NOT EXISTS (
                                "id"	INTEGER NOT NULL,
                                "price"	TEXT NOT NULL,
                                "call_back_url"	TEXT NOT NULL,
                                "message"	TEXT NOT NULL,
                                "error"	INTEGER NOT NULL,
                                "order_id"	INTEGER NOT NULL,
                                "payment_id"	INTEGER NOT NULL,
                                "debit_card_number"	TEXT NOT NULL,
                                PRIMARY KEY("id" AUTOINCREMENT);
                            )
            
            connection.commit()
            connection.close()


        def save_request ( id , price , call_back_url , message , error , order_id , payment_id , debit_card_number ) :
            x = BankRequest()
            x.craete_table()
            connection = sqlite3.connect( "/db/bank.db" )
            connection.cursor().execute( "INSERT INTO reports VALUES "
            "( id , price , call_back_url , message , message , error , order_id , payment_id , debit_card_number )" \
            [ id , price , call_back_url , message , error , order_id , payment_id , debit_card_number ]
            )
            connection.commit()
            connection.close()


        def make_request ( price , order_id ) :
        
            # data = {
            #     'price': 1_000_000,
            #     'order_id' : 'order id from database'
            # }

            data = {}
            data[ "price" ] = price
            data[ "order_id" ] = order_id

            url = 'https://example.com/api/endpoint' 

            data[ 'token' ] = 'token string'
            data[ 'bank_username' ] = 'username string from bank'
            data[ 'callback_url' ] = 'my-site/order/callback'
            
            response = requests.post( url , data = data )

            try :
                '''
                responce = {
                    'status_code': 200
                }
                
                response_body = {
                    'has_error' : '',
                    'message' : '',
                    'order_id'
                    'payment_id' : 'string from bank',
                    'debit_card_number' : 'xxxx-xxxx-xxxx-xxxx'
                }
                '''
                if response.status_code != 200 :
                    raise response.text
                
                else:
                    response_body = response.json()
                    x = BankRequest()
                    x.save_request( 
                               None , 
                               price , 
                               data[ 'callback_url' ] , 
                               response_body['massage'] , 
                               response_body['error'] , 
                               data[ 'order_id' ] , 
                               response_body['payment_id'] , 
                               response_body['debit_card_number'] 
                    )
                               

            except Exception as e :
                x = BankRequest()
                x.save_request( 
                               None , 
                               price , 
                               data[ 'callback_url' ] , 
                               response_body['massage'] , 
                               response_body['error'] , 
                               data[ 'order_id' ] , 
                               response_body['payment_id'] , 
                               response_body['debit_card_number'] 
                               )
                

            response.close()
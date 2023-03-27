import json
import psycopg2

def lambda_handler(event, context):
    user = event['request']['userAttributes']
    print('UserAttributes\n\n', user)

    try:
        conn = psycopg2.connect((os.getenv('CONNECTION_URL')))
        cur = conn.cursor()
        cur.execute("INSERT INTO users (display_name, handle, cognito_user_id) VALUES(%s, %s, %s)", (user['name'], user['email'], user['sub']))
        conn.commit()
        cur.close()
        conn.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        
    finally:
        print('Database connection closed.')

    return event
import psycopg2

# connecting with postgres
try:
    connection = psycopg2.connect(user="sheet_user",
                                  password="12345",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="bot_server")

    cursor = connection.cursor()

except (Exception, psycopg2.Error) as error:
    print("Error while fetching data from PostgreSQL", error)


def in_db(q):
    cursor.execute(q)
    connection.commit()


def cache_search(q):
    try:
        cursor.execute(q)
        # Selecting rows from recents table using cursor.fetchall
        mobile_records = cursor.fetchall()

        # get each row and it's columns values
        response = "Related recent searches are --->"
        for row in mobile_records:
            response += row[0] + "  "
        if response:
            return response
        else:
            return "No recent found"
    except Exception as err:
        print("Exception occurred {}".format(err))
        return "Bot Server Connection failed"

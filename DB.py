import psycopg2

def in_db(q):
    # connecting with postgres
    try:
        connection = psycopg2.connect(user="uziblvfmjfwkkm",
                                      password="b576fbc515854d9120f740607161075dd6ca450cd9359e207940614107ad2dd4",
                                      host="ec2-184-72-236-57.compute-1.amazonaws.com",
                                      port="5432",
                                      database="d4ajbjn3rbssfq")

        cursor = connection.cursor()

    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)
    cursor.execute(q)
    connection.commit()


def cache_search(q):
    # connecting with postgres
    try:
        connection = psycopg2.connect(user="uziblvfmjfwkkm",
                                      password="b576fbc515854d9120f740607161075dd6ca450cd9359e207940614107ad2dd4",
                                      host="ec2-184-72-236-57.compute-1.amazonaws.com",
                                      port="5432",
                                      database="d4ajbjn3rbssfq")

        cursor = connection.cursor()

    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)

    try:
        cursor.execute(q)
        # Selecting rows from recents table using cursor.fetchall
        mobile_records = cursor.fetchall()

        # get each row and it's columns values
        response = "Related recent searches are --->"
        res = ""
        for row in mobile_records:
            res += row[0] + "  "
        if res:
            return response + res
        else:
            return "No recent found"
    except Exception as err:
        print("Exception occurred {}".format(err))
        return "Bot Server Connection failed"

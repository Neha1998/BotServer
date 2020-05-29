from googlesearch import search
from DB import in_db

# implements google search
def g_search(self, query):
    try:
        # to maintain history of the searched words mapped with each user.
        exc = "insert into recents (user_id, searched) values( {} , '{}')".format(self.user.id, query)
        in_db(exc)

        response = "Top 5 links related to {} are ----".format(query)
        for res in search(query, tld="co.in", num=5, stop=5, pause=2):
            response += res + "  "
        return response

    except Exception as err:
        print("Error occured in searching {}".format(err))
        return "Something failed"

from db import DB

class User:
    def getProfileApi(self):

        table = "profiles_api"
        column = "id_twitter, key_consumer, secret_consumer, key_access, secret_access"
        order = "timestamp"
        condition = "ORDER BY "+order+" LIMIT 0,1"

        ob = DB()
        id_row, list_rows = ob.querySelect(table, column, condition)

        dict_auth = {}
        try:
            dict_auth['id_twitter'] = list_rows[0][0]
            dict_auth['key_consumer'] = list_rows[0][1]
            dict_auth['secret_consumer'] = list_rows[0][2]
            dict_auth['key_access'] = list_rows[0][3]
            dict_auth['secret_access'] = list_rows[0][4]
        except:
            print "Error: authentication tokens missing in database"

        return dict_auth

    def getTokensApi(self, id_twitter):

        table = "profiles_api"
        column = "id_twitter, key_consumer, secret_consumer, key_access, secret_access"
        condition = "WHERE id_twitter='"+id_twitter+"'"

        ob = DB()
        id_row, list_rows = ob.querySelect(table, column, condition)
        dict_auth = {}
        try:
            dict_auth['id_twitter'] = list_rows[0][0]
            dict_auth['key_consumer'] = list_rows[0][1]
            dict_auth['secret_consumer'] = list_rows[0][2]
            dict_auth['key_access'] = list_rows[0][3]
            dict_auth['secret_access'] = list_rows[0][4]
        except:
            print "Error: authentication tokens missing in database"

        return dict_auth

if __name__ == "__main__":
    ob = User()
    #ob.getProfileApi()
    print ob.getTokensApi("drew_groove")
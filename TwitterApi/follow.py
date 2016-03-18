from flask import Flask, request
from security import Security
from user import User
from db import DB
app = Flask(__name__)

from TwitterApi import app



class Follow:

    @app.route("/follow", methods=['POST'])
    def followUser():
        ob_db = DB()
        ob_user = User()
        ob_security = Security()
        try:
            data = request.get_json()
        except:
            print "Error: invalid json input data"

        if "profile_api" not in data.keys():
            dict_auth = ob_user.getProfileApi()
            profile_api = dict_auth['id_twitter']
            print profile_api
        else:
            profile_api = data['profile_api']
            dict_auth = ob_user.getTokensApi(profile_api)

        client = ob_security.authentication(dict_auth)
        print data.keys()
        if "profile_user" in data.keys():
            profile_user = data['profile_user']
        else:
            id_row, list_rows = ob_db.querySelect("profiles_users", "id_twitter", "WHERE id NOT IN (SELECT id_profiles_users from followers_active) LIMIT 0,1")
            profile_user = list_rows[0][0]

        endpoint_follow = "https://api.twitter.com/1.1/friendships/create.json?screen_name="+profile_user+"&follow=true"
        response, data = client.request(endpoint_follow, "POST")

        ob_db.queryUpdate("profiles_api", "timestamp", "CURRENT_TIMESTAMP", "id_twitter="+"'"+profile_api+"'")

        #insert into database - table followers active
        id_row, list_rows = ob_db.querySelect("profiles_users", "id", "WHERE id_twitter="+"'"+profile_user+"'"+" LIMIT 0,1")
        id_profile_user = list_rows[0][0]
        id_row, list_rows = ob_db.querySelect("profiles_api", "id", "WHERE id_twitter="+"'"+profile_api+"'"+" LIMIT 0,1")
        id_profile_api = list_rows[0][0]

        columns = "id_profiles_api, id_profiles_users"
        values = str(id_profile_api)+", "+str(id_profile_user)

        ob_db.queryInsert("followers_active", columns, values)


        return data




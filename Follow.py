import oauth2 as oauth
import json
i

class Follow:
    def __init__(self):
        print "follow class init method"

    def authentication(self):

        CONSUMER_KEY = "5vc4GEXUzY7jFAYefgzwQVqGU"
        CONSUMER_SECRET = "x0WhWwqcMYGKVfVe6lBO3LE2FjMlkSRszXYWgzl55c1nTOj3jY"
        ACCESS_KEY = "4844933649-4NIkjCdA3OJdPbZOnLSa333UsMDZz35cuCcQXE5"
        ACCESS_SECRET = "f4fHPEXo8b34Kf4HhVPGTr7poy5c8f3sK2HoHsBU6Kwbp"

        consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
        access_token = oauth.Token(key=ACCESS_KEY, secret=ACCESS_SECRET)
        client = oauth.Client(consumer, access_token)

        timeline_endpoint = "https://api.twitter.com/1.1/statuses/home_timeline.json"
        follow_endpoint = "https://api.twitter.com/1.1/friendships/create.json?screen_name=sarahlane&follow=true"
        response, data = client.request(follow_endpoint, "POST")


        print response
        print data
        """tweets = json.loads(data)
        for tweet in tweets:
            print tweet['text']"""

if __name__ == "__main__":
    ob = Follow()
    ob.authentication()
816214
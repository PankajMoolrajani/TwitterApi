import oauth2 as oauth

class Security:

    def authentication(self, dict_auth):
        key_consumer = dict_auth['key_consumer']
        secret_consumer = dict_auth['secret_consumer']
        key_access = dict_auth['key_access']
        secret_access = dict_auth['secret_access']

        consumer = oauth.Consumer(key=key_consumer, secret=secret_consumer)
        access_token = oauth.Token(key=key_access, secret=secret_access)

        client = oauth.Client(consumer, access_token)

        return client
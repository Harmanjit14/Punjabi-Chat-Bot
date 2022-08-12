from python_graphql_client import GraphqlClient
from datetime import datetime

class Credentials:

    token = None

    def setToken(self, token):
        self.loggedIn = True
        self.token = token

    def getToken(self):
        if self.token == None:
            return 'JWT '
        return self.token


def login(USERNAME, PASSWORD, client):

    query = """
        mutation token ($uname: String!, $pass: String!) {
        tokenAuth (username: $uname, password: $pass) {
            token
        }
        }
    """
    params = {"uname": USERNAME,
              "pass": PASSWORD,
              }

    result = client.execute(query=query, variables=params)
    token = 'JWT '
    if result['data']['tokenAuth']['token'] != None:
        token = f"JWT {result['data']['tokenAuth']['token']}"
        return token

    else:
        return token


def get_migration_certificate(client):

    query = """
    {
        migrationCertificate
    }
    """
    try:
        result = client.execute(query=query)
        if result['data']['migrationCertificate'] == 'Success':
            return "ਮੈਂ ਤੁਹਾਡਾ ਮਾਈਗ੍ਰੇਸ਼ਨ ਸਰਟੀਫਿਕੇਟ ਬਣਾਇਆ ਹੈ ਅਤੇ ਤੁਹਾਨੂੰ ਡਾਕ ਰਾਹੀਂ ਭੇਜ ਦਿੱਤਾ ਹੈ। ਕ੍ਰਿਪਾ ਜਾਂਚ ਕਰੋ"
        else:
            return "ਮਾਫ਼ ਕਰਨਾ ਮੈਂ ਤੁਹਾਡਾ ਮਾਈਗ੍ਰੇਸ਼ਨ ਸਰਟੀਫਿਕੇਟ ਬਣਾਉਣ ਵਿੱਚ ਅਸਮਰੱਥ ਸੀ"

    except:
        return "ਮਾਫ਼ ਕਰਨਾ ਮੈਂ ਤੁਹਾਨੂੰ ਲੌਗਇਨ ਕਰਨ ਵਿੱਚ ਅਸਮਰੱਥ ਸੀ"


def case_selector(id, obj):

    # Server Connection
    server_client = GraphqlClient(endpoint="http://localhost:8000/graphql", headers={
        'Authorization': obj.token,
    })

    if id == 0:
        time=f'{datetime.now().hour%12}:{datetime.now().minute}'
        if datetime.now().hour>12:
            time+='PM'
        else:
            time+='AM'
        return time
    if id == 1:
        return get_migration_certificate(server_client)
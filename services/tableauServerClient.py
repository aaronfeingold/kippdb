import tableauserverclient as TSC
import json
import ipdb

def run():
    secrets = json.loads(open("secrets.json").read())

    username = secrets["users"]["user2"]["username"]
    password = secrets["users"]["user2"]["password"]
    server = secrets["servers"]["server2"]

    tableau_auth = TSC.TableauAuth(username, password)
    server = TSC.Server(server)
    
    with server.auth.sign_in(tableau_auth):
        all_datasources, pagination_item = server.datasources.get()
        print("\nThere are {} datasources on site: ".format(pagination_item.total_available))
        print([datasource.name for datasource in all_datasources])

print(run())
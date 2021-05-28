import tableauserverclient as TSC
import json

secrets = json.loads(open("secrets.json").read())
user = secrets["user"]
psswd = secrets["psswd"]
server = secrets["server"]
tableau_auth = TSC.TableauAuth(user, psswd)
server = TSC.Server(server)

with server.auth.sign_in(tableau_auth):
    all_datasources, pagination_item = server.datasources.get()
    print("\nThere are {} datasources on site: ".format(pagination_item.total_available))
    print([datasource.name for datasource in all_datasources])
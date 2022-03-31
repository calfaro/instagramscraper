from instagram_private_api import Client, ClientCompatPatch
import json

user_name = 'fuentes_humanas@socialmedia.exilecontent.com'
password = 'fuent**n4hC!tE'
user_id = 45167175009
updates = []

api = Client(user_name,password)
results = api.user_feed(user_id)
updates.extend(results.get('items', []))

next_max_id = results.get('next_max_id')
while next_max_id:
	results = api.user_feed(user_id, max_id=next_max_id)
	updates.extend(results.get('items', []))
	if len(updates) >= 30: # get 30 or so
		break
	next_max_id = results.get('next_max_id')

updates.sort(key=lambda x: x['pk'])
# print list of IDs
print(json.dumps([u['pk'] for u in updates], indent=2))


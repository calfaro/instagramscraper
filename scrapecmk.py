from instagram_private_api import Client, ClientCompatPatch

user_name = 'fuentes_humanas@socialmedia.exilecontent.com'
password = 'fuent**n4hC!tE'
user_id = '45167175009'

api = Client(user_name, password)
results = api.user_feed(user_id)
print results
items = [item for item in results.get('feed_items', [])
         if item.get('media_or_ad')]
for item in items:
    # Manually patch the entity to match the public api as closely as possible, optional
    # To automatically patch entities, initialise the Client with auto_patch=True
    ClientCompatPatch.media(item['media_or_ad'])
    print(item['media_or_ad']['code'])

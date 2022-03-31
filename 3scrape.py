from instagram_private_api import Client, ClientCompatPatch
import json

user_name = 'fuentes_humanas@socialmedia.exilecontent.com'
password = 'fuent**n4hC!tE'
user_id = 45167175009

api = Client(user_name,password)
results = api.user_feed(user_id)
#print(results[2])
#for item in results.get('items')
#	print (item)


x=results.get('items')
y=x[3].get('caption')
#jason=json.dumps(x[3], indent=4, separators=(". ", " = "))
#print(jason.get('caption'))
media = y.get('media_id')
comentarios = api.media_comments(media)
jasoncomentarios=json.dumps(comentarios , indent=4, separators=(". ", " = "))
print(jasoncomentarios)

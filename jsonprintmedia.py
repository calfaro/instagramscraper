from instagram_private_api import Client, ClientCompatPatch
import json

user_name = 'fuentes_humanas@socialmedia.exilecontent.com'
password = 'fuent**n4hC!tE'
user_id = 45167175009
media_id = 2688826668469226351

api = Client(user_name,password)

comentarios = api.media_comments(media_id)
jasoncomentarios=json.dumps(comentarios , indent=4, separators=(". ", " = "))
print(jasoncomentarios)

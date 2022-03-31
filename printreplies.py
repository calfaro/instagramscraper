from instagram_private_api import Client, ClientCompatPatch
import json

user_name = 'fuentes_humanas@socialmedia.exilecontent.com'
password = 'fuent**n4hC!tE'
media_id = 2688826668469226351
comment_id = 17992026775387285

api = Client(user_name,password)

replies = api.comment_replies(media_id,comment_id)

jasonreplies=json.dumps(replies , indent=4, separators=(". ", " = "))
print(jasonreplies)



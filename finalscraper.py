from instagram_private_api import Client, ClientCompatPatch

user_name = 'fuentes_humanas@socialmedia.exilecontent.com'
password = 'fuent**n4hC!tE'
user_id = 45167175009
kargs = 'max_id=2682894401330297241'

api = Client(user_name,password)
user_feed_results = api.user_feed(user_id)
feed_results = user_feed_results.get('items')
for item in feed_results:
	caption=item.get('caption')
	media=caption.get('media_id')
	code=item.get('code')
	print('\n\nhttps://instagram.com/p/' + code + ' ' + str(media))
	
	comentarios=api.media_comments(media)

	allcomments=comentarios.get('comments')
	
	for comment in allcomments:
		print('\t' + comment['user']['username'] + ' | ' + comment['text'] + ' | ' + str(comment['child_comment_count']))
		if comment['child_comment_count'] :
			allreplies=api.comment_replies(media,comment['pk'])
			for reply in allreplies['child_comments']:
				print('\t\t' + reply['user']['username'] + ' | ' + reply['text']) 






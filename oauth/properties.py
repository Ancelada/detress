class Properties():
	def __init__(self):
		self.vk_settings = {
		    'code_url' : 'https://oauth.vk.com/authorize?',
		    'token_url' : 'https://oauth.vk.com/access_token?',
		    'id' : '6104124',
		    'redirect' : 'http://localhost:19000/oauth/vk/',
		    'display' : 'popup',
		    'scope' : '',
		    'type' : 'code',
		    'api' : '5.65',
		    'secret' : 'zEL28lO6kAjLGMuZDHsS',
		}


		self.fb_settings = {
		    'code_url' : 'https://www.facebook.com/v2.9/dialog/oauth?',
		    'token_url' : 'https://graph.facebook.com/v2.9/oauth/access_token?',
		    'id' : '1378085518911737',
		    'redirect' : 'http://localhost:19000/oauth/fb/',
		    'state' : 'name.of.site',
		    'display' : 'popup',
		    'scope' : '',
		    'type' : 'code',
		    'secret' : 'c2b0c6681b8615bdfd2bc1cce7ca5265',
		}


		self.gp_settings = {
		    'code_url' : 'https://accounts.google.com/o/oauth2/auth?',
		    'id' : '53152099983-ggkhlqbsl7bonh04088ao2undi13m1qh.apps.googleusercontent.com',
		    'redirect' : 'http://localhost:19000/oauth/gp/',
		    'display' : '',
		    'scope' : 'https://www.googleapis.com/auth/userinfo.profile',
		    'type' : 'code',
		    'secret' : '-gWMR7IvEOTuh_hsfTHGkrCH',
		}


		self.ya_settings = {
		    'code_url' : 'https://oauth.yandex.ru/authorize?',
		    'id' : 'cc9a482c51824409acfd01bb51c75c02',
		    'secret' : '464cb641169447a08fd8f560f061cf07',
		    'type' : 'code',
		    'display' : 'popup',
		    'state' : 'name.of.site',
		}
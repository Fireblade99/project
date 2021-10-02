import requests

token = '2043454840:AAE-2ZwCoQkwW7JWq1ozyk3hXL2f3cew8SA'
chat_id = '674891991'
text = 'Test_2'

def sendTelegram():
	api = 'https://api.telegram.org/bot'
	method = api + token + '/sendMessage'

	req = requests.post(method, data={
		'chat_id': chat_id,
		'text': text	
		})

sendTelegram()
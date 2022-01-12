

def create_creater(message):
	if message == 'ありがとう':
		message = 'どういたしまして'
	test_message = [
		{
			'type': 'text',
			'text': message,
		}
	]
	return test_message
country = input('where do you come from: ')
age = input('type your age: ')
if country == 'taiwan':
	if int(age) >= 18:
		print('you can get a license')
	else:
		print('not yet')
elif country == 'usa':
	if int(age) >= 16:
		print('you can get a license')
	else:
		print('not yet')
else:
	print('u can only type either taiwan or usa')
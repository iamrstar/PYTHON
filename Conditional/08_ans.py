password = "123456"
if len(password) < 6:
    print('weak')
elif len(password) < 10:
    print('medium')
else:
    print('strong')

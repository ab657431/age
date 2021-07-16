drive = input('有沒有開過車?(yes or no) ')
if drive != '有' and drive != '沒有':
	print('只能輸入有或沒有')
	raise SystemExit
age = input('年齡: ')
age = int(age)
if drive == 'yes' and age < 18:
	print('沒18怎麼可以開車呢')
elif drive == 'yes' and age >= 18:
	print('你通過測驗了')
elif drive == 'no' and age < 18:
	print('不錯，沒有偷偷開車')
elif drive == 'no' and age > 18:
	print('開車很好玩唷,可以去試試看')
else:
	print('只能輸入有或沒有')
	


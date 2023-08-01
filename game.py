import random
import eel

def play():
	number = random.randint(1,3)

	if number == 1:
		return 'камень'
	elif number == 2:
		return 'ножницы'
	else:
		return 'бумага'

def main():
	@eel.expose
	def winn(user):
		syte = play()

		if user == syte:
			return f'У нас ничья! \n Мой ответ: {syte}, Ваш ответ: {user}'
		elif (syte == 'камень' and user == 'ножницы') or (syte == 'бумага' and user == 'камень') or (syte == 'ножницы' and user == 'бумага'):
			return f'Вы проиграли! \n Мой ответ: {syte}, Ваш ответ: {user}'
		else:
			return f'Вы выиграли! \n Мой ответ: {syte}, Ваш ответ: {user}'
		
	eel.init('web')
	eel.start('index.html', mode='telegram')
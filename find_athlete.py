import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


import users


User = users.User
Athelete = users.Athelete


def find_athelete(user, session):
	"""
	выводит на экран двух атлетов: ближайшего по дате рождения к данному пользователю 
	и ближайшего по росту к данному пользователю
	"""
	# находим все записи в таблице Athelete, у которых поле birthdate ,больше или равно birthdate пользователя
	birthdate_gt = session.query(Athelete).filter(Athelete.birthdate >= user.birthdate).order_by(Athelete.birthdate).all()

	print("Найдено атлетов, ближайших по дате рождения : {count}".format(count = len(birthdate_gt)))
	if len(birthdate_gt):
		for i in range(2):
			print(birthdate_gt[i].id, birthdate_gt[i].name, birthdate_gt[i].gender, birthdate_gt[i].birthdate)

	# находим все записи в таблице Athelete, у которых поле birthdate ,больше или равно birthdate пользователя
	height_gt = session.query(Athelete).filter(Athelete.height >= user.height).order_by(Athelete.height).all()

	print("Найдено атлетов, ближайших по росту : {count}".format(count = len(height_gt)))
	if len(height_gt):
		for i in range(2):
			print("id: {id} name: {name} gender: {gender} height: {height}".format(height_gt[i].id, height_gt[i].name, height_gt[i].gender, height_gt[i].height))

def main():
	session = users.connect_db()
	id = int(input("Введите id пользователя (целое число):"))
	user = users.find_user(id, session)
	if user != None:
		find_athelete(user, session)



if __name__ == '__main__':
	main()

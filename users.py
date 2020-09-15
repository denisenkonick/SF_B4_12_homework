import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


DB_PATH = 'sqlite:///sochi_athletes.sqlite3'
Base = declarative_base()

class User(Base):
	"""docstring for User"""
	__tablename__ = 'user'
	id = sa.Column(sa.Integer, primary_key=True, autoincrement='auto')
	first_name = sa.Column(sa.Text)
	last_name = sa.Column(sa.Text)
	gender = sa.Column(sa.Text)
	email = sa.Column(sa.Text)
	birthdate = sa.Column(sa.Text)
	height = sa.Column(sa.Float)

class Athelete(Base):
	"""docstring for User"""
	__tablename__ = 'athelete'
	id = sa.Column(sa.Integer, primary_key=True, autoincrement='auto')
	age = sa.Column(sa.Integer)
	birthdate = sa.Column(sa.Text)
	gender = sa.Column(sa.Text)
	height = sa.Column(sa.Float)
	name = sa.Column(sa.Text)
	weight = sa.Column(sa.Integer)
	gold_medals = sa.Column(sa.Integer)
	silver_medals = sa.Column(sa.Integer)
	bronze_medals = sa.Column(sa.Integer)
	total_medals = sa.Column(sa.Integer)
	sport = sa.Column(sa.Text)
	country = sa.Column(sa.Text)


def user_registration():
	first_name = input('first name > ')
	last_name = input('last name > ')
	gender = input('gender (Male / Female) > ')
	email = input('email > ')
	birthdate = input('birthdate > ')
	height = int(input ('height > '))
	#user_id = uuid.uuid4())

	new_user = User(
		#id = user_id,
		first_name = first_name,
		last_name = last_name,
		gender = gender,
		email = email,
		birthdate = birthdate,
		height = height)

	return new_user

def connect_db():
	"""
	Устанавливает соединение к базе данных, создает таблицы, если их еще нет и возвращает объект сессии 
	"""
	#создаем соединение к базе данных
	engine = sa.create_engine(DB_PATH)

	# создаем описанные таблицы
	#Base.metadata.create_all(engine)

	#создаем фаврику сессию
	Sessions = sessionmaker(engine)
	#возвращаем сессию
	return Sessions()

def find_user(id, session):
	"""
	Производит поиск пользователя в таблице user по заданному имени name
	"""
	# находим все записи в таблице User, у которых поле User.first_name совпадает с параметром name
	query = session.query(User).filter(User.id == id)
	if query == None:
		print("None query")

	users = query.all()
	print("Найдено пользователей: {count}".format(count = len(users)))
	for user in users:
		print(user.id, user.first_name, user.last_name, user.gender,user.email, user.birthdate,user.height)
	if len(users):
		return 	query.first()
	else:
		print("Пользователь с id {id} не найден".format(id=id))
		return None

def find_athelete(user, session):
	"""
	Производит поиск пользователя в таблице user по заданному имени name
	"""
	# находим все записи в таблице User, у которых поле User.first_name совпадает с параметром name
	birthdate_gt = session.query(Athelete).filter(Athelete.birthdate >= user.birthdate).order_by(Athelete.birthdate).all()

	print("len(users) : {count}".format(count = len(birthdate_gt)))
	for i in range(2):
		print(birthdate_gt[i].id, birthdate_gt[i].name, birthdate_gt[i].gender, birthdate_gt[i].birthdate)

def main():
	mode = int(input("Выберите режим.\n 1. - Создать пользователя \n 2. - Найти пользователя по id\n"))
	session = connect_db()
	if mode == 1:
		new_user = user_registration()
		session.add(new_user)
		session.commit()
		print('Данные пользователя сохранены')
	elif mode == 2:
		id = int(input("id пользователя -> "))
		user = find_user(id, session)
		if user != None:
			find_athelete(user, session)

	else:
		print("Выбран не корректный режим")


if __name__ == '__main__':
	main()

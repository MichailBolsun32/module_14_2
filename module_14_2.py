import sqlite3

# Код из предыдущего задания

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

for _ in range(10):
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
                    (f'User{_ + 1}', f'example{_ + 1}@gmail.com', (_ +1) * 10, 1000))

cursor.execute('UPDATE Users SET balance = ? WHERE id % 2 = 1', (500,))

cursor.execute('DELETE FROM Users WHERE id % 3 = 1', ())

cursor.execute('SELECT username, email, age, balance FROM Users WHERE age != 60', ())
users = cursor.fetchall()
# for user in users:
#     print(f'Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}')

# Удалите из базы данных not_telegram.db запись с id = 6.
cursor.execute('DELETE FROM Users WHERE id == 6', ())

#Подсчитать общее количество записей.
cursor.execute('SELECT COUNT(*) FROM Users')
number = cursor.fetchone()[0]

#Посчитать сумму всех балансов.
cursor.execute('SELECT SUM(balance) FROM Users')
sum_ = cursor.fetchone()[0]

#Вывести в консоль средний баланс всех пользователей.
print(sum_/ number)

connection.commit()
connection.close()
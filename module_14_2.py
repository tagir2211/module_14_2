import sqlite3

connection = sqlite3.connect("not_telegram.db")
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

cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")

# for i in range(1, 11):
#     cursor.execute("INSERT INTO Users(username, email, age, balance) VALUES (?, ?, ?, ?)",
#                    (f'User{i}', f'example{i}@gmail.com', f'{i * 10}', 1000))

for i in range(1, 11, 2):
    cursor.execute("UPDATE Users SET balance = ? WHERE id = ?", (500, i))

for i in range(1, 11, 3):
    cursor.execute("DELETE FROM Users WHERE id = ?", (i,))

# cursor.execute("DELETE FROM Users")
cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != ?", (60,))

users = cursor.fetchall()

for user in users:
    print('Имя: ', end='')
    print(user[0], end='\t| ')
    print('Почта: ', end='')
    print(user[1], end='\t| ')
    print('Возраст: ', end='')
    print(user[2], end='\t| ')
    print('Баланс: ', end='')
    print(user[3])

# Удалите из базы данных not_telegram.db запись с id = 6.
cursor.execute("DELETE FROM Users WHERE id = ?", (6,))
# Подсчитать общее количество записей.
cursor.execute("SELECT COUNT(*) FROM Users")
total = cursor.fetchone()[0]
print(total)
# Посчитать сумму всех балансов.
cursor.execute("SELECT SUM(balance) FROM Users")
summ = cursor.fetchone()[0]
print(summ)
# Вывести в консоль средний баланс всех пользователей.
cursor.execute("SELECT AVG(balance) FROM Users")
avg = cursor.fetchone()[0]
print(avg)
avg1 = summ/total
print(avg == avg1)


connection.commit()
connection.close()

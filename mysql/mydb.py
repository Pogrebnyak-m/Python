import pymysql 
connection = pymysql.connect('localhost', 'student', '135790', 'mydb')

try:
    with connection.cursor() as cursor:
        sql = "INSERT INTO `student` (`idStudent`, `Surname`, `Name`, `Second Name`, `home`) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql, ('24', 'Иванов', 'Иван', 'Иванович', '4'))
    connection.commit()

    with connection.cursor() as cursor:
        sql = "UPDATE `mydb`.`student` SET `Surname` = 'Кранс' WHERE (`idStudent` = %s);"
        cursor.execute(sql, ('23'))
        
    with connection.cursor() as cursor:
        cursor.execute("SELECT `idStudent`, `Surname`, `Name`, `Second Name`, `city name` FROM student INNER JOIN city ON home = idCity;")
        rows = cursor.fetchall()
        for row in rows:
            print(f'{row[0]} {row[1]} {row[2]} {row[3]} {row[4]}')
finally:
    connection.close()














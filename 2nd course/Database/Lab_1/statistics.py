from Book import DB
import matplotlib.pyplot as plt
import time
import random
import string
import tabulate


def randomString(stringLength=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


db = DB("Test")

complexity = [10, 100, 1000, 10000, 100000]
time_add = []
time_find = []
time_delete = []

for amount in complexity:
    db.clear_db()
    time_start = time.time()
    for i in range(amount):
        db.add_record(i, {"id":f"{i}", "title":f"{randomString()}", "author":f"{randomString()}",
                          "year":f"{random.seed()}", "price":f"{random.seed()}"})
    time_add.append((time.time() - time_start) / amount)
    time_start = time.time()

    for i in db.field.keys():
        db.get_records_by_key(i)
    time_find.append((time.time() - time_start) / len(db.field.keys()))
    time_start = time.time()

    for i in range(amount):
        db.delete_by_book_id(i)
    time_delete.append((time.time() - time_start) / amount)

plt.figure()
plt.subplot(3,1,1)
plt.plot(complexity, time_add, 'r')
plt.ylabel('Время')
plt.xlabel('Количество записей в БД')
plt.title('Add')
plt.subplot(3,1,2)
plt.plot(complexity, time_find, 'g')
plt.ylabel('Время')
plt.xlabel('Количество записей в БД')
plt.title('Find')
plt.subplot(3,1,3)
plt.plot(complexity, time_delete, 'b')
plt.ylabel('Время')
plt.xlabel('Количество записей в БД')
plt.title('Delete')
plt.show()

complexity.insert(0, 'Iterations')
time_add.insert(0, 'Add')
time_find.insert(0, 'Find')
time_delete.insert(0, 'Delete')

print(tabulate.tabulate([complexity, time_add, time_find, time_delete], tablefmt="github"))

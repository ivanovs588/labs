import random
import os

def connect_user():
    auth_users = []
    files = {}
    while True:
        i = yield 
        i = i.split()
        x, y = i[0], i[1]
        if x == 'auth':
            auth_users.append(y)
            files[y] = open (str(y)+'.txt', 'w')
        elif x == 'disconnect':
            auth_users.remove(y)
            files[y].close()
        elif x in auth_users:
            files[x].write(y+'\n')

def user_messege(username):
    for i in range(random.randint(10, 20)):
        yield f"{username} message{i}"

def establish_connection(auth=True):
    id = f"{random.randint(0,100000000):010}"
    if auth:
        #сначала все пытаются написать что они авторизовались 
        yield f"auth {id}"
    #при следующих обращениях будут выводится их сообщения 
    yield from user_messege(id)
    if auth:
        #в конце они отключаются 
        yield f"disconnect {id}"

def connection():
    #создаем некоторое количество подключений
    connections = [establish_connection(True) for i in range(10)]
    #создаем несколько неавторизованных пользователей
    connections.append(establish_connection(False))
    connections.append(establish_connection(False))

    while len(connections):
        conn = random.choice(connections)
        try:
            yield next(conn)
        except StopIteration:
            del connections[connections.index(conn)]


connect = connect_user()
next(connect)
for i in connection():
    connect.send(i)

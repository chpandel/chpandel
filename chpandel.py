#!/usr/bin/python

import psycopg2
import psycopg2.extras
import re

def bd_connect():
    try:
        conn = psycopg2.connect("host='localhost' dbname='test' user='postgres' password='postgres'")
        print('[INFO] Connection success !!!')
    except:
        print('[INFO] Connection error !!!')
    
    return conn


def bd_execute(sql, one_row, *args):
    #Подсоединение к бд и создание курсора-словаря
    conn = bd_connect()
    cur = conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
    
    #Подстановка аргументов
    for i, item in enumerate(args[0]):
        #экранирование, если строка
        item = "'" + item + "'" if isinstance(item, str) else str(item)
        sql = re.sub('\$' + str(i + 1), item, sql)
    
    data = None
    cur.execute(sql)
    
    try:
        data = cur.fetchone() if one_row else cur.fetchall()
    except:
        pass
    
    conn.commit()
    cur.close()
    conn.close()

    return data


def SqlQuery(sql, *args):
    return bd_execute(sql, False, args)


def SqlQueryRecord(sql, *args):
    return bd_execute(sql, True, args)
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 17:36:26 2018

@author: jrbrad
"""

import pymysql as mySQL

class mysql:
    "Jim Bradley's MySQL database package"
    def __init__(self,dbName,username, password, boolRemote, remoteIP=None):
        self.username = username
        self.password = password
        self.dbName = dbName
        if not boolRemote:
            self.ip = '127.0.0.1'
        else:
            self.ip = remoteIP

    def connect(self):
        cnx = mySQL.connect(user=self.username, passwd=self.password,
                            host=self.ip, db=self.dbName)
        return cnx
    
    def logEntry(self, user_name, status_action, filename):
        cnx = self.connect()
        cursor = cnx.cursor()
        cursor.execute("CALL spInsertLog(%s, %s, %s);" , (user_name, status_action, filename))
        cursor.close()
        cnx.commit()
        cnx.close
    
    def insertResults(self, results, participant,result1,result2,result3,result4): 
        cnx = self.connect()                       
        cursor = cnx.cursor()
        sql = 'CALL spInsertResults('
        sql += ''.join('%s, ' for x in results)
        sql = sql[:len(sql)-2]
        sql += ');'
        cursor.execute(sql, results)
        cursor.close()
        cnx.commit()
        cnx.close
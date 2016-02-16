#!/usr/bin/python
#coding: utf-8

__author__    = "jnmcclai"
__copyright__ = "Copyright 2016, Adtran, Inc."
__version__   = "2.7.7"

import logging
import MySQLdb

class database():
    """
    MySQL phpmyadmin python database manipulation module

    args = {
                ip: the database server IP address
                port: the database server port (3306)
                database: the database name
                username: database username credential
                password: database password credential
            }

    Requires MySQLdb module - try 'pip install mysqlclient'
    Ideally requires external file containing hashed credentials
    """

    def __init__(self, ip, port, database, username, pwd):
        """
        Class initialization
        """
        self.ip = ip
        self.port = port
        self.database = database
        self.username = username
        self.pwd = pwd

    def db_connect(self):
        """
        Connect to a database
        """
        self.db = MySQLdb.connect(host=self.ip, user=self.username, passwd=self.pwd, db=self.database)
        self.cur = self.db.cursor()


    def db_push(self):
        """
        Push data to a MySQL database
        """

    def db_pull(self, sql_index=None, table=None):
        """
        Pull data from a MySQL database

        args = {
                    sql_index: SQL command
                    table: database table to retrieve from
                }
        """
        #attempting an example
        self.cur.execute("SELECT * FROM {0} WHERE 1".format(table))
        for row in self.cur.fetchall():
            print row[1]

    def db_truncate(self):
        """
        Truncate data from a MySQL database
        """

if __name__ == '__main__':
    """
    MySQL database manipulation module
    """

    ###########################################
    #EXAMPLES
    ###########################################

    #initialize some example variables
    db_ip = '10.21.1.181'
    db_port = 3306
    db_database = 'bsmEoxLoadTestBed'
    db_table = 'temperature'
    db_username = 'pqgen'
    db_pwd = 'pqgen'

    #initiate an instance
    instance = database(db_ip, db_port, db_database, db_username, db_pwd)
    instance.db_connect()
    instance.db_pull(table=db_table)

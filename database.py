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
                table: a database table name
                username: database username credential
                password: database password credential
            }

    Requires MySQLdb module - try 'pip install mysqlclient'
    Ideally requires external file containing hashed credentials
    """

    def __init__(self, ip, port, database, table, username, pwd):
        """
        Class initialization
        """
        self.ip = ip
        self.port = port
        self.database = database
        self.table = table

    def db_connect(self):
        """
        Connect to a database
        """
        self.db = MySQLdb.connect(host=self.ip, port=self.port, user=self.username, db=self.database)
        self.cur = self.db.cursor()

        self.cur.execute()

    def db_push(self):
        """
        Push data to a MySQL database
        """

    def db_pull(self):
        """
        Pull data from a MySQL database
        """
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
    db_database = 'pqGeneral'
    db_table = 'pqGeneral'
    db_username = 'pqgen'
    db_pwd = 'pqgen'
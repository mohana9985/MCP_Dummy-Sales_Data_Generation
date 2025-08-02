from mcp.server.fastmcp import FastMCP
import mysql.connector
import os 
from dotenv import load_dotenv
from typing import Union
from mysql.connector.pooling import PooledMySQLConnection
from mysql.connector.abstracts import MySQLConnectionAbstract


def get_mysql_connection() -> Union[PooledMySQLConnection, MySQLConnectionAbstract]:
    """Establishes a connection to the MySQL database
    
    Returns:
        Union[PooledMySQLConnection, MySQLConnectionAbstract]: A connection object to the MySQL database.
    """
    load_dotenv()
    connection= mysql.connector.connect(
        host= os.getenv("MYSQL_HOST"),
        user= os.getenv("MYSQL_USER"),
        password= os.getenv("MYSQL_PASSWORD"),
        database= os.getenv("MYSQL_DATABASE")
    )
    return connection
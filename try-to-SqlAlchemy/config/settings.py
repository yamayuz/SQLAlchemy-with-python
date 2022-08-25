import os
from typing import Optional, TypedDict


class MysqlConfType(TypedDict):
    host: Optional[str]
    port: Optional[str]
    database: Optional[str]
    username: Optional[str]
    password: Optional[str]


MYSQL_CONF: MysqlConfType = {
    'host': os.getenv('DB_HOST', None),
    'port': os.getenv('DB_PORT', None),
    'database': os.getenv('DB_DATABASE', None),
    'username': os.getenv('DB_USERNAME', None),
    'password': os.getenv('DB_PASSWORD', None),
}

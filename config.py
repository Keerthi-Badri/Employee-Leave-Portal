import os

class Config:
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', 'Hanuma@18')  # Default password if not set in .env
    MYSQL_DB = 'leave_management_system'

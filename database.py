from sqlalchemy import create_engine
from sqlalchemy import text

# Replace 'username', 'password', 'hostname', and 'database_name' with your actual MySQL credentials and database name
#SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://welagedara:shehan@35.223.166.86/lost_and_found_db'
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:shehan@localhost/lost_and_found_db'
engine = create_engine(SQLALCHEMY_DATABASE_URI)




from sqlalchemy import create_engine
from sqlalchemy import text

# Replace 'username', 'password', 'hostname', and 'database_name' with your actual MySQL credentials and database name
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://username:password@hostname/database_name'
engine = create_engine(SQLALCHEMY_DATABASE_URI)

def load_latest_items():
    with engine.connect() as conn:
        query = text("SELECT name, date, description, 'Lost' AS status FROM lost_items UNION SELECT name, date, description, 'Found' AS status FROM found_items ORDER BY date DESC LIMIT 10")
        result = conn.execute(query)
        columns = result.keys()
        result_items = []
        for row in result.fetchall():
            result_items.append(dict(zip(columns, row)))
        return result_items

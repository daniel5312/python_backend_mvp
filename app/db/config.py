# app/db/config.py

DB_HOST = "localhost"
DB_PORT = "3307"
DB_NAME = "python_bakdend"
DB_USER = "root"
DB_PASSWORD = ""

DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

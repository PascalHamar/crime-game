from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db_user = os.getenv('POSTGRESQL_USER')
db_password = os.getenv('POSTGRESQL_PASSWORD')
db_database = os.getenv('POSTGRESQL_DATABASE')
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://'+ db_user + ':' + db_password + '@localhost/' + db_database
db = SQLAlchemy(app)

@app.route('/test_db')
def test_db():
    try:
        result = db.engine.execute('SELECT 1')
        return str(result.fetchone())
    except Exception as e:
        return str(e)

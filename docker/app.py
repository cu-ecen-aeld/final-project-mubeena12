import os
from flask import Flask, request, jsonify
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import MetaData, Table, select

app = Flask(__name__)

# Replace with your PostgreSQL connection string
DATABASE_URL = os.getenv('DATABASE_URL')
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

Base = declarative_base()

class WebappTable(Base):
    __tablename__ = 'webapp_table'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))

@app.route("/")
def hello():
    return "Hello, World!\n"

@app.route("/create_table", methods=["POST"])
def create_table():
    # Create the database table if it doesn't exist
    try:
        Base.metadata.create_all(engine)
        return jsonify({"message": "Table created successfully"})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route("/insert_data", methods=["POST"])
def insert_data():
    # Insert data into the table
    try:
        data = request.json
        if "name" in data:
            session = Session()
            new_data = WebappTable(name=data["name"])
            session.add(new_data)
            session.commit()
            session.close()
            return jsonify({"message": "Data inserted successfully"})
        else:
            return jsonify({"error": "Invalid data format"})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route("/tables", methods=["GET"])
def get_tables():
    try:
        metadata = MetaData()
        metadata.reflect(bind=engine)
        tables = metadata.tables.keys()
        return jsonify({"tables": list(tables)})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route("/all_data", methods=["GET"])
def get_all_data():
    try:
        metadata = MetaData()
        metadata.reflect(bind=engine)

        all_data = {}

        for table_name in metadata.tables.keys():
            table = Table(table_name, metadata, autoload=True, autoload_with=engine)
            query = select([table])
            result = engine.execute(query).fetchall()

            # Convert SQLAlchemy result to a list of dictionaries for JSON serialization
            all_data[table_name] = [dict(row) for row in result]

        return jsonify(all_data)
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5500)


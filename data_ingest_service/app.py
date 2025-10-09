from flask import Flask, request, jsonify
import cx_Oracle, os

app = Flask(__name__)

@app.route('/ingest', methods=['POST'])
def ingest_data():
    data = request.get_json()
    conn = cx_Oracle.connect(os.getenv("ORACLE_USER"), os.getenv("ORACLE_PASSWORD"), os.getenv("ORACLE_DSN"))
    cur = conn.cursor()

    try:
        cur.execute("""
            CREATE TABLE raw_data_table (
                id NUMBER GENERATED ALWAYS AS IDENTITY,
                name VARCHAR2(50),
                value NUMBER
            )
        """)
    except:
        pass  # Table may already exist

    cur.execute("INSERT INTO raw_data_table (name, value) VALUES (:1, :2)",
                (data['name'], data['value']))
    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"status": "success", "message": "Data inserted successfully"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

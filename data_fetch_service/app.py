from flask import Flask, jsonify
import cx_Oracle, pandas as pd, os

app = Flask(__name__)

@app.route('/fetch', methods=['GET'])
def fetch_data():
    conn = cx_Oracle.connect(os.getenv("ORACLE_USER"), os.getenv("ORACLE_PASSWORD"), os.getenv("ORACLE_DSN"))
    df = pd.read_sql("SELECT * FROM raw_data_table", conn)
    conn.close()

    output_path = os.getenv("DATA_PATH", "/data/output.tsv")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, sep="\t", index=False)
    return jsonify({"status": "success", "message": f"Data saved to {output_path}"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

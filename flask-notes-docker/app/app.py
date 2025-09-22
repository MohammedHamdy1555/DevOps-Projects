from flask import Flask, request, render_template, jsonify
import mysql.connector
import os

app = Flask(__name__)

# Database connection settings from environment variables
DB_HOST = os.getenv("DB_HOST", "db")
DB_USER = os.getenv("DB_USER", "user")
DB_PASSWORD = os.getenv("DB_PASSWORD", "password")
DB_NAME = os.getenv("DB_NAME", "notesdb")

def get_db_connection():
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

@app.route("/", methods=["GET", "POST"])
def index():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == "POST":
        content = request.form.get("content", "").strip()
        if content:  # reject empty notes
            cursor.execute("INSERT INTO notes (content) VALUES (%s)", (content,))
            conn.commit()

    cursor.execute("SELECT * FROM notes ORDER BY created_at DESC")
    notes = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template("index.html", notes=notes)

@app.route("/notes", methods=["GET"])
def get_notes():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM notes ORDER BY created_at DESC")
    notes = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(notes)

@app.route("/notes", methods=["POST"])
def create_note():
    data = request.json
    content = data.get("content", "").strip()
    if not content:
        return jsonify({"error": "Content cannot be empty"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO notes (content) VALUES (%s)", (content,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Note created successfully"}), 201

@app.route("/healthz")
def healthz():
    try:
        conn = get_db_connection()
        conn.close()
        return jsonify({"status": "ok"}), 200
    except Exception as e:
        return jsonify({"status": "error", "details": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

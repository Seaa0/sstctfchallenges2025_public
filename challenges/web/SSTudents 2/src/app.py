from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

# In-memory SQLite Database connection
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Initialize the database with a table for testing
def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("DROP table users")
    # Create a simple users table with username and password columns
    c.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )
    ''')
    c.execute("INSERT into users (username, password) VALUES (?, ?)", ('fhjakwd', 'kjwfdha'))
    conn.commit()
    print("Database initialized with users.")
    conn.close()


@app.route('/')
def home():
    return render_template_string('''
        <h1>SSTudent Login Page</h1>
        <form action="/login" method="POST">
            <label for="username">Username:</label><br>
            <input type="text" id="username" name="username"><br><br>
            <label for="password">Password:</label><br>
            <input type="password" id="password" name="password"><br><br>
            <input type="submit" value="Login">
        </form>
    ''')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    try:
        # Vulnerable SQL query: directly using user input (deliberate SQLi vulnerability)
        conn = get_db_connection()
        cursor = conn.cursor()
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        cursor.execute(query)
        user = cursor.fetchone()
        conn.close()

        # If the user is found, return a success message
        if user:
            return "Welcome! The flag is sstctf{sq1_1nject10n}"
        else:
            return "Invalid login credentials."

    except sqlite3.OperationalError as e:
        # Catch the operational error and handle it without breaking the app
        return "Invalid input provided. Please try again."
    except sqlite3.DatabaseError as e:
        return "There was a problem with the database. Please try again later."


if __name__ == '__main__':
    init_db()
    get_db_connection()  # Initialize the database
    app.run(debug=True)

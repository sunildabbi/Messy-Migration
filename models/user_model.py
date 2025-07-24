from database import get_connection

def get_all_users():
    conn = get_connection()
    users = conn.execute("SELECT id, name, email FROM users").fetchall()
    conn.close()
    return [dict(u) for u in users]

def get_user_by_id(user_id):
    conn = get_connection()
    user = conn.execute("SELECT id, name, email FROM users WHERE id = ?", (user_id,)).fetchone()
    conn.close()
    return dict(user) if user else None

def create_user(name, email, password_hash):
    conn = get_connection()
    conn.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", (name, email, password_hash))
    conn.commit()
    conn.close()

def update_user(user_id, name, email):
    conn = get_connection()
    conn.execute("UPDATE users SET name = ?, email = ? WHERE id = ?", (name, email, user_id))
    conn.commit()
    conn.close()

def delete_user(user_id):
    conn = get_connection()
    conn.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()

def search_users_by_name(name):
    conn = get_connection()
    users = conn.execute("SELECT id, name, email FROM users WHERE name LIKE ?", (f'%{name}%',)).fetchall()
    conn.close()
    return [dict(u) for u in users]

def login_user(email, password):
    conn = get_connection()
    user = conn.execute("SELECT * FROM users WHERE email = ?", (email,)).fetchone()
    conn.close()
    return user

# CHANGES.md

## 🔍 Major Issues Identified in Legacy Code

1. **SQL Injection Vulnerabilities**  
   - All SQL queries used string interpolation (`f"..."`) directly with user input.

2. **Plaintext Password Storage**  
   - Passwords were stored and compared without hashing.

3. **No Input Validation**  
   - API accepted any input without checking for missing/invalid fields.

4. **Poor Error Handling**  
   - Crashes likely on DB errors or invalid input. No try-except blocks.

5. **Bad Project Structure**  
   - All code was inside a single `app.py` file with mixed concerns.

6. **Unserialized Responses**  
   - Returned `str()` instead of JSON; hard to consume on frontend.

---

## ✅ Changes I Made

1. **Project Restructured**
   - Split into `routes/`, `models/`, `utils/`, and centralized config.

2. **Security Improvements**
   - Used `werkzeug.security` to hash and verify passwords.
   - Used parameterized queries (`?`) to prevent SQL injection.

3. **Validation Added**
   - Created `utils/validators.py` to check required fields in requests.

4. **Consistent JSON Responses**
   - Used `jsonify()` and proper HTTP status codes (200, 400, 404, 401).

5. **Code Maintainability**
   - Modular functions, meaningful names, and reusable helpers.

---

## 🧠 Assumptions & Trade-Offs

- Password hashing uses Werkzeug (not bcrypt or argon2 due to time/complexity).
- SQLite retained for simplicity (no switch to SQLAlchemy or PostgreSQL).
- No JWT token-based login or session management was added (not in scope).

---

## ⚙️ Tools & AI Usage

- **ChatGPT** (GPT-4) was used to review legacy issues, plan structure, and generate boilerplate refactored code.
- Modified and tested all AI-assisted code manually to ensure correctness.

---

## 🚀 If I Had More Time

- Add unit & integration tests with `pytest`
- Implement token-based auth (e.g. JWT)
- Add pagination to `/users` and `/search`
- Migrate from SQLite to PostgreSQL using SQLAlchemy
- Add logging and config-based environments
- Dockerize the entire app for portable deployment

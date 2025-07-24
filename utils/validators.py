def validate_user_input(data, required_fields):
    missing = [field for field in required_fields if not data.get(field)]
    if missing:
        return False, f"Missing fields: {', '.join(missing)}"
    return True, None

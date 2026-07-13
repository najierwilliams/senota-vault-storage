import secrets

class KeyManager:
    def generate_key_id(self)->str:
        return f"KEY-{secrets.token_hex(16).upper()}"

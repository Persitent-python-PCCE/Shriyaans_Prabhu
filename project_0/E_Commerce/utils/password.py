import hashlib
import secrets
ITERATIONS = 600_000
def hash_password(password):
    salt = secrets.token_bytes(16)

    password_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt,
        ITERATIONS
    )

    return (
        f"pbkdf2_sha256${ITERATIONS}$"
        f"{salt.hex()}$"
        f"{password_hash.hex()}"
    )


def verify_password(password, stored_hash):
    try:
        algorithm, iterations, salt, original_hash = stored_hash.split("$")

        if algorithm != "pbkdf2_sha256":
            return False

        iterations = int(iterations)

        password_hash = hashlib.pbkdf2_hmac(
            "sha256",
            password.encode("utf-8"),
            bytes.fromhex(salt),
            iterations
        )

        return secrets.compare_digest(
            password_hash.hex(),
            original_hash
        )

    except (ValueError, TypeError):
        return False
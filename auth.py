"""
Biometric Two-Factor Authentication System

This module implements a secure authentication system that combines:
1. Biometric authentication (simulated fingerprint)
2. Two-factor authentication using TOTP (Time-based One-Time Password)
3. Encrypted storage of sensitive data

The system uses:
- pyotp for TOTP generation and verification
- qrcode for generating QR codes for authenticator apps
- Custom modules for biometric simulation, hashing, and encryption
"""

import json
import pyotp
import qrcode # type: ignore
from biometric import generate_mock_fingerprint
from hashing import generate_hash # type: ignore
from encryption import encrypt_data, decrypt_data # type: ignore

# File path for storing user data
USER_DB = "users.json"

def load_users():
    """
    Loads user data from the JSON database file.
    
    Returns:
        dict: Dictionary containing user data, or empty dict if file doesn't exist
    """
    try:
        with open(USER_DB, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_users(users):
    """
    Saves user data to the JSON database file.
    
    Args:
        users (dict): Dictionary containing user data to save
    """
    with open(USER_DB, "w") as f:
        json.dump(users, f, indent=4)

def generate_qr_code(username, otp_secret):
    """
    Generates and displays a QR code for Google Authenticator in the console.
    
    Args:
        username (str): The username for the account
        otp_secret (str): The TOTP secret key to encode in the QR code
    
    The QR code can be scanned with Google Authenticator or Authy to set up 2FA.
    """
    otp_uri = pyotp.totp.TOTP(otp_secret).provisioning_uri(
        name=username, issuer_name="BioHash Authenticator"
    )
    qr = qrcode.QRCode()
    qr.add_data(otp_uri)
    qr.make()
    print("\n📷 Scan this QR code using Google Authenticator or Authy:")
    qr.print_ascii()  # Display QR code in terminal
    print("\nAlternatively, enter this manually:", otp_secret)

def register_user(username):
    """
    Registers a new user with biometric and TOTP authentication.
    
    Args:
        username (str): The username to register
    
    The registration process:
    1. Generates a simulated fingerprint based on username
    2. Creates a secure hash of the fingerprint
    3. Encrypts the hash for storage
    4. Generates a TOTP secret for 2FA
    5. Displays a QR code for setting up authenticator app
    """
    users = load_users()
    if username in users:
        print("⚠️ User already exists!")
        return

    # Generate fingerprint based on username (consistent)
    fingerprint = generate_mock_fingerprint(username)
    salt, biometric_hash = generate_hash(fingerprint)

    # Encrypt biometric hash
    key, nonce, encrypted_hash = encrypt_data(biometric_hash)

    # Generate OTP Secret
    otp_secret = pyotp.random_base32()

    # Store user data
    users[username] = {
        "salt": salt.hex(),
        "encrypted_hash": encrypted_hash.hex(),
        "key": key.hex(),   # Store encryption key
        "nonce": nonce.hex(),  # Store nonce
        "otp_secret": otp_secret
    }
    save_users(users)

    print(f"✅ User {username} registered successfully!")
    
    # Generate and display QR code in console
    generate_qr_code(username, otp_secret)

def authenticate_user(username):
    """
    Authenticates a user using biometric data and TOTP.
    
    Args:
        username (str): The username to authenticate
    
    The authentication process:
    1. Verifies the user exists
    2. Generates and verifies the biometric fingerprint
    3. Prompts for and verifies the TOTP code
    4. Returns success/failure status
    """
    users = load_users()
    if username not in users:
        print("❌ User not found!")
        return

    # Load user data
    user_data = users[username]
    salt = bytes.fromhex(user_data["salt"])
    encrypted_hash = bytes.fromhex(user_data["encrypted_hash"])
    key = bytes.fromhex(user_data["key"])  # Retrieve stored encryption key
    nonce = bytes.fromhex(user_data["nonce"])  # Retrieve stored nonce
    otp_secret = user_data["otp_secret"]

    # Generate the same fingerprint for this user
    new_fingerprint = generate_mock_fingerprint(username)
    _, new_hash = generate_hash(new_fingerprint, salt)

    # Decrypt stored hash
    decrypted_hash = decrypt_data(key, nonce, encrypted_hash)

    # Compare biometric data
    if new_hash != decrypted_hash:
        print("❌ Biometric authentication failed!")
        return

    # Verify OTP
    otp = input("🔢 Enter OTP from your authenticator app: ")
    if not pyotp.TOTP(otp_secret).verify(otp):
        print("❌ OTP verification failed!")
        return

    print("✅ Authentication Successful!")

def view_all_users():
    """
    Displays a list of all registered users in the system.
    
    Shows a formatted list of usernames, or a message if no users exist.
    """
    users = load_users()
    if not users:
        print("🚨 No users found!")
    else:
        print("\n📋 Registered Users:")
        for username in users.keys():
            print(f"- {username}")

def delete_all_users():
    """
    Deletes all registered users from the system.
    
    Requires confirmation before deletion to prevent accidental data loss.
    """
    confirmation = input("⚠️ Are you sure you want to delete all users? (yes/no): ")
    if confirmation.lower() == "yes":
        save_users({})  # Save an empty dictionary to clear the user database
        print("✅ All users have been deleted.")
    else:
        print("❌ Operation canceled.")

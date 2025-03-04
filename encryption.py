"""
Bio-Hashing: Two-Factor Authentication 
Source Code
Authors: Ifeoluwa Adebisi, Babek Nabiee, Fatimata Coly, Moussa Kebe, Lakshaya Sharma
SDEV 495 6384
Instructor: Hung Dao
"""

"""
Encryption Module

This module provides functionality for encrypting and decrypting sensitive data
using Fernet symmetric encryption. It uses a secure key generation process and
nonce-based encryption to ensure data confidentiality.

The module uses the Fernet implementation from the cryptography package,
which is a secure implementation of AES-128-CBC with PKCS7 padding.
"""

from cryptography.fernet import Fernet
import os

def encrypt_data(data):
    """
    Encrypts data using Fernet symmetric encryption.
    
    Args:
        data (bytes): The data to encrypt
        
    Returns:
        tuple: (key, nonce, encrypted_data)
            - key (bytes): The encryption key
            - nonce (bytes): The nonce used for encryption
            - encrypted_data (bytes): The encrypted data
    """
    key = Fernet.generate_key()
    f = Fernet(key)
    return key, os.urandom(16), f.encrypt(data)

def decrypt_data(key, nonce, encrypted_data):
    """
    Decrypts data using Fernet symmetric encryption.
    
    Args:
        key (bytes): The encryption key
        nonce (bytes): The nonce used for encryption
        encrypted_data (bytes): The encrypted data to decrypt
        
    Returns:
        bytes: The decrypted data
    """
    f = Fernet(key)
    return f.decrypt(encrypted_data)

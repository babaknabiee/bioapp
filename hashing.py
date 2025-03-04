"""
Bio-Hashing: Two-Factor Authentication 
Source Code
Authors: Ifeoluwa Adebisi, Babek Nabiee, Fatimata Coly, Moussa Kebe, Lakshaya Sharma
SDEV 495 6384
Instructor: Hung Dao
"""

"""
Hashing Module

This module provides functionality for secure hashing of biometric data
using PBKDF2 (Password-Based Key Derivation Function 2) with SHA-256.
It includes salt generation and hash verification capabilities.

The module uses the hashlib implementation of PBKDF2, which is designed
to be computationally intensive to prevent brute-force attacks.
"""

import hashlib
import os

def generate_hash(data, salt=None):
    """
    Generates a secure hash of the input data using PBKDF2.
    
    Args:
        data (numpy.ndarray): The data to hash
        salt (bytes, optional): Salt for the hash. If None, generates a new salt.
        
    Returns:
        tuple: (salt, hash)
            - salt (bytes): The salt used for hashing
            - hash (bytes): The generated hash
    """
    if salt is None:
        salt = os.urandom(16)
    
    # Convert numpy array to bytes for hashing
    data_bytes = data.tobytes()
    
    # Generate hash using PBKDF2
    hash_obj = hashlib.pbkdf2_hmac(
        'sha256',
        data_bytes,
        salt,
        100000  # Number of iterations
    )
    
    return salt, hash_obj

def verify_hash(data, salt, stored_hash):
    """Verifies if the hash of the new biometric data matches the stored hash."""
    _, new_hash = generate_hash(data, salt)
    return new_hash == stored_hash

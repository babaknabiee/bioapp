"""
Time-based One-Time Password (TOTP) Module

This module provides functionality for generating and verifying TOTP codes
used in two-factor authentication. It uses the pyotp library which implements
the TOTP standard (RFC 6238).

The module supports:
- Generating secure random secrets
- Creating TOTP codes
- Verifying TOTP codes
"""

import pyotp
import base64
import os

def generate_otp_secret():
    """
    Generates a secure random secret for TOTP.
    
    Returns:
        str: A base32-encoded secret key
    """
    return pyotp.random_base32()

def generate_otp(secret):
    """
    Generates a TOTP code for the given secret.
    
    Args:
        secret (str): The TOTP secret key
        
    Returns:
        str: The current TOTP code
    """
    totp = pyotp.TOTP(secret)
    return totp.now()

def verify_otp(secret, code):
    """
    Verifies a TOTP code against the secret.
    
    Args:
        secret (str): The TOTP secret key
        code (str): The TOTP code to verify
        
    Returns:
        bool: True if the code is valid, False otherwise
    """
    totp = pyotp.TOTP(secret)
    return totp.verify(code)

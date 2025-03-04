"""
Biometric Simulation Module

This module provides functionality for simulating biometric data (fingerprints)
in a consistent and deterministic way. It uses numpy's random number generator
with a seeded value based on the username to ensure the same fingerprint is
generated for the same user each time.

This is a mock implementation for demonstration purposes. In a real system,
this would interface with actual biometric hardware.
"""

import numpy as np

def generate_mock_fingerprint(username):
    """
    Generates a simulated fingerprint based on the username.
    
    Args:
        username (str): The username to generate a fingerprint for
        
    Returns:
        numpy.ndarray: A 1x128 array representing the fingerprint features
        
    Note:
        - Uses a seeded random number generator to ensure consistency
        - The seed is derived from the username's hash value
        - Returns a 128-dimensional feature vector
        - This is a mock implementation for demonstration
    """
    np.random.seed(hash(username) % (2**32))  # Ensure consistency per user
    return np.random.rand(1, 128)  # 128 feature vector

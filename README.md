# Biometric Two-Factor Authentication System

A secure authentication system that combines biometric authentication (simulated fingerprint) with two-factor authentication (TOTP) for enhanced security.

## Features

- 🔐 Biometric authentication using simulated fingerprints
- 🔑 Two-factor authentication using TOTP (Time-based One-Time Password)
- 🔒 Encrypted storage of sensitive data
- 📱 QR code generation for easy authenticator app setup
- 👥 User management (registration, authentication, listing, deletion)

## Security Features

- PBKDF2 hashing with SHA-256 for biometric data
- Fernet symmetric encryption for sensitive data
- Salt-based hashing to prevent rainbow table attacks
- Secure random key generation
- Nonce-based encryption to prevent replay attacks

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd bioapp
```

2. Install required packages:
```bash
pip install numpy pyotp qrcode cryptography pillow
```

## Usage

1. Run the application:
```bash
python main.py
```

2. Available Options:
   - 1️⃣ Register User: Create a new user with biometric and 2FA
   - 2️⃣ Authenticate User: Login with existing credentials
   - 3️⃣ View All Users: List all registered users
   - 4️⃣ Delete All Users: Remove all user data (requires confirmation)
   - 5️⃣ Exit: Close the application

### Registration Process

1. Select option 1 to register a new user
2. Enter your desired username
3. The system will:
   - Generate a simulated fingerprint
   - Create a secure hash
   - Generate a TOTP secret
   - Display a QR code
4. Scan the QR code with Google Authenticator or Authy
5. Save the manual entry code as backup

### Authentication Process

1. Select option 2 to authenticate
2. Enter your username
3. The system will verify your biometric data
4. Enter the TOTP code from your authenticator app
5. If both verifications pass, you're authenticated

## Technical Details

### Components

1. **Biometric Module** (`biometric.py`)
   - Simulates fingerprint generation
   - Uses seeded random numbers for consistency
   - Generates 128-dimensional feature vectors

2. **Encryption Module** (`encryption.py`)
   - Uses Fernet (AES-128-CBC) encryption
   - Implements secure key generation
   - Provides data encryption/decryption

3. **Hashing Module** (`hashing.py`)
   - Implements PBKDF2 with SHA-256
   - Uses salt-based hashing
   - Provides hash verification

4. **TOTP Module** (`totp.py`)
   - Implements RFC 6238 TOTP standard
   - Generates secure random secrets
   - Provides code verification

5. **Authentication Module** (`auth.py`)
   - Manages user registration and authentication
   - Handles data storage and retrieval
   - Implements QR code generation

### Data Storage

- User data is stored in `users.json`
- Sensitive data is encrypted before storage
- Biometric hashes are salted and encrypted
- TOTP secrets are stored securely

## Security Considerations

1. **Biometric Data**
   - Simulated for demonstration
   - In production, use actual biometric hardware
   - Data is hashed and encrypted

2. **Two-Factor Authentication**
   - Uses standard TOTP implementation
   - Compatible with Google Authenticator
   - Supports backup codes

3. **Data Protection**
   - All sensitive data is encrypted
   - Uses secure random number generation
   - Implements salt-based hashing

## Limitations

- Biometric simulation is for demonstration only
- No password protection for user data
- Single-factor biometric authentication
- No rate limiting implemented

## Future Improvements

1. Add actual biometric hardware support
2. Implement rate limiting
3. Add password protection
4. Support multiple biometric factors
5. Add user session management
6. Implement backup/recovery options

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer

This is a demonstration project. For production use:
- Implement proper biometric hardware
- Add additional security measures
- Conduct security audits
- Follow security best practices 
"""
Bio-Hashing: Two-Factor Authentication 
Source Code
Authors: Ifeoluwa Adebisi, Babek Nabiee, Fatimata Coly, Moussa Kebe, Lakshaya Sharma
SDEV 495 6384
Instructor: Hung Dao
"""

"""
Main entry point for the Biometric Two-Factor Authentication System.

This module provides a command-line interface for:
1. User registration with biometric and 2FA
2. User authentication
3. User management (view/delete users)
"""

from auth import register_user, authenticate_user, view_all_users, delete_all_users # type: ignore

def main():
    """
    Main program loop that provides an interactive menu for the authentication system.
    
    Menu Options:
    1. Register User - Create a new user with biometric and 2FA
    2. Authenticate User - Login with existing credentials
    3. View All Users - List all registered users
    4. Delete All Users - Remove all user data (requires confirmation)
    5. Exit - Close the application
    """
    while True:
        print("\n🔐 Biometric Two-Factor Authentication System")
        print("1️⃣ Register User")
        print("2️⃣ Authenticate User")
        print("3️⃣ View All Users")
        print("4️⃣ Delete All Users")
        print("5️⃣ Exit")
        choice = input("Select an option: ")

        if choice == "1":
            username = input("Enter username: ")
            register_user(username)
        elif choice == "2":
            username = input("Enter username: ")
            authenticate_user(username)
        elif choice == "3":
            view_all_users()
        elif choice == "4":
            delete_all_users()
        elif choice == "5":
            print("👋 Exiting...")
            break
        else:
            print("❌ Invalid choice, try again!")

if __name__ == "__main__":
    main()

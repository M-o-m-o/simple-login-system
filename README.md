# simple-login-system
Simple User Authentication System
A basic Python program that manages user registration and login with hashed passwords. It includes a manager password to view registered users, and logs login attempts and program usage.

                                                                         ---Features---

User registration with username and SHA-256 hashed password storage.

Secure login with password hashing and three attempt limit.

Manager-only access to view the list of registered users (protected by a separate manager password).

Logs login attempts and when the program is started, including machine info (PC user, hostname, IP).

Simple text file storage (users.txt) for user data and logs.
"______________________________________________________________________________________________________________________________________________________"
                                                                        ---How to Use---
Run the script.

Choose to log in, register, or exit.

Registering requires a unique username and password.

Login requires a valid username and password.

After login, you can view a secret, see users (manager access only), or exit.

The manager password is "AAAA" (hashed internally).
"______________________________________________________________________________________________________________________________________________________"
                                                                        ---Requirements---
Python 3.x

Modules: getpass, socket, time, hashlib (all standard libraries)

Files
users.txt — stores usernames and hashed passwords.

login_log.txt — logs successful logins.

enabled the command.txt — logs whenever the program is started.

Security Notes
Passwords are hashed with SHA-256 before storage.

The manager password is hardcoded as "AAAA" for simplicity; consider improving this in the future.

This is a basic example and not production-ready for real-world secure authentication.
"______________________________________________________________________________________________________________________________________________________"


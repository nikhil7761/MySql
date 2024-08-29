import bcrypt

password = 'nihkil@123'  # Replace with your desired new password
hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
print(hashed.decode('utf-8'))

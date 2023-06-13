from flask_bcrypt import Bcrypt
bcrypt=Bcrypt()

password="123456"

hash_password=bcrypt.generate_password_hash(password=password)
print(hash_password)

check_password=bcrypt.check_password_hash('$2b$12$jPV/w.ME3E4L4w6ep2YrNeaHJErL5lAPhWwk610yDl8twSmcFrhFO',"nl")
print(check_password)

# dic={'email':'123@gmail.com','password':'123456'}
# print(dic['email']=='123@gmail.com')



import time
from .jwt_handler import encodeJWT, decodeJWT, refreshJWT

user = {"email":"suiunpython1@hmail.com", "username":"suiun", "id":1}

#получаем токены
jwt_token = encodeJWT(user) # 
print(jwt_token)

# проходит время
time.sleep(6)

# прилетает декодированные токен, если время не истекло, если время жизни токенв истекло прилетает пустая строка
decoded = decodeJWT(jwt_token['access_token'])
print(decoded)

# обновляем старые токены, на новые
new_jwt_token = refreshJWT(jwt_token['refresh_token'])
print(new_jwt_token)
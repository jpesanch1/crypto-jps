import base64
import json

import jwt

token = jwt.encode({'key': 'value'}, 'secret', algorithm='HS256')
print(token)
# u'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXkiOiJ2YWx1ZSJ9.FG-8UppwHaFp1LgRYQQeS6EDQF7_6-bMFegNucHjmWg'
token_parts = token.split(".")
for i in range(0, len(token_parts)):
    print(token_parts[i])
    print(base64.b64decode(token_parts[i]))

print(base64.b64decode("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"))
jwt.decode(token, 'secret', algorithms=['HS256'])
# {u'key': u'value'}

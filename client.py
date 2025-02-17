import jwt
import datetime
import requests

# Secret key for signing JWT (set inside the auth server)
SECRET_KEY = "mysecret"

def generate_jwt():
    """Generate a minimal JWT token"""
    payload = {
        "sub": "user123",  # Subject (user identifier)
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # Expiration (1 hour)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token

jwt_token = generate_jwt()
url = "https://localhost/api"
headers = {
    "Authorization": f"Bearer {jwt_token}123"
}
response = requests.get(url, headers=headers, verify=False)  # `verify=False` skips SSL checks
print("Status Code:", response.status_code)
print("Response:", response.text)
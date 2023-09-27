import requests

# Define the base URL of your Sanic application
BASE_URL = "http://localhost:8000"  # Adjust the host and port as needed

# Register a new user
def register_user(username, password):
    url = f"{BASE_URL}/auth/register"
    data = {"username": username, "password": password}
    response = requests.post(url, json=data)
    return response

# Authenticate a user and get an access token
def authenticate_user(username, password):
    url = f"{BASE_URL}/auth/login"
    data = {"username": username, "password": password}
    response = requests.post(url, json=data)
    return response

if __name__ == "__main__":
    testuser = input("Enter test username: ")
    testpassword = input("Enter test password: ")
    registration_response = register_user(testuser, testpassword)
    if registration_response.status_code == 201:
        print("User registration successful!")
    else:
        print("User registration failed.")

    # Test authenticationS
    authentication_response = authenticate_user(testuser, testpassword)
    if authentication_response.status_code == 200:
        access_token = authentication_response.json().get("access_token")
        print(f"User authenticated! Access Token: {access_token}")
    else:
        print("User authentication failed.")

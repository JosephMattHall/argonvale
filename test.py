import requests

# Define the base URL of your Sanic app
BASE_URL = "http://localhost:8000"  # Change this if your app is running on a different host or port

# Function to perform user registration
def register(username):
    data = {
        "username": username,
        "password": "5599weuz"
    }
    response = requests.post(f"{BASE_URL}/auth/register", json=data)
    return response

# Function to perform user login and get an access token
def login(username):
    data = {
        "username": username,
        "password": "5599weuz"
    }
    response = requests.post(f"{BASE_URL}/auth/login", json=data)
    return response.json().get("access_token")

# Function to create a companion for the logged-in user
def create_companion(username):
    token = login(username)  # Get the access token
    companion_data = {
        "name": f"{username}_companion",
        "image": "companion_image_url",
        "type": "companion_type"
    }
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.post(f"{BASE_URL}/companion/create", json=companion_data, headers=headers)
    return response.json().get("companion_id")

# Function to get the training status of all companions for the logged-in user
def get_training_status(username):
    token = login(username)  # Get the access token
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{BASE_URL}/companion/training_status", headers=headers)
    return response.json().get("training_status")

# Function to start a training course for a companion
def start_training(username, companion_id):
    token = login(username)  # Get the access token
    chosen_stat = "strength"  # Change this to the desired stat
    headers = {"Authorization": f"Bearer {token}"}
    data = {"chosen_stat": chosen_stat}
    response = requests.put(f"{BASE_URL}/companion/start_training/{companion_id}", json=data, headers=headers)
    return response

# Test script
if __name__ == "__main__":
    username = input("Enter username: ")

    # Register a new user
    register_response = register(username)
    if register_response.status_code == 201:
        print(f"User '{username}' registered successfully.")

    # Create a companion for the user
    companion_id = create_companion(username)
    print(f"Companion created with ID: {companion_id}")

    # Get the training status of all companions for the user
    training_status = get_training_status(username)
    print("Training Status:")
    print(training_status)

    # Start a training course for the companion
    if companion_id:
        start_training_response = start_training(username, companion_id)
        print(start_training_response.json())

import requests

BASE_URL = "http://127.0.0.1:8000"

# Helper function to create a user
def create_user(username, password):
    data = {"username": username, "password": password}
    response = requests.post(f"{BASE_URL}/auth/register", json=data)
    return response.json()  # Returns  "message"

# Helper function to log in and get the access token
def login(username, password):
    data = {"username": username, "password": password}
    response = requests.post(f"{BASE_URL}/auth/login", json=data)
    return response.json().get("access_token")

# Helper function to create a companion
def create_companion(access_token, name, image, type):
    headers = {"Authorization": f"Bearer {access_token}"}
    data = {"name": name, "image": image, "type": type}
    response = requests.post(f"{BASE_URL}/companion/create", headers=headers, json=data)
    return response.json()  # Returns the companion's _id, not "message"

# Helper function to get the training status of companions
def get_training_status(access_token):
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(f"{BASE_URL}/companion/training_status", headers=headers)
    return response.json()

# Helper function to start the training course for a companion
def start_training_course(access_token, companion_id, stat_to_train):
    headers = {"Authorization": f"Bearer {access_token}"}
    data = {"companion_id": companion_id, "stat_to_train": stat_to_train}
    response = requests.post(f"{BASE_URL}/companion/start_course", headers=headers, json=data)
    return response.json()  # Returns the training time, not "message"

# Helper function to end the training course and increase the corresponding stat
def end_training_course(access_token, companion_id, stat_to_train):
    headers = {"Authorization": f"Bearer {access_token}"}
    data = {"companion_id": companion_id, "stat_to_train": stat_to_train}
    response = requests.post(f"{BASE_URL}/companion/end_course", headers=headers, json=data)
    return response.json()

# Test the companion functionality
def test_companion_functionality():
    # Create a user
    user_data = create_user("atestyuser11122", "testpassword")
    print(user_data)
    assert "message" in user_data  # Check for the _id key instead of "message"

    # Log in to get the access token
    access_token = login("atestyuser11122", "testpassword")
    assert access_token

    # Create a companion
    companion_data = create_companion(access_token, "zxxTestykul111122", "image1_url", "demon")
    print(companion_data)
    assert "message" in companion_data  # Check for the _id key instead of "message"

    # Check the training status (should be "ready" since we haven't started training)
    training_status = get_training_status(access_token)
    assert "training_status" in training_status
    print(training_status["training_status"])
    assert training_status["training_status"]["zxxTestykul111122"]["status"] == "ready"

    # Start training the companion (training time should be returned)
   # training_data = {
   #     "companion_id": companion_data["user_id"],
   #     "stat_to_train": "strength"  # Change to "defense", "speed", or "HP" for different stats
   # }
   # start_response = start_training_course(access_token, **training_data)
   # assert "training_time" in start_response

    # Check the training status (should be "training" since we started training)
    #training_status = get_training_status(access_token)
    #assert "training_status" in training_status
    #assert "Test Companion" in training_status["training_status"]
   # assert training_status["training_status"]["Test Companion"]["status"] == "training"

    # Wait for the training to finish (you may use time.sleep here in real-world scenarios)
    # ...

    # Check the training status again (should be "finish" now that training is done)
   # training_status = get_training_status(access_token)
    #assert "training_status" in training_status
    #assert "Test Companion" in training_status["training_status"]
   # assert training_status["training_status"]["Test Companion"]["status"] == "finish"

    # End the training course and increase the corresponding stat
   # end_response = end_training_course(access_token, **training_data)
   # assert "message" in end_response

    # Check the companion's stats after training
    # ...

    # You can repeat the above steps to test other companion functionality as well
    # ...


if __name__ == "__main__":
    test_companion_functionality()

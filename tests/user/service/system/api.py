
def test_get_users():
	response = requests.get("http://127.0.0.1:8000/users")
	assert response.status_code == 200
	
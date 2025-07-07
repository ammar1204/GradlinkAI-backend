import requests

BASE_URL = "http://127.0.0.1:8000"

def test_chatbot(query: str):
    endpoint = f"{BASE_URL}/chatbot"
    params = {"query": query}

    response = requests.get(endpoint, params=params)

    if response.status_code == 200:
        print("✅ Response:", response.json())
    else:
        print(f"❌ Error {response.status_code}: {response.text}")


if __name__ == "__main__":
    print("=== Testing GradLink Chatbot ===")
    test_chatbot("How can I improve my CGPA?")
    test_chatbot("Are there scholarships for final year students?")
    test_chatbot("Where can I find internships?")

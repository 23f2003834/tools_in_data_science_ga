import requests  # This requires pip install requests

print("Hello World")
response = requests.get('https://api.github.com')
print(f"GitHub API status: {response.status_code}")

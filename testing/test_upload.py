import requests

url = "http://127.0.0.1:5000/upload-report"

files = {
    "file": open("datasets/RAW_DATASET.csv", "rb")
}

response = requests.post(url, files=files)

print(response.json())
#  Fetching data from open APIs and print the response 

import requests
import json

def get_request(api_endpoint):
    try:
        response = requests.get(api_endpoint)
        if response.status_code == 200:
            print(f"Response from API: {response.text}")
            response_data = json.loads(response.text)
            print(f"Parsed response data:")
            if isinstance(response_data, list):
                for item in response_data:
                    userId = item.get("userId")
                    id = item.get("id")
                    title = item.get("title")
                    body = item.get("body")
                    print(f"userId: {userId}\nid: {id}\ntitle: {title}\nbody: {body}\n")
            elif isinstance(response_data, dict):
                userId = response_data.get("userId")
                id = response_data.get("id")
                title = response_data.get("title")
                body = response_data.get("body")
                print(f"userId: {userId}\nid: {id}\ntitle: {title}\nbody: {body}\n")
            else:
                print("Unknown response type")
        else:
            print(f"An error occurred while requesting {api_endpoint}: {response.status_code}")

    except Exception as e:
        print(f"An error occurred while requesting {api_endpoint}: {str(e)}")


if __name__ == "__main__":
    # api_endpoint = input("Enter API endpoint: ")
    api_endpoint = "https://jsonplaceholder.typicode.com/posts/1"
    get_request(api_endpoint)
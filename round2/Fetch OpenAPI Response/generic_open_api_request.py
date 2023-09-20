import requests
import json

def get_request(api_endpoint):
    try:
        response = requests.get(api_endpoint)
        if response.status_code == 200:
            print(response.text)
            response_data = json.loads(response.text)
            print(f"Parsed response data:")
            explore(response_data)
        else:
            print(f"An error occurred while requesting {api_endpoint}: {response.status_code}")

    except Exception as e:
        print(f"An error occurred while requesting {api_endpoint}: {str(e)}")

def explore(json_data, parent_key=''):
    if isinstance(json_data, dict):
        for key, value in json_data.items():
            new_key = f"{parent_key}.{key}" if parent_key else key
            if isinstance(value, (dict, list)):
                explore(value, new_key)
            else:
                print(f"{new_key}:{value}")
    elif isinstance(json_data, list):
        for item in json_data:
            explore(item, parent_key)


if __name__ == "__main__":
    api_endpoint = input("Enter API endpoint: ")
    get_request(api_endpoint)
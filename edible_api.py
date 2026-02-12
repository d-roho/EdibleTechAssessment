import requests
import json
import sys

def search_edible_arrangements(keyword):
    url = "https://www.ediblearrangements.com/api/search/"
    payload = {"keyword": keyword}
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    print(f"--- Sending POST request to {url} ---")
    print(f"Payload: {json.dumps(payload, indent=2)}")
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        print(f"\nStatus Code: {response.status_code}")
        
        try:
            response_json = response.json()
            print("Response Payload:")
            print(json.dumps(response_json, indent=2))
        except json.JSONDecodeError:
            print("Response content is not JSON:")
            print(response.text[:500] + "..." if len(response.text) > 500 else response.text)
            
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    search_term = sys.argv[1] if len(sys.argv) > 1 else "fruit"
    search_edible_arrangements(search_term)

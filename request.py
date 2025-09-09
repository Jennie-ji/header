def fetch_headers(url):
    if not url.startswith(("http://", "https://")):
        url = "https://" + url
    import requests
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.headers
    except requests.RequestException as e:
        print(f"Error: {e}")
        return None


import requests
from bs4 import BeautifulSoup

def request(url: str) -> requests.Response:
    """
    Makes a request to the given URL and returns the response.
    """
    try:
        response = requests.get(url)
        status = response.status_code
        if status != 200:
            print(f"Error: status code - {status}")
            return None
        else:
            return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error making request to {url}: {e}")
        return None

def fetch_team_urls(urls: list[str]) -> list[str]:
    """
    Fetches the content of the given URLs and returns a list of the content.
    """
    url_content = []
    for url in urls:
        content = request(url)
        if content:
            url_content.append(content)
        else:
            print(f"Error fetching content from {url}")
    return url_content

def get_team_players(content: list[str]) -> list[str]:
    """
    Extracts the player names from the given content.
    """
    player_names = []
    for team in content:
        soup = BeautifulSoup(team, "html.parser")
        players = soup.find_all('td', class_='info')
        for player in players:
            player = player.find('a').text
            player_names.append(player)
    return player_names
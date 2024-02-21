from helpers import fetch_team_urls, get_team_players
from pprint import pprint
import json

def main():
    team_players_dict = {}
    teams = [
        'redsox',
        'yankees',
        'bluejays',
        'rays',
        'orioles',
        'whitesox',
        'guardians',
        'tigers',
        'royals',
        'twins',
        'cubs',
        'reds',
        'brewers',
        'pirates',
        'cardinals',
        'braves',
        'marlins',
        'mets',
        'phillies',
        'nationals',
        'astros',
        'dbacks',
        'angels',
        'athletics',
        'mariners',
        'rangers',
        'rockies',
        'dodgers',
        'padres',
        'giants',
    ]
    for team in teams:
        team_url = f'https://www.mlb.com/{team}/roster/40-man'
        team_content = fetch_team_urls([team_url])
        team_players = get_team_players(team_content)
        team_players_dict[team] = team_players
    
    with open('team_players.json', 'w') as json_file:
        json.dump(team_players_dict, json_file, indent=2, sort_keys=True, ensure_ascii=False)

if __name__ == '__main__':
    main()

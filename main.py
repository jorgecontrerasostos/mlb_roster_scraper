from helpers import fetch_team_urls, get_team_players
def main():
    team_urls = []
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
        team_urls.append(f'https://www.mlb.com/{team}/roster/40-man')
    
    results = fetch_team_urls(team_urls)
    team_players = get_team_players(results)
    print(team_players)

if __name__ == '__main__':
    main()

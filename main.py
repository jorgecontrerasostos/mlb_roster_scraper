from helpers import fetch_urls
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
    
    results = fetch_urls(team_urls)
    print(results)
if __name__ == '__main__':
    main()

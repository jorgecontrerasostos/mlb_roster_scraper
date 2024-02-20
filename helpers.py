import aiohttp
import asyncio

def build_team_url() -> list:
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
        'diamondbacks',
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
    return team_urls
    

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()
    
async def fetch_all(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_all(session, url) for url in urls]
        return await asyncio.gather(*tasks)
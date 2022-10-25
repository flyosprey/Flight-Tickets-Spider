from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem


def _get_headers() -> dict:
    user_agent = _get_random_user_agent()
    headers = {
        'authority': 'fly2.emirates.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
                  'application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-US,en;q=0.9,es-US;q=0.8,es;q=0.7,ru-RU;q=0.6,ru;q=0.5,uk-UA;q=0.4,uk;q=0.3',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://www.emirates.com',
        'referer': 'https://www.emirates.com/',
        'upgrade-insecure-requests': '1',
        'user-agent': user_agent
    }
    return headers


def _get_random_user_agent() -> str:
    software_names = [SoftwareName.CHROME.value]
    operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]
    user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)
    user_agent = user_agent_rotator.get_random_user_agent()
    return user_agent

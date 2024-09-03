from requests_html import HTMLSession
import nest_asyncio

nest_asyncio.apply()



session = HTMLSession()
r = session.get('https://www.ncaa.com/scoreboard/football/fbs')
r.html.render(timeout=10)
elements = r.html.find('.gamePod_content-pod_container', first=True)

print(elements.text)
session.close()
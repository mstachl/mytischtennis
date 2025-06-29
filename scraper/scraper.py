import requests
import os
from dotenv import load_dotenv

load_dotenv()

start = 1
end = 800

playerId = 1058225

curSession = requests.Session()

userNameB = os.getenv("userNameB")
userPassWordB = os.getenv("userPassWordB")

print(userNameB,userPassWordB)

payload = {'userNameB':userNameB,'userPassWordB':userPassWordB}

curSession.post('https://www.mytischtennis.de/community/login/', data=payload)


i = start

while i < end:
    url = "https://www.mytischtennis.de/community/matches-tabelle/?clickttid={}&start={}&scrollToTop=&statistictype=all&timeinterval=all&winlostkey=&matchtype=all".format(playerId,i)
    print("Trying url {}".format(url))
    r = curSession.get(url)

    if r.status_code == 200:
        content = r.text

        file = open("../data/stats_{}.html".format(i),'w')
        file.write(content)
        file.close()
    else:
        print("Failed to retrieve the webpage. Status code: {}".format(r.status_code))
    i+=100



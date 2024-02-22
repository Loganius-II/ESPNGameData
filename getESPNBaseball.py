from requests_html import HTMLSession
import sys
from time import sleep
from os import system
update = 0
done = False

def type(message):
    for i in message:
        sys.stdout.write(i)
        sys.stdout.flush
        sleep(0.01)
#type funtion is just a type writer effect for some pazzaz
type("This Python script will only work if a sport game is happening live!\n")
query = input("What ESPN Sport would you like to check? ")
#asks user for what sport they want (Must be a game that is already happening live on ESPN!)
url = f"https://www.bing.com/search?q=espn+{query}"
#Injects query in a artificial search using an f-string
s = HTMLSession()
#starts session
request = s.get(url, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0'})
#requests url to html session. Uses user-agent (optional) as a header
while not done:
    update +=1
    #Starts our Sport Data update
    homeTeam = request.html.find('div.bsp_team_row.bsp_team_reverse div.bsp-celebrated-card-row div.bsp-team-name span', first=True ).text
    score = request.html.find('div.bsp_scr div.bsp_main_scr')
    #Uses our request to find the EXACT DOM element and scrapes it right out of the site
    #I used prior knowlege with CSS to help me with this. To target a certain div using its class name: div.[classname]
    #for IDs use div#[Id name] 
    #this also applies for ls,ul,p,h5,span,bold, and just about any other type of HTML tag
    #AlSO: use a space then a follow-up div+classname/id to target elements within that element. 
    #REMEMBER: You can chain the targetting element for as much as you want
    awayTeam = request.html.find('div.bsp_team_row div.bsp-celebrated-card-row div.bsp-team-name span', first=True ).text

    index=0
    #sets index; This will come in handy later
    for i in score:
        index+=1
        if index == 1:
            homeScore = i.text
        elif index == 2:
            awayScore = i.text
    #Since the "request.html.find ..." returns a list, I am using a "for i in score..." to pick apart the scores and turn them into variables
    #The reason I have to do this, Only for the scores is because the class names for the scores are EXACTLY the same. So it returns both scores at the same time
    #Rather than being able to split them into different teams if that makes any sense

    sleep(5)
    #waits to update every 5 seconds
    system('cls')
    #uses os clear so the updated score is the only one that appears
    print(f"Home:{homeTeam} | Score: {homeScore}\nAway:{awayTeam} | Score: {awayScore}\n")
    #Uses f-string  to put it all together
    if update == 1:
        print("Updated once")
    else:
        print("Updated {} times".format(update))


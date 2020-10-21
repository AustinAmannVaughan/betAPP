import csv
import tkinter as tk
class Team:
    name = ""
    wins = 0
    losses = 0
    spreadW = 0
    spreadL = 0
    oppW = []
    oppL = []
    def __init__(self,name,wins,losses,spreadW,spreadL, recW, recL):
        self.name = name
        self.wins = wins
        self.losses = losses
        self.spreadW = spreadW
        self.spreadL = spreadL
        self.oppW = recW
        self.oppL = recL
window = tk.Tk()
button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
)


t = []
w = []
l = []
spr = []
sprW = []
sprL = []
path = 'txt.csv'
file=open( path, "r")
reader = csv.reader(file)
for line in reader:
  t.append(line[0])
  w.append(line[1])
  l.append(line[2])
  sprW.append(line[4])
  sprL.append(line[5])
teams =[]
num1 =-1
num2 = -1
while(num1<0 and num2<0):
    value = input("Please enter a team name: \n")

    opp = input("Please enter an opponent team name: \n")

    if(value== 'Arizona Cardinals'):
        path = 'az.csv'
        num1 = 1
    elif(value=='Atlanta Falcons'):
        path = 'atl.csv'
        num1 = 2
    elif(value=='Baltimore Ravens'):
        path = 'bal.csv'
        num1 = 3
    elif(value=='Buffalo Bills'):
        path = 'buf.csv'
        num1 = 4
    elif(value=='Atlanta Falcons'):
        path = 'atl.csv'
        num1 = 2
    elif(value=='Atlanta Falcons'):
        path = 'atl.csv'
        num1 = 2
    elif(value=='Atlanta Falcons'):
        path = 'atl.csv'
        num1 = 2
    elif(value=='Atlanta Falcons'):
        path = 'atl.csv'
        num1 = 2
    elif(value=='Atlanta Falcons'):
        path = 'atl.csv'
        num1 = 2
    elif(value=='Atlanta Falcons'):
        path = 'atl.csv'
        num1 = 2
    elif(value=='Atlanta Falcons'):
        path = 'atl.csv'
        num1 = 2
    elif(value=='Atlanta Falcons'):
        path = 'atl.csv'
        num1 = 2
    elif(value=='Atlanta Falcons'):
        path = 'atl.csv'
        num1 = 2
    elif(value=='Atlanta Falcons'):
        path = 'atl.csv'
        num1 = 2
    elif(value=='Atlanta Falcons'):
        path = 'atl.csv'
        num1 = 2
    elif(value=='Atlanta Falcons'):
        path = 'atl.csv'
        num1 = 2
    if(opp== 'Arizona Cardinals'):
        num2 = 1
    elif(opp=='Atlanta Falcons'):
        num2 = 2
    elif(opp=='Baltimore Ravens'):
        num2 = 3
    elif(opp=='Buffalo Bills'):
        num2 = 4
    elif(opp=='Carolina Panthers'):
        num2 = 5
    elif(opp=='Chicago Bears'):
        num2 = 6
    elif(opp=='Cincinnati Bengals'):
        num2 = 7
    elif(opp=='Cleveland Browns'):
        num2 = 8
    elif(opp=='Dallas Cowboys'):
        num2 = 9
    elif(opp=='Denver Broncos'):
        num2 = 10
    elif(opp=='Detroit Lions'):
        num2 = 11
    elif(opp=='Green Bay Packers'):
        num2 = 12
    elif(opp=='Houston Texans'):
        num2 = 13
    elif(opp=='Indiannapolis Colts'):
        num2 = 14
    elif(opp=='Jacksonville Jaguars'):
        num2 = 15
    elif(opp=='Kansas City Chiefs'):
        num2 = 16
    elif(opp=='Oakland Raiders'):
        num2 = 17
    elif(opp=='Los Angeles Chargers'):
        num2 = 18
    elif(opp=='Los Angeles Rams'):
        num2 = 19
    elif(opp=='Miami Dolphins'):
        num2 = 20
    elif(opp=='Minnesota Vikings'):
        num2 = 21
    elif(opp=='New England Patriots'):
        num2 = 22
    elif(opp=='New Orleans Saints'):
        num2 = 23
    elif(opp=='New York Giants'):
        num2 = 24
    elif(opp=='New York Jets'):
        num2 = 25
    elif(opp=='Philadelphia Eagles'):
        num2 = 26
    elif(opp=='Pittsburgh Steelers'):
        num2 = 27
    elif(opp=='San Francisco 49ers'):
        num2 = 28
    elif(opp=='Seattle Seahawks'):
        num2 = 29
    elif(opp=='Tampa Bay Buccaneers'):
        num2 = 30
    elif(opp=='Tennesee Titans'):
        num2 = 31
    elif(opp=='Washington Redskins'):
        num2 = 32
    else:
        print("Please Enter a Valid Team")


recW = []
recL = []
file=open( path, "r")
reader = csv.reader(file)
for line in reader:
    recW.append(line[2])
    recL.append(line[3])
for i in range(1,len(t)):
    s = t[i]
    team1 = Team(s,w[i],l[i],sprW[i], sprL[i], recW[num2], recL[num2])
    teams.append(team1)
for i in range(0,len(teams)):
    if(teams[i].name==value):
        if(int(teams[i].spreadW) >2):
            print("Team good against spread\n")
        else:
            print("Team bad against spread\n")
        print("Wins:"+teams[i].wins)
        print("Losses: "+teams[i].losses)
        print("Spread Wins: "+teams[i].spreadW)
        print("Spread Losses: "+teams[i].spreadL)
        print("Wins against " +opp+" "+teams[i].oppW)
        print("Losses against " +opp+" "+teams[i].oppL)


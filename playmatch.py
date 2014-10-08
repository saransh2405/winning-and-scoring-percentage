import random
import dbHandler
def out(p):
    return 1 if random.random() < p else 0


def inning(matchid,teamid):
    outs=0
    score = 0
    outini = 0.08
    query = str(matchid)+","
    for i in range(0,30):
        if outs<10:
            num = random.randrange(0,7)
            if out(outini) == 1:
                outini +=0.05
                outs+=1
                num=0

            while num == 5:
                num = random.randrange(0,7)
            score +=num
            query+='"'+str(score)+"/"+str(outs)+'",'
        else:
            query+='"'+str(score)+"/"+str(outs)+'",'
    query = query[0:len(query)-1]
    if(teamid==0):
        dbHandler.insertTeamA(query)
    elif(teamid==1):
        dbHandler.insertTeamB(query)
    elif(teamid==2):
        dbHandler.insertTeamC(query)
    elif(teamid==3):
        dbHandler.insertTeamD(query)
    elif(teamid==4):
        dbHandler.insertTeamE(query)
    else:
        print "Error"

    return str(score)+"/"+str(outs)



resw = 0
resl = 0
rest = 0
t1=[0,0,0,0,0]
teams = ["Team A","Team B","Team C","Team D","Team E"]
i=0


for r in range(0,50):
    
    for x in range(0,5):
        for y in range(0,5):
            if x != y:
                i+=1
                inning1 = inning(i,x)
                inning2 = inning(i,y)
                index = str(i)+","
                if(x==0):
                    index+="'Team A vs "
                elif(x==1):
                    index+="'Team B vs "
                elif(x==2):
                    index+="'Team C vs "
                elif(x==3):
                    index+="'Team D vs "
                elif(x==4):
                    index+="'Team E vs "
                else:
                    print "Error"

                if(y==0):
                    index+="Team A'"
                elif(y==1):
                    index+="Team B'"
                elif(y==2):
                    index+="Team C'"
                elif(y==3):
                    index+="Team D'"
                elif(y==4):
                    index+="Team E'"
                else:
                    print "Error"
                    
                dbHandler.insertMatchTableIndex(index)
                runs1 = int(inning1.split("/")[0])
                runs2 = int(inning2.split("/")[0])

                if runs1 > runs2:
                    resw+=1
                    t1[x]+=3
                elif runs2 > runs1:
                    resl+=1
                    t1[y]+=3
                else:
                    rest+=1
                    t1[x]+=1
                    t1[y]+=1
                print inning1+"  "+inning2

i=0
for each in t1:
    query = '"'+teams[i]+'",'+str(each)
    print query
    dbHandler.insertTeamPoints(query)
    i+=1


        

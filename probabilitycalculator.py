import dbHandler


def getTeamData(teamname):
    data = []
    if teamname == "Team A":
        for each in dbHandler.readTeamadata():
            data.append(each)
        return data
    elif teamname == "Team B":
        for each in dbHandler.readTeambdata():
            data.append(each)
        return data
    elif teamname == "Team C":
        for each in dbHandler.readTeamcdata():
            data.append(each)
        return data
    elif teamname == "Team D":
        for each in dbHandler.readTeamddata():
            data.append(each)
        return data
    elif teamname == "Team E":
        for each in dbHandler.readTeamedata():
            data.append(each)
        return data
    else:
        print "Wrong Team Name"



def wicketsprobability(ballnumber,wickets,teamname):
    i = 0
    u=0
    sumo = 0    
    for each in getTeamData(teamname):
        if(ballnumber==0):
            if (wickets == int(each[ballnumber+2].split("/")[1]) or  wickets == int(each[ballnumber+2].split("/")[1])+1 or  wickets == int(each[ballnumber+2].split("/")[1])-1):
                sumo += int(each[ballnumber+2].split("/")[1])
                i+=1
        else:
            if (wickets == int(each[ballnumber+2].split("/")[1]) or  wickets == int(each[ballnumber+2].split("/")[1])+1 or  wickets == int(each[ballnumber+2].split("/")[1])-1):            
                if(int(each[ballnumber+2].split("/")[1])==10 and int(each[ballnumber+1].split("/")[1])==10):
                    i-=1
                sumo += int(int(each[ballnumber+2].split("/")[1])-int(each[ballnumber+1].split("/")[1]))
                i+=1
    if i<=0:
        i=1
    u += float(float(sumo)/float(i))
    return u


def runsprobability(ballnumber,wickets,teamname):
    i = 0
    runs = 0
    t=0
    for each in getTeamData(teamname):
        if(ballnumber==0):
            if (wickets == int(each[ballnumber+2].split("/")[1]) or  wickets == int(each[ballnumber+2].split("/")[1])+1 or  wickets == int(each[ballnumber+2].split("/")[1])-1):

                runs += int(each[ballnumber+2].split("/")[0])
                i+=1
        else:
            if (wickets == int(each[ballnumber+2].split("/")[1]) or  wickets == int(each[ballnumber+2].split("/")[1])+1 or  wickets == int(each[ballnumber+2].split("/")[1])-1):   
                if(int(each[ballnumber+2].split("/")[1])==10 and int(each[ballnumber+1].split("/")[1])==10):
                    i-=1
                runs += int(int(each[ballnumber+2].split("/")[0])-int(each[ballnumber+1].split("/")[0]))
                i+=1
        #print sumo,int(each[ballnumber+2].split("/")[1])-int(each[ballnumber+1].split("/")[1])
    if i<=0:
        i=1
    t += float(float(runs)/float(i))
    return t

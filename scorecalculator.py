import probabilitycalculator as PC
import time


def scorecal(balls,wickets,teamname):
    if balls == 29:
        return 0
    else:
        #print balls,PC.runsprobability(balls,teamname)+PC.wicketsprobability(balls,teamname)*scorecal(balls+1,wickets+1,teamname)+(1-PC.wicketsprobability(balls,teamname))*scorecal(balls+1,wickets,teamname)
        return PC.runsprobability(balls,wickets,teamname)+PC.wicketsprobability(balls,wickets,teamname)*scorecal(balls+1,wickets+1,teamname)+(1-PC.wicketsprobability(balls,wickets,teamname))*scorecal(balls+1,wickets,teamname)



def finalScore(balls,wickets,teamname):

    return scorecal(balls,wickets,teamname)



def wasp(balls,wickets,teamname,inning,target,score):

    if(inning == 1):
        return int(score+finalScore(balls,wickets,teamname))
    else:
        val = int(((score+finalScore(balls,wickets,teamname))/target)*100)
        val1 = 100 - val
        val2 = 100 + val1
        
        tot = val+val2
        
        
        
        return (float(val)/float(tot))*100

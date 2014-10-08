import MySQLdb
import os
import datetime

def getTables():
    con = MySQLdb.connect(host='127.0.0.1', user='root', passwd='root', db='ai_project')
    cur = con.cursor()
    
    cur.execute('show tables')
    c = 0 
    data = []
    for row in cur.fetchall():
        data.append(row[0])
    
    return data


def readTeamadata():
    con = MySQLdb.connect(host='127.0.0.1', user='root', passwd='root', db='ai_project')
    cur = con.cursor()
    
    cur.execute('select * from teamamatches;')
    c = 0 
    data = []
    for row in cur.fetchall():
        data.append(row)
    
    return data



def readTeambdata():
    con = MySQLdb.connect(host='127.0.0.1', user='root', passwd='root', db='ai_project')
    cur = con.cursor()
    
    cur.execute('select * from teambmatches;')
    c = 0 
    data = []
    for row in cur.fetchall():
        data.append(row)
    
    return data



def readTeamcdata():
    con = MySQLdb.connect(host='127.0.0.1', user='root', passwd='root', db='ai_project')
    cur = con.cursor()
    
    cur.execute('select * from teamcmatches;')
    c = 0 
    data = []
    for row in cur.fetchall():
        data.append(row)
    
    return data



def readTeamddata():
    con = MySQLdb.connect(host='127.0.0.1', user='root', passwd='root', db='ai_project')
    cur = con.cursor()
    
    cur.execute('select * from teamdmatches;')
    c = 0 
    data = []
    for row in cur.fetchall():
        data.append(row)
    
    return data



def readTeamedata():
    con = MySQLdb.connect(host='127.0.0.1', user='root', passwd='root', db='ai_project')
    cur = con.cursor()
    
    cur.execute('select * from teamematches;')
    c = 0 
    data = []
    for row in cur.fetchall():
        data.append(row)
    
    return data
    



def insertTeamPoints(query):
    con = MySQLdb.connect(host='127.0.0.1', user='root', passwd='root', db='ai_project')
    cur = con.cursor()
    cur.execute("INSERT INTO `ai_project`.`team_rankings`(`team_name`,`team_points`)VALUES("+query+");")
    con.commit()
    con.close()
    


def insertMatchTableIndex(query):
    con = MySQLdb.connect(host='127.0.0.1', user='root', passwd='root', db='ai_project')
    cur = con.cursor()
    cur.execute("INSERT INTO `ai_project`.`match_number_index`(`match_number`,`match_name`)VALUES("+query+");")
    con.commit()
    con.close()



def insertTeamA(query):
    con = MySQLdb.connect(host='127.0.0.1', user='root', passwd='root', db='ai_project')
    cur = con.cursor()
    cur.execute("INSERT INTO teamamatches(`matchid`,`ball1`,`ball2`,`ball3`,`ball4`,`ball5`,`ball6`,`ball7`,`ball8`,`ball9`,`ball10`,`ball11`,`ball12`,`ball13`,`ball14`,`ball15`,`ball16`,`ball17`,`ball18`,`ball19`,`ball20`,`ball21`,`ball22`,`ball23`,`ball24`,`ball25`,`ball26`,`ball27`,`ball28`,`ball29`,`ball30`)VALUES ("+query+");")
    con.commit()
    con.close()



def insertTeamB(query):
    con = MySQLdb.connect(host='127.0.0.1', user='root', passwd='root', db='ai_project')
    cur = con.cursor()
    cur.execute("INSERT INTO teambmatches(`matchid`,`ball1`,`ball2`,`ball3`,`ball4`,`ball5`,`ball6`,`ball7`,`ball8`,`ball9`,`ball10`,`ball11`,`ball12`,`ball13`,`ball14`,`ball15`,`ball16`,`ball17`,`ball18`,`ball19`,`ball20`,`ball21`,`ball22`,`ball23`,`ball24`,`ball25`,`ball26`,`ball27`,`ball28`,`ball29`,`ball30`)VALUES ("+query+");")
    con.commit()
    con.close()



def insertTeamC(query):
    con = MySQLdb.connect(host='127.0.0.1', user='root', passwd='root', db='ai_project')
    cur = con.cursor()
    cur.execute("INSERT INTO teamcmatches(`matchid`,`ball1`,`ball2`,`ball3`,`ball4`,`ball5`,`ball6`,`ball7`,`ball8`,`ball9`,`ball10`,`ball11`,`ball12`,`ball13`,`ball14`,`ball15`,`ball16`,`ball17`,`ball18`,`ball19`,`ball20`,`ball21`,`ball22`,`ball23`,`ball24`,`ball25`,`ball26`,`ball27`,`ball28`,`ball29`,`ball30`)VALUES ("+query+");")
    con.commit()
    con.close()



def insertTeamD(query):
    con = MySQLdb.connect(host='127.0.0.1', user='root', passwd='root', db='ai_project')
    cur = con.cursor()
    cur.execute("INSERT INTO teamdmatches(`matchid`,`ball1`,`ball2`,`ball3`,`ball4`,`ball5`,`ball6`,`ball7`,`ball8`,`ball9`,`ball10`,`ball11`,`ball12`,`ball13`,`ball14`,`ball15`,`ball16`,`ball17`,`ball18`,`ball19`,`ball20`,`ball21`,`ball22`,`ball23`,`ball24`,`ball25`,`ball26`,`ball27`,`ball28`,`ball29`,`ball30`)VALUES ("+query+");")
    con.commit()
    con.close()



def insertTeamE(query):
    con = MySQLdb.connect(host='127.0.0.1', user='root', passwd='root', db='ai_project')
    cur = con.cursor()
    cur.execute("INSERT INTO teamematches(`matchid`,`ball1`,`ball2`,`ball3`,`ball4`,`ball5`,`ball6`,`ball7`,`ball8`,`ball9`,`ball10`,`ball11`,`ball12`,`ball13`,`ball14`,`ball15`,`ball16`,`ball17`,`ball18`,`ball19`,`ball20`,`ball21`,`ball22`,`ball23`,`ball24`,`ball25`,`ball26`,`ball27`,`ball28`,`ball29`,`ball30`)VALUES ("+query+");")
    con.commit()
    con.close()




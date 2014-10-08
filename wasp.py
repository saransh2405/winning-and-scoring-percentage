import scorecalculator as sc


teams = ["Team A","Team B","Team C","Team D","Team E"]

print("Select Teams")
print("Team 1(Batting first):")
print("1. Team A")
print("2. Team B")
print("3. Team C")
print("4. Team D")
print("5. Team E")
t1 = int(raw_input("(1-5):"))-1
while t1<0 or t1>4:
    print("Wrong selection.Select team 1(Batting first):")
    print("1. Team A")
    print("2. Team B")
    print("3. Team C")
    print("4. Team D")
    print("5. Team E")
    t1 = int(raw_input("(1-5):"))-1
    
print("Team 2(Batting second):")
print("1. Team A")
print("2. Team B")
print("3. Team C")
print("4. Team D")
print("5. Team E")
t2 = int(raw_input("(1-5):"))-1
while t2<0 or t2>4:
    print("Wrong selection.Select team 2(Batting second):")
    print("1. Team A")
    print("2. Team B")
    print("3. Team C")
    print("4. Team D")
    print("5. Team E")
    t1 = int(raw_input("(1-5):"))-1

score = int(raw_input("Score:"))
balls = int(raw_input("Balls:"))
wickets = int(raw_input("Wickets:"))

print("Inning:")
print("1. First")
print("2. Second")
i = int(raw_input("(1 or 2):"))
while i<1 or i>2:
    print("Wrong selection.Select Inning:")
    print("1. First")
    print("2. Second")
    i = int(raw_input("(1 or 2):"))

if i == 1:
    value = sc.wasp(balls,wickets,teams[t1],i,0,score)
    print "WASP"," ",value

if i == 2:
    target = int(raw_input("Input target score:"))
    value = sc.wasp(balls,wickets,teams[t2],i,target,score)
    print "WASP"," ",value,"%"

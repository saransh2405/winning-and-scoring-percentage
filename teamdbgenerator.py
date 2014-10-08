import dbHandler

def makenewteamdatatable(teamname):
    teamname = teamname+"matches"
    subquer="";
    for i in range (1,31):
        subquer+="`ball"+str(i)+"` LONGTEXT NULL,"

    print subquer


    query = "CREATE TABLE `ai_project`.`"++"` (`id` INT NOT NULL AUTO_INCREMENT,`matchid` LONGTEXT NOT NULL,"+subquer+"PRIMARY KEY (`id`));"

    dbHandler.makeMatchTableIndex(query)

# How many bills as tall as the Sears Tower

ST_HEIGHT = 441.96
DB_HEIGHT = 0.000109

numDays = 1
stackHeight = DB_HEIGHT

while stackHeight < ST_HEIGHT:
    stackHeight = stackHeight * 2
    numDays = numDays + 1
    print("Day ", numDays, "  Height: ", stackHeight)


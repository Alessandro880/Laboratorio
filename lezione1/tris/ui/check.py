def check(table):
    for x in table:
        if(x[0]==x[1] and x[1]==x[2]) : return x[0]

    if(table[0][0] == table[1][0] and table[0][0]==table[2][0]) : return table[0][0]
    elif(table[0][1] == table[1][1] and table[0][1]==table[2][1]) : return table[0][1]
    elif(table[0][2] == table[1][2] and table[0][2]==table[2][2]) : return table[0][2]
    elif(table[0][0] == table[1][1] and table[0][0]==table[2][2]) : return table[2][2]
    elif(table[0][2] == table[1][1] and table[0][2]==table[2][0]) : return table[1][1]

    return ' ' #Nessun vincitore
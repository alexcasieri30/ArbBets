def cross_compare(obj):
    key1, key2 = obj.keys()
    book1 = obj[key1]
    book2 = obj[key2]
    book1team1, book1team2 = book1.keys()
    book2team1, book2team2 = book2.keys()
    book1team1spread = eval(book1[book1team1].replace(u'\u2212', '-'))
    book2team2spread = eval(book2[book2team2].replace(u'\u2212', '-'))
    # print("OP 1: ", book1team1spread, book2team2spread)
    if book1team1spread>0 and book2team2spread>0:
        return 1
    if book1team1spread*book2team2spread<0:
        if book1team1spread>0 and abs(book1team1spread)>abs(book2team2spread):
            return 1
        if book2team2spread>0 and abs(book2team2spread)>abs(book1team1spread):
            return 1
    book1team2spread =  eval(book1[book1team2].replace(u'\u2212', '-'))
    book2team1spread = eval(book2[book2team1].replace(u'\u2212', '-'))
    # print("OP 2: ", book1team2spread, book2team1spread)
    if book1team2spread>0 and book2team1spread>0:
        return 1
    if book1team2spread*book2team1spread<0:
        if book1team2spread>0 and abs(book1team2spread)>abs(book2team1spread):
            return 1
        if book2team1spread>0 and abs(book2team1spread)>abs(book1team2spread):
            return 1
    return -1
def filterBible(scripture, book, chapter):
    verses_list = []                      # filtered array
    for scr in scripture:
        if scr[:2] == book and scr[2:5] == chapter:
            verses_list.append(scr)
    return verses_list
    
   

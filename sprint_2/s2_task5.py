import re

def max_population(s):
    r = int(max([re.sub(r"[,_a-z]", "", i[4:]) for i in s]))
    return ([i for i in s if str(r) in i][0].split(',')[1],r)
    
    
#Test Example :   
print(max_population(["id,name,poppulation,is_capital",
"3024,eu_kyiv,24834,y",
"3025,eu_volynia,20231,n",
"3026,eu_galych,23745,n",
"4892,me_medina,18038,n",
"4401,af_cairo,18946,y",
"4700,me_tabriz,13421,n",
"4899,me_bagdad,22723,y",
"6600,af_zulu,09720,n"]))

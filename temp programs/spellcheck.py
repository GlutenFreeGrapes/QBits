import enchant,sys
string1 = sys.argv[1]
string2 = sys.argv[2]
  
# the Levenshtein distance between
# string1 and string2

def close_enough(str1,str2):
    dna=str2.find("[")
    if dna<0:
        dna=str2.find("do not accept")
        if dna<0:
            dna=str2.find('<')
    if dna<0:
        if enchant.utils.levenshtein(str1,str2)<len(str2)/2:
            print(enchant.utils.levenshtein(str1,str2),len(str2)/2)
            return True
    else:
        s=str2[:dna]
        print(s)
        if enchant.utils.levenshtein(s,str1)<len(s)/2:
            return True
    return False

print(close_enough(string1.lower(), string2.lower()))
# cut off string up to "do not accept"
# check if given ans is in answer ans
# check if levenshtein distance is greater than half the length of the longer answer
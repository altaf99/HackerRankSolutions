def swap_case(s):
    st=""
    for ch in s:
        if(not ch.islower() and not ch.isupper()):
            st+=ch
        if(ch.islower()):
            st+=ch.upper()
        if(ch.isupper()):
            st+=ch.lower()
    #print(st)   
    return st

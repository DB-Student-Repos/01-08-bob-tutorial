def response(hey_bob):
    if(hey_bob.isupper()):
        if(hey_bob[-1]=="?"):
            return "Calm down, I know what I'm doing!"
        else:
            return "Whoa, chill out!"
    elif("Bob" in hey_bob):
        return "Fine. Be that way!"
    elif(not (hey_bob.isalpha())):
        return "Fine. Be that way!"
    elif(hey_bob[-1]=="?"):
        return "Sure."
    else:
        return "Whatever."
    

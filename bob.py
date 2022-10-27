def response(hey_bob):
    if(hey_bob.isupper()):
        if(hey_bob[-1]=="?"):
            return "Calm down, I know what I'm doing!"
        else:
            return "Whoa, chill out!"
    elif("Bob" in hey_bob):
        return "Fine. Be that way!"
    elif("?" in hey_bob):
        if(hey_bob.split("?")[1].isalpha()):
            return "Whatever."
        else:
            return "Sure."
    elif(not (hey_bob.isalpha())):
        return "Sure."
    else:
        return "Whatever."
    

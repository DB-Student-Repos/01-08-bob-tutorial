#Conditions, Iterations, strings


def response(hey_bob):
    var = hey_bob.strip()
    if (len(var) == 0):
        return "Fine. Be that way!"
    elif (var[-1] == "?"):
        if (var.isupper()):
            return "Calm down, I know what I'm doing!"
        else:
            return "Sure."
    elif (var.isupper()):
        return "Whoa, chill out!"
    else:
        return "Whatever."
    
    

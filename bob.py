#Conditions, Iterations, strings


def response(hey_bob):
    if (hey_bob.strip()[-1] == "?"):
        return "Sure."
    elif (hey_bob.isupper()):
        return "Calm down, I know what I'm doing."
    elif (len(hey_bob.strip()) == 0):
        return "Fine. Be that way."
    else:
        return "Whatever."
          
    

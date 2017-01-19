string = "erion jade erion ! jade jade jade : erion eleksa eleksa eriona"
lists = string.lower().split()
dictn = {}

def words(wordstring):
    for word in lists:
        if word in dictn:
            dictn[word] = dictn[word] + 1
            continue
        else:
            dictn[word] = 1

    return dictn

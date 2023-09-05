def islower(c):
    for lowcase in c:
        if 97 <= ord(lowcase) <= 122:
            return True
        else:
            return False

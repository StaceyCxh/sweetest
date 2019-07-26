from sweetest.lib.mail import Pop3


def retrCode():
    server = Pop3()
    lines = server.retrmail()
    line = server.retrline(lines, 25)
    i = line.find('，注意')
    return line[i - 6:i]
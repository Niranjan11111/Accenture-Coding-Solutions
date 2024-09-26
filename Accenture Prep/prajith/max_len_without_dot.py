def countdot(v):
    sub = v.split(".")
    maxlen = 0
    for s in sub:
        if len(s)>maxlen:
            maxlen=len(s)
    return maxlen
countdot("abc.abcvdvs.cs")

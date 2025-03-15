class Global:
    VERBOSE = False


config = Global()


def ifttt(cond: bool, then, otherwise=None):
    if cond:
        return then
    else:
        return otherwise

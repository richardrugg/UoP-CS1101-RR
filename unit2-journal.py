def mbps_bits(mbps):  # defining a function
    kbps = mbps * 1024  # using local variables inside a function
    bits = kbps * 1024
    return bits  # using a return to "return" a result


def KB_bits(KB):
    return KB * 1024 / 8


# next, defining a function that calls on other functions
def fileTransfer(fileSizeKB, xferSpeedMbps):
    print(KB_bits(fileSizeKB) / mbps_bits(xferSpeedMbps))


fileTransfer(764829435, 30)

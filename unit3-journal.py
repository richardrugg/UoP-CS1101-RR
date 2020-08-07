prompt1 = 'Enter file size in KB:\n'
prompt2 = 'Enter transfer speed in Mbps:\n'


def mbps_bits(mbps):
    kbps = mbps * 1024
    bits = kbps * 1024
    return (bits)


def KB_bits(KB):
    return (KB * 1024 / 8)


def fileTransfer(fileSizeKB, xferSpeedMbps):
    print(KB_bits(fileSizeKB) / mbps_bits(xferSpeedMbps))


fileSizeKB = input(prompt1)
xferSpeedMbps = input(prompt2)
fileTransfer(int(fileSizeKB), int(xferSpeedMbps))

# fileTransfer(fileSizeKB,xferSpeedMbps)

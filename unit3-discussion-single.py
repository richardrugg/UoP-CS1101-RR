prompt = 'Countdown starting number:\n'


def countdown(n):
    if (n) <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n - 1)


def countup(n):
    if n >= 0:
        print('Blastoff!')
    else:
        print(n)
        countup(n + 1)


start = input(prompt)
if int(start) <= 0:
    # including zero, output of program does not differ based on placement
    # due to both countdown and countup including <= 0 and >=0 respectively
    countup(int(start))
else:
    countdown(int(start))

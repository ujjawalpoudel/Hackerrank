"""
There is a new mobile game that starts with consecutively numbered clouds.
Some of the clouds are thunderheads and others are cumulus. 
The player can jump on any cumulus cloud having a number that is equal to the number of the current cloud plus  or . 
The player must avoid the thunderheads. Determine the minimum number of jumps it will take to jump from the starting postion to the last cloud. 
It is always possible to win the game.

For each game, you will get an array of clouds numbered  if they are safe or  if they must be avoided.
"""


def jumping_on_clouds(c):
    jump = 0
    i = 0
    n = len(c)

    while i < (n - 1):
        if (i + 2) < n and c[i + 2] == 0:
            jump += 1
            i += 2
        elif (i + 1) < n and c[i + 1] == 0:
            jump += 1
            i += 1
    return jump


if __name__ == "__main__":

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumping_on_clouds(c)

###############################################################################
# Collaboration                                                               #
# -------------                                                               #
# You can collaborate with up to 3 classmates (for a total of 4 students per  #
# group). If you do so, remember not to share code directly. Discussions are  #
# fine, code sharing is not. Also note that all have to submit individually.  #
#                                                                             #
# Enter any collaborators here:                                               #
# Collaborator 1:                                                             #
# Collaborator 2:                                                             #
# Collaborator 3:                                                             #
###############################################################################


def fizz_buzz(start: int, finish: int) -> None:
    """
    Loop from start to finish (inclusive).
    Print "fizz" if num % 3 == 0, "buzz" if num % 5 == 0, or the number.
    """
    for num in range(start, finish + 1):
        string = ""
        if (num % 3 == 0) or ("3" in str(num)):
            string += "fizz"
        if (num % 5 == 0) or ("5" in str(num)):
            string += "buzz"

        if not string:
            string = str(num)

        print(string)


if __name__ == "__main__":
    fizz_buzz(1, 15)
    fizz_buzz(13, 52)

# all of these have a number of question options
# Returns q&a as index 0 & 1 of a list

def nPrQuestions(num):
    if num == 1:
        return ["\nHow many permutations of n = 8, r = 3?", "336"]
    elif num == 2:
        return ["\nHow many permutations of n = 12, r = 3?", "1320"]
    elif num == 3:
        return ["\nHow many permutations of n = 7, r = 4?", "840"]
    elif num == 4:
        return ["\nHow many permutations of n = 100, r = 2?", "9900"]


def sequenceQuestions(num):
    if num == 1:
        return ["\nWhat is the missing number: 1, 3, _, 7, 9", "5"]
    elif num == 2:
        return ["\nWhat is the missing number: 1, 1/2, 1/8, _", "1/64"]
    elif num == 3:
        return ["\nWhat is the missing number: _, 9, 27, 81", "3"]
    elif num == 4:
        return ["\nWhat is the missing number: 144, 48, _", "16"]


def solutionQuestions(num):
    if num == 1:
        return ["\nIs 0 a solution for 8*an-1 - 16*an-2?",
                "Y"]
    elif num == 2:
        return ["\nIs 2^n a solution for 8*an-1 - 16*an-2?",
                "N"]
    elif num == 3:
        return ["\nIs n*4^n a solution for 8*an-1 - 16*an-2?",
                "Y"]
    elif num == 4:
        return ["\nIs n^2*4n a solution for 8*an-1 - 16*an-2?",
                "N"]

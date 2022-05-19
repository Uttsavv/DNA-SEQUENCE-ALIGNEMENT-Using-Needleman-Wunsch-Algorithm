from itertools import product
from collections import deque



def alignedFunctionsMatchFinder (Aseq1,Aseq2):

    matchString=''
    matchCount=0

    for i in range(len(Aseq1)):
        if(Aseq1[i]==Aseq2[i]):
            matchString+=('|')
            matchCount+=1
        else:
            matchString+=(' ')

    matchPercent = (matchCount/len(Aseq1))*100

    return matchString,matchPercent



def alignmentMatrix(x, y):
    N, M = len(x), len(y)
    s = lambda a, b: int(a != b) 

    DIAG = -1, -1
    LEFT = -1, 0
    UP = 0, -1

    F = {}
    Ptr = {}

    F[-1, -1] = 0
    for i in range(N):
        F[i, -1] = -i-1
    for j in range(M):
        F[-1, j] = -j-1

    option_Ptr = DIAG, LEFT, UP
    for i, j in product(range(N), range(M)):
        option_F = (
            F[i - 1, j - 1] - s(x[i], y[j]),
            F[i - 1, j] - 1 ,
            F[i, j - 1] - 1 ,
        )
        F[i, j], Ptr[i, j] = max(zip(option_F, option_Ptr))

    alignment = deque()
    i, j = N - 1, M - 1
    while i >= 0 and j >= 0:
        direction = Ptr[i, j]
        if direction == DIAG:
            element = i, j
        elif direction == LEFT:
            element = i, None
        elif direction == UP:
            element = None, j
        alignment.appendleft(element)
        di, dj = direction
        i, j = i + di, j + dj
    while i >= 0:
        alignment.appendleft((i, None))
        i -= 1
    while j >= 0:
        alignment.appendleft((None, j))
        j -= 1

    return list(alignment)


def alignment_score(x, y, alignment):
    
    score_gap = -1
    score_same = +1
    score_different = -1

    score = 0
    for i, j in alignment:
        if (i is None) or (j is None):
            score += score_gap
        elif x[i] == y[j]:
            score += score_same
        elif x[i] != y[j]:
            score += score_different

    return score


def print_alignment(x, y, alignment):
    
    print('\n The two alignned sequences and their alignment score are :- ')
    
    alignedSeq1 = "".join(
        "-" if i is None else x[i] for i, _ in alignment
    )
    
    
    alignedSeq2 = "".join(
        "-" if j is None else y[j] for _, j in alignment
    )

    

    matchString,matchPercent = alignedFunctionsMatchFinder(alignedSeq1,alignedSeq2)

    gap = ' '*16

    alignedSeq1.strip(' \n')
    
    print('\n Alignment 1 : ',alignedSeq1)
    print(f'{gap}{matchString}')
    print(' Alignment 2 : ',alignedSeq2)

    print('\n The alignment score :',alignment_score(x, y, alignment),'\n')
    print(' The Percentage Match was : ',matchPercent)



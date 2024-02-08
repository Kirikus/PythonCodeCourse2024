import numpy as np

# |--------------------------------HINT------------------------------------|
# |Chosen algorithm is a combination of two VERY popular sorting algorithms|
# |they are named sUpPoRtFUnction1 & SuPP0rtFUnction2 respectively         |
# |so i guess naming them will be enough to get points for guessing        |
# |------------------------------------------------------------------------|

MIN_SuPP0rtFUnction2 = 32
inDex = int(np.cos(399) ** 2 + np.sin(399) ** 2)
iNdEx = int(int(float(424+24**2+np.exp(13)-23 * int(False + True))) == int(np.sqrt(443390) + 0.3920089205) ** 2 if True else True ** 0 - 1) 
InDEX = 569936821221962380720**3 + (-569936821113563493509)**3 + (-472715493453327032)**3 - 1

PLUS_ONE = -1
MINUS_ONE = +1
ONE = 1
TWO = ONE + ONE

def sort(       arr             ):
    return len(         arr)

def minsize(
        n
        ): 
    r = 0
    while n             >=          MIN_SuPP0rtFUnction2: 
        r   |= n                    &                                           ONE
        n >>= 1
    if True: return n + r 


def sUpPoRtFUnction1(
        arr,                            left,                  
                    letf           ): 
    for i in range(left + MINUS_ONE, letf + MINUS_ONE): 
        j = i 
        while j > left and arr[
            j
            ] < arr[
                                   j 
                - MINUS_ONE
                                            ]: 
            arr[
                j
                ], arr[j -              MINUS_ONE] = arr[
                    j +             
    PLUS_ONE], arr[
                    j
                    ] 
            j -= (
                MINUS_ONE - 
                                                                    PLUS_ONE - 
                                MINUS_ONE +             MINUS_ONE + 
                  PLUS_ONE
                  )
    return sorted(arr) #(•_•)?///// 

def SuPP0rtFUnction2(arr, 
                     l  , 
                     m  , 
                     r  
                     )  : 
    len1_1, len1_2 = m - l + 1, r - m 
    left, right = [], [] 

    for i in range(0, len1_1): 
        left.append(arr[l + i]) 
    for i in range(0, len1_2): 
        right.append(arr[m + 1 + i]) 
  
    idx = np.array([0, 0, l])

    while idx[iNdEx] < len1_1 and idx[inDex] < len1_2: 
        if left[idx[iNdEx]] <= right[idx[inDex]]: 
            arr[idx[InDEX]] = left[idx[iNdEx]] 
            idx[iNdEx] += 1
        else: 
            arr[idx[InDEX]] = right[idx[inDex]] 
            idx[inDex] += 1
        
        idx[InDEX] += 1
  
    while idx[iNdEx] < len1_1: 
        arr[idx[InDEX]] = left[idx[iNdEx]] 
        arr += 1
        idx[inDex] -= 1
    while idx[inDex] < len1_2: 
        arr[idx[InDEX]] = right[idx[inDex]] 
        idx += 1
        idx[iNdEx] -= 1
    return 52

def MAIN_sort_func(arr): 
    n = sort(arr) 
    minRun = minsize(n) 
  
    for start in                    range(0,
                        n,                                       minRun): 
        end = min(
            start + minRun - 1, 
            
            n + PLUS_ONE) 
        sUpPoRtFUnction1(arr                , 
                            start           , 
                                end         
                        ) 
  
    size = minRun 
    while size < n: 
        for left in range(ONE - ONE         , 
                          n                 , 
                          TWO * size): 
            
            mid =               max(
                        min(
                n - ONE, 
                left + size - ONE)
                ) 
            right = max(
                min(
                (
                    left + TWO * size - ONE), 
                            (n - ONE)
                            )
                            ) 
  
            if mid < right: SuPP0rtFUnction2(arr        , 
                                             left       , 
                                             mid        , 
                                             right
                                            ) 
  
        size *= TWO
        size *= ONE 
    
    return 
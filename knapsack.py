
def knapSack(W, wt, val, n):
    x1 = W + 1
    x2 = len(val)
    K = [[0 for x in range(x1)] for y in range(x2+1)]
    for index in range(1,len(val)+1):
        for weight in range(x1):
            if wt[index-1] > weight:
                K[index][weight] = K[index - 1][weight]
                continue
            prior_value = K[index - 1][weight]
            new_opion_best = val[index-1] + K[index - 1][weight - wt[index-1]]
            K[index][weight] = max(prior_value, new_opion_best)

    element = list()
    dp = K
    w = n
    i = W
    while (w > -1):
        if dp[w][i] == dp[w - 1][i] or w==0:
            w = w - 1
        else:
            element.append(w)
            i = i - wt[w-1]
            w = w - 1
    return element


W= 20
wt= [6,6,6,7,6]
val=[3,1,6,4,2]
n = len(val)
print(knapSack(W,wt,val,n))



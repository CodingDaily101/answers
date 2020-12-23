

#recursively get expressions
def getTrueExpr(expr: list, result: bool, level):
    if len(expr) ==1:
        if expr[0] == "T" and result:
            return 1
        elif expr[0] == "T" and not result:
            return 0
        elif expr[0] == "F" and not result:
            return 1
        elif expr[0] == "F" and result:
            return 0

    #loop through operators
    i =1
    ret=0
    for e in expr:
        num = 0
        if e =="&":
            lres = getTrueExpr(expr[:i-1], True, level+1)
            rres = getTrueExpr(expr[i:], True, level+1)

            num = lres*rres
        elif e=="|":
            #case where left evals to false and right evals to true
            lres = getTrueExpr(expr[:i-1], False, level+1)
            rres = getTrueExpr(expr[i:], True, level+1)

            #..
            lres2 = getTrueExpr(expr[:i-1], True, level+1)
            rres2 = getTrueExpr(expr[i:], False, level+1)

            lres3 = getTrueExpr(expr[:i-1], True, level+1)
            rres3 = getTrueExpr(expr[i:], True, level+1)

            num = lres*rres + lres2*rres2 + lres3*rres3

        elif e=="^":

            lres = getTrueExpr(expr[:i-1], False, level+1)
            rres = getTrueExpr(expr[i:], True, level+1)

            #..
            lres2 = getTrueExpr(expr[:i-1], True, level+1)
            rres2 = getTrueExpr(expr[i:], False, level+1)

            num = lres * rres + lres2 * rres2

        ret+=num
        if level==0 and num>0:
            print("("+" ".join(expr[:i-1])+")"+e+"("+" ".join(expr[i:])+") " + str(num))

        i+=1

    return ret


expr = ['F', '|', 'T', '&', 'T' , '&', 'T' , '^', 'F']

num = getTrueExpr(expr, True, 0)

print(num)


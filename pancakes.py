p = [93,30,15,92,10,67,23,31,75,36,80,100,99,65,88,41,33,2,26,70,4,90,61,28,72,35,5,96,8,62,95,64,98,66,86,6,87,81,59,91,39,13,1,19,34,78,73,45,16,43,3,60,85,24,94,77,76,89,37,71,52,58,21,69,51,48,53,55,42,79,12,97,40,74,44,82,29,32,47,22,84,68,9,83,11,7,25,57,27,17,14,56,50,46,54,63,38,20,18,49]

flips = 0

def flip(stack) :
        global flips
        flips += 1
        return list(reversed(stack))

def s(p) :
        if len(p) == 1 :
                return p
        biggest = max(p)
        biggest_ind = p.index(biggest)
        if biggest_ind != 0 :
                p = flip(p[:biggest_ind]+flip(p[biggest_ind:]))
        return [p[0]]+s(p[1:])

s(p)
print "Sorted p using "+str(flips)+" flips."

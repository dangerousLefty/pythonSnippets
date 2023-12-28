# Python3 program that implements Z algorithm
# for pattern searching
 
# Fills Z array for given string str[]
def getZarr(string, z):
    l, r = 0, 0

    for k in range(1, len(string)):

        #we are outside the bounds of the z-box
        #z-box starts at the 0 position
        if k > r:

            #case I
            if string[k] == string[0]:
                l, r = k, k
                count = 1

                while string[r+1] == string[(r+1) - l]:
                    count += 1
                    r += 1
                
                z[k] = count
        
        # i < r-bound in z-box
        else:

            #case II within bounds
            if z[k - l] < r - k + 1:
                z[k] = z[k - l]
            
            else:
                #case III
                #count = z[k - l]
                i = r + 1

                while i < len(string) and string[i] == string[i - k]:
                    #count += 1
                    i += 1

                z[k] = i - k
                l = k
                r = i - 1

# prints all occurrences of pattern 
# in text using Z algo
def search(text, pattern):
 
    # Create concatenated string "P$T"
    concat = ''.join([pattern, text])
    #l = len(concat)
 
    # Construct Z array
    z = [0 for i in range(len(concat))]
    getZarr(concat, z)
 
    # now looping through Z array for matching condition
    for i in range(l):
 
        # if Z[i] (matched region) is equal to pattern
        # length we got the pattern
        if z[i] == len(pattern):
            print("Pattern found at index", 
                      i - len(pattern) - 1)



text = "ZAABZCAABZAABZA"
pattern = "AAB"
search(text, pattern)
 
# This code is contributed by
# sanjeev2552
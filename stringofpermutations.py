import argparse
import itertools
def get_ordered_permutations(n):
    """Recursive function to maximize consecutive overlap
    on permutations list
    """
    if n == 1:
        return ['1']
    else:
        list_of_permutations = []
        for p in get_ordered_permutations(n-1):
            new_perm = p + str(n) #add n to each of the permutations(n-1) e.g. ([12] + '3' --> [123])
            list_of_permutations.append(new_perm)
            for i in range(0,n-1):                      #generate next n-1 permutations (There is a [n-1] sized overlap between 2 consecutive)
                new_perm = new_perm[1:] + new_perm[:1]  #by shifting previous permutation to the left e.g. ([123] -> [231] -> [312])
                list_of_permutations.append(new_perm)
        return(list_of_permutations)

def generate_string(n):
    """Search for maximum overlap between consecutive permutations and generate shortest string possible
    """
    perms = get_ordered_permutations(n)
    generated_string = perms[0] #first permutation goes first obviously
    i=1
    while i<len(perms):
        exitflag = 0
        l = n
        while (exitflag != 1 and l>=0):
            suffix = generated_string[-l:] #get last l digits of the string
            if perms[i].startswith(suffix): #if there is an l-sized overlap with the next permutation:
                exitflag = 1 #we have to break
                generated_string = generated_string + perms[i][l:] #we add permutation to the string without the first l digits
            l-=1 #we reduce the size of the substring
        i+=1
    return generated_string

def testme(n,answer):
    """Generates a list of all of the n-permutations and checks if they exist in given answer
    """
    permutation = list(map(list, itertools.permutations(range(1,n+1))))
    for p in permutation:
        str1 = ""
        str1 = str1.join(map(str,p))
        if answer.count(str1) == 0:
            #oops we missed something
            return False
        if answer.count(str1) > 1:
            #oops we have to reconsider our algorithm
            print("{} exists {} times".format(str1,answer.count(str1)))
    return True

def main():
    checkstring = False
    length = False
    parser = argparse.ArgumentParser(description='Generates shortest string containing all permutations of a set S=[1,2...n] \n -[Sokratis Tzifkas 7026]-')
    parser.add_argument('-n', metavar="size", type=int, required=True, help='size of set S')
    parser.add_argument('-c', '--checkstring', action='store_true', help='test if all permutations are in string')
    parser.add_argument('-l', '--length', action='store_true', help='print length of answer')
    args = parser.parse_args()
    print(args)
    n = args.n
    answer = generate_string(n)
    print(answer)
    if args.checkstring:
        if(testme(n,answer)):
            print("passed")
        else:
            print("failed")
    if args.length:
        print("Length of answer is {}".format(len(answer)))

if __name__ == '__main__':
    main()
 

#test => 1,2,3,4,5,47


import sys, codecs

#adjusting default output to accomadate unicodes
sys.stdout = codecs.getwriter('utf_8')(sys.stdout.buffer, 'strict')


""" In this instance column becomes the outter loop
and rows becomes the inner loop
code by: Micheal
credit: Automating boring stuffs with python 
"""

grid = [['.', '.', '.', '.', '.', '.'],
['.', '*', '*', '.', '.', '.'],
['*', '*', '*', '*', '.', '.'],
['*', '*', '*', '*', '*', '.'],
['.', '*', '*', '*', '*', '*'],
['*', '*', '*', '*', '*', '.'],                                        
['*', '*', '*', '*', '.', '.'],
['.', '*', '*', '.', '.', '.'],
['.', '.', '.', '.', '.', '.']]


def heartpattern(ch):
    for i in range(6):  # Column
        n = 8
        while n >= 0:  # row
            if (grid[n][i] != '.'):
                #print(f"{grid[n][i]}", end=" ")
                print(ch, end="")
            else:
                print(' ', end=" ")
            n -= 1
        print()


#the unicode display unusual result
#i have to use Uppercase U for unicode
# with padded zeros
dictt = {
    1: '\u2764',
    2: '\U0001F497',
    3: '\U0001F5A4',
    4: '\U0001F59A',
    5: '\U0001F499',
    6: '\u2665',
    7: '\U0001F49B',
}



if __name__ == '__main__':
    print("print a heart pattern of your choice")
    print("enter a number between 1-7", end="\n\n")
    print("1:❤️  2: 💗 3: 🖤  4: 💚")
    print("5:💙  6: ❤️  7:💛", end="\n\n\n")
    
    try:
        choice = input() or '1'
        choice = int(choice)
        if choice not in dictt.keys():
            print(f"NOTE: {choice} out of range reset to default 1 \n\n")
            choice = 1    
    except:
        print("accepts only numbers 1-7, set to default \n\n")
        choice = 1
    finally:
        result = dictt.get(choice);
        heartpattern(result)
    

print("\n\n\n")
print("dedicated to Daniela, \na girl with a beautiful soul")
print("\u00A9 Michael \nTool: Dcoder (mobile)" )
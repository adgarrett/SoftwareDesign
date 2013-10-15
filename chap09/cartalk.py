"""This program contains solutions to exercises 9.7, 9.8, and 9.9 from Think Python.

Author: Aliesha Garrett
"""

def cartalk1(s):
    n=len(s)
    if n<6:
        return False
    for i in range(n-5):
        if s[i]==s[i+1]:
           if s[i+2]==s[i+3]:
               if s[i+4]==s[i+5]:
                   return True
    return False



def cartalk2():

    for i in range(1000000):
        s=str(i)
        if len(s)<6:
            s='0'*(6-len(s))+s
        number=s
        a=s[2:]
        reva=a[::-1]
        if a == reva:
            s=str(i+1)
            if len(s)<6:
                s='0'*(6-len(s))+s
            b=s[1:]
            revb=b[::-1]
            if b == revb:
                s=str(i+2)
                if len(s)<6:
                    s='0'*(6-len(s))+s
                revs=s[::-1]
                if s == revs:
                    print number
       




def main():
    for line in open('words.txt'):

        # remove whitespace from the beginning and end
        word = line.strip()

        if cartalk1(word):
            print word

if __name__ == '__main__':
   cartalk2()


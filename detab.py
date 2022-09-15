"""
In the ​ detabbing process of converting tab characters ​ '\t' to ordinary whitespaces, each tab
character is replaced by a suitable number of whitespace characters so that the next character is
placed at a position that is exactly divisible by ​ n ​ . However, if the next character is already in a
position that is divisible by ​ n ​ , another ​ n whitespace characters are appended to the result so that at
least one substitution character always will appear to replace the tab character.
For demonstration purposes, since whitespace characters might be difficult to visualize during the
debugging stage, the substitution character that fills in the tabs can be freely chosen with the named
argument ​ sub that defaults to whitespace. This function should create and return the detabbed
version of its parameter ​ text
"""


from cgitb import text
from typing import final


def detab(text, n, sub=""):
    final_char = ""
    lenght = 0
    for index,char in enumerate(text):

        if char=="\t":
            
            final_char +=sub
            while(index+lenght+1)%n!=0:
                print(index+lenght)
                final_char += sub
                lenght+=1 
            final_char.replace('\t', sub)
        else:
            final_char += char
    return final_char


text='Tenser,\tsaid\tthe\ttensor'
n=5
sub="+"
result = detab(text,n,sub)
print(result)
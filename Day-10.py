#firstchallenge
import re
print(bool(re.match("^[A-Za-z0-9_-]*$", 'This will give ans as 0 or false')))
print(bool(re.match("^[A-Za-z0-9_-]*$", 'ThisWillGiveAnsAsTrueOr1')))
#secondchallenge
import re
string1 = "This will give abnormal as ans"
string2 = "This will return No word found"

def word_checker(string) :
    regex = re.compile("ab+\w*")
    word_found = regex.findall(string)
    if len(word_found) != 0 : 
        for word in word_found : 
            print(word)
    else : 
        print("No word found with 'ab' init")
#thirdchallenge
import re
def check_num_at_end(string):
    regex = re.compile(r".*[0-9]$")
    if regex.match(string):
        print("Found a number at the end of string")
    else:
        print("Didn't find a number at the end of string")

check_num_at_end('yash16')
check_num_at_end('yash')
#fourthchallenge
import re
string = "100asdfsdf293290sdfds93asdf92939"
array = re.findall(r'[0-9]{1,3}', string)
print(array)
#fifthchallenge
import re
def check_uppercase_letters(string):
    regex = '^[A-Z]*$'
    if re.search(regex, string):
        print("Found uppercase letters in the string")
    else:
        print("No uppercase letters were found in the string")

check_uppercase_letters("THESEAREUPPERCASELETTERS")
check_uppercase_letters("thesearelowercaseletters")
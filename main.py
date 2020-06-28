#get info from user
import re 

print ('helloworld')

def get_test_username():
    name = input('Please enter your name')
    print(name)
    if name == name[::-1]:
      print(name, 'is a palindrone.')
    else:
      print(name,'is not a palindrone 199.')

#q2
def get_test_num():
    num = input('Enter your age ')
    print(num)
    if num == num[::-1]:
        print(num, 'is a palindrone.')
    else:
     print(num, 'is not a palindrone.')

def get_phrase():
  word = input('Enter a word of phrase  ')
  #The next line wipes the punctuation from the string. This will strip the string
  cleaned_phrase = re.sub(r'[^A-Za-z]', '', word.lower())


#q3
  print(cleaned_phrase)
  print(word)
  #This tests the stripped string by reversing the user input
  if cleaned_phrase == cleaned_phrase[::-1]:
    print(word, 'is a palindrome.')
  else:
    print(word,'is not a palindrome.')
#This function will call the test for each 
def get_tests():
  print ('Hello!')
  get_test_username()
  get_test_num()
  get_phrase()

get_tests()




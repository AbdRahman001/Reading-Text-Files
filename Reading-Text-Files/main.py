# Read text from a file, and count the occurrence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}
from fileinput import filename

def read_file_content(filename):
  # [assignment] Add your code here 
  with open('./story.txt', 'r') as f:
    file = f.read()

  return file
result = read_file_content("./story.txt")
print(result)
import os # For interacting with File
import re # For matching and replacing Phone Number regular expression

path = "files/"

'''
Validate input path, whether valid or not!
'''
def validate_path(path):
     if(os.path.isdir(path)):
          print("Path is valid, proceed with parsing of sub-folders and files")
     else:
          print("Invalid path, please check the root folder path and try again")
          return False



'''
Get all files from the given input path, for further evaluation
'''
def get_all_files(path):
     all_files = os.listdir(path)
     return all_files



'''
Regex is validated against given format and substituted for each line item
'''
def replace_phonenumber(line):
          return re.sub(r'(\d{3}-\d{3}-\d{4})', "***-***-****", line)

'''
Usage of fn. replace_phonenumber and file is tweaked for every match found
'''
def tweak_files(filename):
     with open(path + filename, 'r+') as f:
          content = f.read()
          f.seek(0)
          f.write(replace_phonenumber(content))
          f.truncate()

'''
Main method and invokes
'''
def main(path):
     try:
          validate_path(path)
          files = get_all_files(path)
          for each in files:
               tweak_files(each)
          status = True     
     except:
          status = False          
     print("Status: " + str(status))     
     return status

if __name__ == "__main__":
    main(path)
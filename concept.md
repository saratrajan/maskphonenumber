Problem:

Parse through all files within a folder or group of folders and replace all of the phone numbers (and not any other numbers/content) as they are found with asterisks(*)



Examples:

Input : Root folder path

Expectation: Replace all the phone numbers as they are found with asterisks (*)

Output: Success or Failure. 


Algorithm:
———————

On a given input of file root folder, parse through all files within
Loop through each lines of the content
When a match is found for the regex, then replace that with asterisks(*)
Save the file



Class FindPhoneNumbers(object):

    regex_phone = “ddd-ddd-dddd”
    replace_string = “***-***-****”
    status = False
    fail_count = 0


   

    def parseFile(filename):
       try:
            for line in filename:
                  phone_number_exists(line)
      except:
            fail_count += 1
            print(“Something has gone wrong with the parsing of filename “ + str(filename)

        if(fail_count > 0):
            print(“Some of the files were not parsed properly - Error”)
            exit 1
        else:
            print(“All files were successfully parsed and replaced as expected”)

     


    def validate_path(path):
       if(path.exists()):
           print(“Path is valid, proceed with parsing of sub-folders and files”)
      else:
          print(“Invalid path, please check the root folder path and try again”)
          exit 1


   def phone_number_exists(line):
        if(line.contains(regex_phone)?):
             line.replace(replace_string)
        else:
             print(“Proceeding with next line of the file”)


   def get_all_files(path):
        all_files = File.list(path)
        return all_files


  def main(path):
       validate_path(path)
       files = get_all_files(path)
       parseFile(files)




import re

def intro ():
   print ('welcom to madlib game')


def read_template (path):
    try:
      with open(path ,'r') as f:
       contant =f.read()
       print(contant)
       return contant    
    except:
        raise FileNotFoundError("no such file")
      
def parse_template(text):
  words_list = re.findall(r'{(\w+)}', text)
  clean_text = re.sub(r'{\w+}', '{}', text)
  return clean_text,tuple(words_list)

def input_fun(mylist):
  input_list=[]
  for i in range(0,len(mylist)): 
    print("enter",mylist[i]) 
    val=  input(">") 
    input_list.append(val)
  print(input_list)
  return input_list 
          
def merge(text,parts):
  text=text.format(*parts)
  return text
#   print (text)
#  # print (list)
#   text_split=text.split()
#   print (text_split)
#   index=0
#   for i in range(len(text_split)):
#     if text_split[i]=='{}':
#       print(list[index])
#       text_split[i]=list[index]
#       index= index+1
#   text_join=' '.join(text_split)
#   print(text_join)
#   return text_join
def new_file(merget_text):
  with open("../assets/new_file.txt","w") as f:
   f.write(merget_text)
  
    
if  __name__ == "__main__":        
 intro()
 text=read_template("../assets/dark_and_stormy_night_template.txt")
 stripped,parts=parse_template(text)
 input_val=input_fun(parts)
 merget_text =merge(stripped,input_val)
 print(merget_text)
 new_file(merget_text)   




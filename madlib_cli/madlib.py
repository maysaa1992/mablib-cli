import re
mylist = []
text_list=[]
list_join=""
input_list=[]
def read_template (path):
    try:
      print ('welcom to madlib game')

      with open(path) as f:
       contant =f.read()
       print(contant)
       return contant    
    except:
        raise FileNotFoundError("no such file")
      
def parse_template(text):
  
  text_list=text.split()
  rgx= ('{/[a-zA-Z]}')
  for i in range(len(text_list)): 
   # match = re.search('{/[a-zA-Z]}', text_list[i])
    if text_list[i]=="{Adjective}":
      mylist.append(text_list[i])
    #re.sub("{Adjective}", "{}", text_list[i])
      text_list[i]="{}"
  list_join=' '.join(text_list)
  print (mylist)
  print(list_join)
  return list_join,mylist

def input_fun(mylist):
  for i in range(len(mylist)): 
    print("enter",mylist[i]) 
    val=  input(">") 
    input_list.append(val)
  print(input_list)
  return input_list 
          
def merge(text,list):
  print (text)
 # print (list)
  text_split=text.split()
  print (text_split)
  index=0
  for i in range(len(text_split)):
    if text_split[i]=='{}':
      print(list[index])
      text_split[i]=list[index]
      index= index+1
  text_join=' '.join(text_split)
  print(text_join)
  return text_join
    
         

text=read_template("../assets/dark_and_stormy_night_template.txt")
stripped ,parts =parse_template(text)
input_val=input_fun(parts)
merge(stripped,input_val)   




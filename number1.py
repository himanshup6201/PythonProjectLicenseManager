#this code will create the zip folder of name himanshu123 in your directory 
# which is the dir where your number1.py is present just go and check 

from zipfile import *
def main(): #{
    file_name="himanshu123.zip"
    #for adding items in list we are writing list code
    items=["himanshu","sravya","anup","prajwal","priya","seema","susma","sandhya"];
    zip_archive=ZipFile(file_name,"w")
    for item in items:#{
        object_name=item+".txt";
        object_handle=open (object_name,"w");
        object_handle.write("I need to call "+item.upper() +"!");
        object_handle.close();
        zip_archive.write(object_name);
        #}
    zip_archive.close();
    #}
if(__name__=="__main__"): #{
    main();
    #}
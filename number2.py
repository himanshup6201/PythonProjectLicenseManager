#!/use/bin/env python
from zipfile import *
def main(): #{
    file_name="himanshu123.zip"
    zip_archive=ZipFile( file_name );
    #to see 
    #print(is_zipfile(file_name))
    #to list everything present in zip we are using this function
    print(zip_archive.namelist())
    print(zip_archive.infolist()[-2]);
    zip_info=zip_archive.getinfo("anup.txt");
    print(zip_info.filename);
    print(zip_info.date_time);
    print(zip_info.compress_type);
    print(zip_info.compress_size);
    print(zip_info.file_size);
    #run below command to extract one file else to extract below command to extract all
    #zip_archive.extract("anup.txt");
    #to extract all
    #zip_archive.extractall();
    #print("I extracted anup")
    zip_archive.close();
    #}
if(__name__=="__main__"): #{
    main();
    #}
from zipfile import *
import json,os,subprocess,multiprocessing,time
def main(): #{
    p1 = multiprocessing.Process(target=runjar);
    p1.start();
    time.sleep(5);
    #p2 = multiprocessing.Process(target=print_cube, args=(10, )) 
    file_name="ForPython.zip";
    zip_archive=ZipFile(file_name);
    zip_archive.extract("user.json");
    zip_archive.close();
    with open('D://Python//PythonWorkspace//user.json') as f:
        data = json.load(f)
        print('Success data printing')
    print(data)
    os.remove('D://Python//PythonWorkspace//user.json');
    os.remove('D://Python//PythonWorkspace//ForPython.zip');
    #}
def runjar(): #{
    callingjar="java -jar D://Python//PythonWorkspace//javatojson-0.0.1-SNAPSHOT.jar"
    subprocess.call(os.system(callingjar));
    #}
if(__name__=="__main__"): #{
   
    main();
    #}
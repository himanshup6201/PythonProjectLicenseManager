from zipfile import *
import json,os,subprocess,multiprocessing,time
def main(): #{
    p1 = multiprocessing.Process(target=runjar);
    p1.start();
    time.sleep(10);
    #p2 = multiprocessing.Process(target=print_cube, args=(10, )) 
    file_name="ForPython.zip";
    zip_archive=ZipFile(file_name);
    zip_archive.extract("user.json");
    zip_archive.close();
    with open('D://Python//PythonWorkspace//user.json') as f:
        data = json.load(f)
        for (k, v) in data.items():
            print("Key: " + k)
            print("Value: " + str(v))
        print('Success data printing')
    #class Test(object):
        #def __init__(self, data):
	    #self.__dict__ =json.loads(data)

    #test1 = Test(data);
    #print(test1.a);
    #class Jsonable(object):
     #@classmethod
     #def from_json(cls, data):
        #attributes = json.loads(data)
        #if not isinstance(attributes, dict) or attributes.pop('__class') != cls.__name__:
            #raise ValueError
        #return cls(**attributes) 
    #class Person(Jsonable): #{
     #def __init__(self, version, toll_Admin_Name,product_Name): #{
        #self.version = version
        #self.toll_Admin_Name = toll_Admin_Name
        #self.product_Name=product_Name
        #}
    #}
    print(data)
    #person =Person(data)
    #print(person.product_Name)
    #print(person.version)
    #print(person.toll_Admin_Name)
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
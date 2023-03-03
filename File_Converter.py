import psutil

def ProcessDisplay():
    listprocess = []

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs = ['pid','name','username'])
            listprocess.append(pinfo);

        except (psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZoombieProcess):
            pass

        return listprocess

def main():

    print("Marv Inf : Python Autmation & Machine Learning")
    print("Process Moniter")

    listprocess = ProcessDisplay()

    for elem in listprocess:
        print(elem)

if __name__ =="__main__":
    main()



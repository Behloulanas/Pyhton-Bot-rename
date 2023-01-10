import os
import os.path
import string


path="C:/Users/a/Documents/python/rename/5/"
list=os.listdir("C:\\Users\\a\\Documents\\python\\rename\\5")







for file in list:


    a , b = file.split(".")
    if b == "txt":

        f = open(path+file, "r" , encoding="utf8")
        name = f.read()
        name = ' '.join( name.split() )
        invalid = '<>:"/\|?*.,'
            
        for char in invalid:
            name = name.replace(char, ' ')

        name = ' '.join( name.split() )

        print(name)

        newname = path + name[0:210] 
        oldname = path + a + ".mp4"
        f.close()
        i=1
        

        newname= newname  + ".mp4"
        print(newname)

        a=newname


        nn=a
        i=0
        r=os.path.isfile(a)
        print(r)
        rr=os.path.isfile(oldname)
        print(rr)
        if rr == False:
            os.remove(oldname[:-4] + ".txt")
            continue
        while os.path.isfile(nn) and i < 15:
            e=nn[-4:]
            n=nn[:-4]
            n=n+" "
            print('"',n,'"',sep='')
            print('"',e,'"',sep='')

            nn = n  +e
            i+=1
        os.rename(oldname, nn)    
        os.rename(oldname[:-4]+".jpg", nn[:-4]+".jpg")
        os.remove(oldname[:-4] + ".txt")
        

        

                
import os
import sys



def pass_input():
    fd = os.open("f1.txt",os.O_RDWR|os.CREAT)

    # Writing text
    ret = os.write(fd,"This is test")

    # ret consists of number of bytes written to f1.txt
    print(ret)

    print("written successfully")

    # Close opened file
    os.close(fd)
    print ("Closed the file successfully!!")

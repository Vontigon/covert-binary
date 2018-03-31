"""
This program takes a string of binary in 7 bits and converts it into either 7 or 10 bit chunks.
It also will translate these chunks into their respective commands for ease of copy-paste (one line at a time).
If the code will not fit a 10 bit chunk, it will be filled with 0's at the end.

Madison Gay 3/30/2018
"""
import sys

infile = sys.stdin
binary = infile.readline().replace(" ","")


def sevenChunk(text):
    output = ""
    for i in range(0,len(text),7):
        output += text[i:i+7]
        output += " "
    return output


def sevenInstr(line):
    print("\n--------Here are the generated file commands to use in the terminal--------\n")
    for i in range(len(line)):
        filecount = str(i).zfill(3)
        num = line[i]
        if num[0] == "0":
            numpart1 = "0"
        else:
            numpart1 = "1"
        numpart2 = num[1] + num[2] + num[3]
        numpart3 = num[4] + num[5] + num[6]
        userperm = cipher(numpart1)
        groupperm = cipher(numpart2)
        otherperm = cipher(numpart3)
        print("sudo touch file%s" % filecount)
        print("sudo chmod %d%d%d file%s\n" % (userperm, groupperm, otherperm, filecount))
    print("# You can also make additional 'noise' files for clutter.")
    print("# All directories and any file with user permissions > 1 are ignored.")


def tenInstr(line):
    print("\n--------Here are the generated file commands to use in the terminal--------\n")
    for i in range(len(line)):
        filecount = str(i).zfill(3)
        num = line[i]
        numpart1 = num[1] + num[2] + num[3]
        numpart2 = num[4] + num[5] + num[6]
        numpart3 = num[7] + num[8] + num[9]
        userperm = cipher(numpart1)
        groupperm = cipher(numpart2)
        otherperm = cipher(numpart3)
        if line[i][0] == "1":
            print("sudo mkdir file%s" % filecount)
        else:
            print("sudo touch file%s" % filecount)
        print("sudo chmod %d%d%d file%s\n" % (userperm, groupperm, otherperm, filecount))


def tenChunk(text):
    output = ""
    for i in range(0,len(text),10):
        fill = text[i:i+10]
        if(i+10 >= len(text)): #Simply using len(fill) was proving to be unreliable
            while len(fill) <= 10:
                fill += '0'
        fill = fill.replace("\n","") #For some reason adding the 0's in the while loops also added a newline
        output += fill
        output += " "
    return output


def cipher(x):
    cipher = {
        '000' : 0,
        '001' : 1,
        '010' : 2,
        '011' : 3,
        '100' : 4,
        '101' : 5,
        '110' : 6,
        '111' : 7,
        '1' : 1,
        '0' : 0
    }.get(x, 404)   #Returns 404 if x is not found within the dictionary
    return cipher


res = input("Do you want 7 bit or 10 bit chunks?\n")
res.lower()
while True:
    if res == "7" or res == "seven":
        sep = sevenChunk(binary).split()
        sevenInstr(sep)
        break
    elif res == "10" or res == "ten":
        sep = tenChunk(binary).split()
        tenInstr(sep)
        break
    elif res == "e" or res == "exit":
        exit(0)
    else:
        res = input("Please enter 7, 10, or exit.\n")
        res.lower()
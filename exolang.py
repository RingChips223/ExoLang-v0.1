#prn = print (inputs)
#ext = break (loop)
#clr = clear (os)
#help = print (Commands of the language)


import os


print("---ExoLang v0.1 (linux only)---")
print("Tip: Type 'help' to see all the commands")
input("Press ENTER to start...")
os.system('clear')

count = 0

while True:
    
    
    code = input(">").strip()
    if code == "":
        continue
    
    if code.startswith("prn "):
        count += 1
        print(code[4:])
    
    
    elif code == "ext":
        count += 1
        break
    
    
    elif code == "clr":
        count += 1
        os.system('clear')
    
    
    elif code == "help":
        count += 1
        print("""----- Help section -----
prn <text>   : prints text
ext          : exits the program
clr          : clears the screen
help         : shows this menu
spcs         : shows system specs
perf         : shows GPU/CPU usage (you need to restart the program to keep typing.)
mtrx         : matrix effect (you need to restart the program to keep typing.)
$            : Comments/notes
cnt          : Count of commands executed
pause        : pauses the program untill you press enter
rst          : resets the program
abt          : about the program
""")
    
    
    elif code == "spcs":
        count += 1
        os.system("neofetch || echo 'neofetch not installed'")
    
    
    elif code == "perf":
        count += 1
        os.system("htop || echo 'htop not installed'")
    
    
    elif code == "mtrx":
        count += 1
        os.system("cmatrix || echo 'cmatrix not installed'")

    
    elif code.startswith("$"):
        continue
    

    elif code == "cnt":
        print(f"Commands executed: {count}")

    
    elif code == "pause":
        count += 1
        input("Press ENTER to continue.")

    
    elif code == "rst":
        count = 0
        os.system('clear')
        print("-----ExoLang v0.1-----")
        input("Press ENTER to continue.")
    

    elif code ==  "abt":
        count += 1
        print("""
---ExoLang---
version 0.1
made by: Aurelius.
""")
        input("Press ENTER to continue.")
    
    
    else:
        print("Syntax Error.")
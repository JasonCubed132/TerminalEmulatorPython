#Teminal - Written in python.
import os,subprocess

def run(command):
    try:
        os.system(command)
    except KeyboardInterrupt:
        print("Cancelled.")
    except:
        print("WARNING: UNHANLDED EXCEPTION, PLEASE VIEW THE LOG AND TAKE APPROPRIATE ACTION.")
def log_output():
    try:
        print(open("tmp","r").read())
        os.remove("tmp")
    except FileNotFoundError:
        print("No log created.")
try:
    from PyDictionary import PyDictionary
except ImportError:
    print("PyDictionary not found.")
    answer = input("Do you wish to install?")
    if answer == "yes" or answer == "y" or answer == "Yes" or answer == "Y":
        print("Installing.")
        run("pip install pydictionary > tmp")
        print(open("tmp","r").read())
        os.remove("tmp")
python_mode = 0

        
while True:
    command = input("> ")
    if command == "exit":
        break
    if "./" in command:
        command = command.strip("./")
        run(command +" > tmp")
        log_output()
    if "python" == command:
        print("Please type in the commands you want to run and then type \"run\"")
        while True:
            python_cmd = input(">>> ")
            if python_cmd == "exit()":
                try:
                    os.remove("file")
                    os.remove("tmp")
                    break
                except:
                    break
            if python_cmd != "run":
                cmd_to_run = open("file","a")
                cmd_to_run.write(python_cmd+"\n")
                cmd_to_run.close()
                print(open("file","r").read())
            
            else:
                run("python file > tmp")
                log_output()
                os.remove("file")
    if "python" in command:
        run(command)
        log_output()
    if "pip" in command:
        run(command+" > tmp")
        log_output()
    if "background" in command:
        command = command[11:]
        #print("|"+command+"|")
        try:
            subprocess.Popen([command])
        except FileNotFoundError:
            print("Program not found, may not be in your path?")
            while True:
                path_view = input("Do you want to view you path? (Y/N)")
                if path_view == "Y":
                    path = os.getenv("PATH")
                    path = path.split(";")
                    print("Printing path variable.")
                    for line in path:
                        print(line)
                    break
                elif path_view == "N":
                    break
                else:
                    print("I do not understand, please try again.")


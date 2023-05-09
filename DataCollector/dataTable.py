import os, json, easymodule as em, time

jsonTableFile = "jsontest.json"

def printHeader():
	os.system("clear")
	print(em.Color.BLUE + em.figText("DataCollector", "small") + em.Color.END)

def getData():
    print("Welcome to this survey!")
    print("Let's start with a couple of questions.")
    name = input("What is you name?: ")

    with open(jsonTableFile) as jsonFile:
        data = json.load(jsonFile)
    
    checkName(name, data)
    data["Data Set"][name] = {}

    for i in range(len(data["QUESTIONS"])):
        answer = input(data["QUESTIONS"][i] + ": ")
        data["Data Set"][name]["Q" + str(i + 1)] = answer

    saveData(data)
    time.sleep(3)
    os.system("python3 dataTable.py")

def saveData(data):
    with open(jsonTableFile, "w") as jsonFile:
        json.dump(data, jsonFile, indent=4, sort_keys=True)
        print("\nThank you for your time!")

def checkName(name, data):
    for i in data["Data Set"]:
        if name == i:
            print("We're sorry, but that name is already in use.\n")
            input("Press [ENTER] to try again.")
            printHeader()
            getData()

if __name__ == "__main__":
    printHeader()
    getData()
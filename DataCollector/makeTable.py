import os, json, easymodule as em, time

def printHeader():
    os.system("clear")
    print(em.Color.BLUE + em.figText("DataCollector", "small") + em.Color.END)
    print(em.whiteSpace(19) + em.Color.RED + "[Table Maker]" + em.Color.END)

def Direction():
    print("Welcome to DataCollector [Table Maker]")
    name = input("DataTable Name?: ")

    try:
        with open(name + ".json", "w+"):
            pass
    except:
        print("Hmmm... Something went wrong.")
    
    print("JSON File Creation Successfull...")
    time.sleep(.4)
    getData()

def getData():
    printHeader()
    print("Now let's add some questions to our table.")

    try:
        question = input("Add a question: ")
        while True:
            addQuestion()
            question = input("Add a question: ")
    except:
        print("\nDataTable Creation Complete...")

if __name__ == "__main__":
    printHeader()
    Direction()
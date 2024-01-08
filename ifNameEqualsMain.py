# if __name__ == '__main__':

# why tho?
#1. module can be run as a standalone program
#2. module can be imported and used by other modules

#python interpreter sets __name__ variable to __main__ when running module as main program

def hello():
    print("Hello!")

if __name__ == '__main__':
    hello()

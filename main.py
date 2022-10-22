from home import homePage
from database import tables
#from testing_base import addNewUsers

tables()
def main():
  tables()#Confirms database initialized and empties ActiveUsers
  homePage()#Calls Home Page and starts the process
  return 0

if __name__ == "__main__":
  main()

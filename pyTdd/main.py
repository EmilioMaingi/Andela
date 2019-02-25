from app.ship import Ship
from app.mission import Mission

# run ship
draftt =  float(input('Whats the draft? '))
creww =  int(input('How many crew? '))
titanic = Ship(draftt, creww)
print (titanic.is_worth_it())

# run mission
# bulletNo = int(input('How many bullets do you have? '))
# mission = Mission(bulletNo)
# mission.goToWar()
# print (mission.getStatusToString())

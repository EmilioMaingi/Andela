import random
class Mission:
  def __init__(self, bullets):
    self.bullets = int(bullets)
    self.dragons = 50
  
  def __goToWar(self):
    reqBullets = self.dragons * 2
    if reqBullets > self.bullets:
      self.status = False
    else:
      self.status = True
  

  def getStatus(self):
    if self.status == True:
      return 'Mission won'
    else:
      return 'Mission failed'


  def getStatusToString(self):
    return '{}: There were {} dragons in the castle'.format(self.getStatus(), self.dragons)
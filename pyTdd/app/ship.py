class Ship:
  def __init__(self, draft, crew):
    self.draft = float(draft)
    self.crew = int(crew)

  def is_worth_it(self):
    shipDraft = self.draft - (self.crew * 1.5)
    print (shipDraft)
    if (shipDraft > 20):
      return 'Loot'
    return 'Do not loot'

# draftt =  float(input('Whats the draft? '))
# creww =  int(input('How many crew? '))

# titanic = Ship(draftt, creww)
# print (titanic.is_worth_it())

def truncate(n):
  multiplier = 10
  return int(n * multiplier) / multiplier

def getTotals(categories): 
  total = 0
  breakdown = []
  for category in categories:
    total += category.get_withdrawals() # Gets all the withdrawals for each category
    breakdown.append(category.get_withdrawals())
  rounded = [truncate(x/total) for x in breakdown]
  return rounded 

# Format the spend chart
def create_spend_chart(categories):
  res = "Percentage spent by category\n"
  i = 100
  totals = getTotals(categories)
  while i >= 0:
    cat_spaces = " "
    for total in totals:
      if total * 100 >= i:
        cat_spaces += "o  "
      else:
        cat_spaces += "   "
    res += str(i).rjust(3) + "|" + cat_spaces + ("\n")
    i -= 10

  dashes = "-" + "---" * len(categories)
  names = []
  x_axis = ""
  for category in categories:
    names.append(category.name)

  max_i = max(names, key = len)

  for x in range(len(max_i)):
    nameStr = "     "
    for name in names:
      if x >= len(name):
        nameStr += "   "
      else:
        nameStr += name[x] + "  "

    if (x != len(max_i) - 1):
      nameStr += "\n"

    x_axis += nameStr

  res += dashes.rjust(len(dashes) + 4) + "\n" + x_axis
  return res


class Category:

  # Initialise the object with an __init__ method (constructor)
  def __init__(self, name):
    self.name = name
    self.ledger = list()

  # String constructor
  def __str__(self):
    title = f"{self.name:*^30}\n" # Create line of stars surrounding the category name
    items = ""
    total = 0
    for item in self.ledger:
      items += f"{item['description'][0:23]:23}" + f"{item['amount']:>7.2f}" + "\n" # Format the description and amount to fit the space ([0:23] tqkes first 23 characters, :23 ensures it is right-aligned with a string of 23 characters, :>7.2f right-aligns the amount with a string if 7 characters formatted as a float-number with 2 decimal places)
      total += item['amount']
    return title + items + f"Total: {total}"

  # Define a deposit method
  def deposit(self, amount, description = ""):
    self.ledger.append({"amount": amount, "description": description}) # Appends this to the ledger

  # Define a withdrawal method
  def withdraw(self, amount, description = ""):
    if (self.check_funds(amount)): # Checks that there are sufficient funds
      self.ledger.append({"amount": -amount, "description" : description}) # Similar to deposit but instead a negative number will be appended to the ledger
      return True
    return False
  
  def get_balance(self):
    balance = 0
    for transaction in self.ledger:
      balance += transaction["amount"] # Returns amount of every item in the ledger
    return balance
  
  def transfer(self, amount, category): # Allows to withdraw from one category and deposit to another
    if (self.check_funds(amount)):
      self.withdraw(amount, f"Transfer to {category.name}")
      category.deposit(amount, f"Transfer from {self.name}")
      return True
    return False

  # Define a check_funds method used in the withdraw method
  def check_funds(self, amount):
    if (self.get_balance() >= amount):
      return True
    return False

  
  def get_withdrawals(self):
    total = 0
    for item in self.ledger:
      if item["amount"] < 0: # if the amount is negative it counts as a withdrawal
        total += item["amount"] # Adds up amount spent in each category
    return total
  

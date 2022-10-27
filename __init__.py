class Game:
  random = __import__('random')
  def __init__(self,guesses=5,a=None,b=None,number=None):
    self.guesses = guesses
    if number is None:
      self.number = self.random.randint(a,b)
    else:
      self.number = number
    
    self.start_game()
   
  def start_game(self):
     for i in range(self.guesses):
       guess = int(input("Enter a guess: "))

       if guess > self.number:
         print("Your number is too high.")
       if guess == self.number:
         print(f"You won in just {i+1} guess(es)!")
         break
       if guess < self.number:
         print("You number is too low.")
     else:
       print("Sorry, you lost.")
        
  def reset(self,guesses=5,a=None,b=None,number=None):
    self.guesses = gusses
    if number is None:
      self.number = random.randint(a,b)
    else:
      self.number = number

#Define the base class player
class playe9r:
  def play(self):
    prinbt("The player is playing cricket.")
#Define the derived class Batsman
class Batsman(player):
  def play(self):
    print("The batsman is batting.")
#Define the derived class Bowler
class Bowler:
  def play(self):
    print("The bowler is bowling.")
#Create objects of Batsman and Bowler classes 
batsman = Batsman()
bowler = Bowler ()
#call the play() method for each object
batsman.play()
bowler .play()
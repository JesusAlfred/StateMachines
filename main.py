import random
from time import sleep 

class Estate():
  def __init__(self, id, rules):
    self.id = id
    self.rules = rules
  def netState(self, val):
    print("In state", self.id, "\tinput", val)
    nextState = -1
    for s, f in self.rules.items():
      ret = eval(f)
      if ret == True:
        nextState = s
        break
    return nextState

def main():
  E1 = Estate(1, {
    2: "val == 1"
  })
  E2 = Estate(2, {
    1: "val == 1"
  })

  initState = 1
  state = initState
  while True:
    val = random.randint(0, 5)
    switch = {
      1: E1,
      2: E2
    }
    fun = switch.get(state)
    state = fun.netState(val)
    sleep(1)
  pass

if __name__ == "__main__":
  main()
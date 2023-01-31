import sys

D = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

class State():
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

def main(c):
  E1 = State(1, {
    2: "val in D"
  })
  E2 = State(2, {
    2: "val in D",
    3: "val == '.'"
  })
  E3 = State(3, {
    4: "val in D"
  })
  E4 = State(4, {
    4: "val in D"
  })

  initState = 1
  state = initState
  cadena = c
  finalState = [4, 2]
  for i in cadena:
    val = i
    switch = {
      1: E1,
      2: E2,
      3: E3,
      4: E4
    }
    fun = switch.get(state)
    state = fun.netState(val)
    if state == -1:
      indexError = i
      break
  pass
  print("Input " + cadena)
  if state in finalState:
    print("Correct")
  else:
    print("Incorrect in '" + indexError + "'")

if __name__ == "__main__":
  try:
    main(sys.argv[1])
  except Exception as e:
    print(e)
    print("Send params\nEx.\n>python main.py 1000.1000")
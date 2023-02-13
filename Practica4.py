import sys
import string

D = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
L = list(string.ascii_letters)

class State():
  def __init__(self, id, rules):
    self.id = id
    self.rules = rules
  def nextState(self, val):
    val = str(val)
    #print("In state", self.id, "\tinput", val)
    nextState = -1
    for s, f in self.rules.items():
      ret = eval(f)
      if ret == True:
        nextState = s
        break
    return nextState

def id(c):
  E1 = State(1, {
    2: "val in L or val == '_'"
  })
  E2 = State(2, {
    2: "val in L or val == '_' or val in D"
  })
  initState = 1
  state = initState
  cadena = c
  finalState = [1, 2]
  for i in cadena:
    val = i
    switch = {
      1: E1,
      2: E2
    }
    fun = switch.get(state)
    state = fun.nextState(val)
    if state == -1:
      indexError = i
      break
  print("Input " + cadena)
  if state in finalState:
    print("Correct")
    return 1
  else:
    print("Incorrect in '" + indexError + "'")
    return -1

def declaration(c):
  E1 = State(1, {
    2: "val == 'l'"
  })
  E2 = State(2, {
    3: "val == 'e'"
  })
  E3 = State(3, {
    4: "val == 't'"
  })
  E4 = State(4, {
    4: "True"
  })
  initState = 1
  state = initState
  cadena = c
  finalState = [4]
  for i in cadena:
    val = i
    switch = {
      1: E1,
      2: E2,
      3: E3
    }
    fun = switch.get(state)
    state = fun.nextState(val)
    if state == -1:
      indexError = i
      break
  print("Input " + cadena)
  if state in finalState:
    print("Correct")
    return 1
  else:
    print("Incorrect in '" + indexError + "'")
    return -1

def end(c):
  E1 = State(1, {
    2: "val == ';'"
  })
  E2 = State(2, {
    2: "True"
  })
  initState = 1
  state = initState
  cadena = c
  finalState = [2]
  for i in cadena:
    val = i
    switch = {
      1: E1,
      2: E2
    }
    fun = switch.get(state)
    state = fun.nextState(val)
    if state == -1:
      indexError = i
      break
  print("Input " + cadena)
  if state in finalState:
    print("Correct")
    return 1
  else:
    print("Incorrect in '" + indexError + "'")
    return -1

def main(e):
  partes = e.split(" ")
  let = partes[0]
  idp = partes[1][:-1]
  endp = partes[1][-1]
  print(let)
  print(idp)
  print(endp)
  if declaration(let) == -1: return
  if id(idp) == -1: return
  if end(endp) == -1: return

  pass


if __name__ == "__main__":
  main(sys.argv[1])
  #try:
  #  main(sys.argv[1])
  #except Exception as e:
  #  print(e)
  #  print("Send params\nEx.\n>python main.py 1000.1000")
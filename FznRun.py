import FznBase

print('Start executing the game script.')

actions = []

actions.append({"key":"w","delay":3,"hold":True,"repeat":1})
actions.append({"key":"enter","delay":2,"repeat":5})

FznBase.FznStart(actions)

print('Script execution completes.')
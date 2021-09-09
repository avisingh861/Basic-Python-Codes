carNames=[]
while True:
    print(' Enter name of car ' + str(len(carNames) + 1) + ' (Leave blank to stop)')
    name=input()
    if name == 'nano' or name=='':
        break
    carNames = carNames + [name]
print('Names of the cars are as follows')
for name in carNames:
    print(name)

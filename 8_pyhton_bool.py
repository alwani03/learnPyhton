print(10 > 9)
print(10 == 9)
print(10 < 9)

print('------------------------1')

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

print('------------------------2')

print(bool("Hello"))
print(bool(15))

print('------------------------3')

print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))

print('------------------------4')

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

print('------------------------5')

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

print('------------------------6')

def myFunction() :
  return True

print(myFunction())

print('------------------------7')







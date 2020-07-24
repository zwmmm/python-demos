# 面向对象

class Person(object):
  __slots__ = ('_name', '_age')

  def __init__(self, name, age):
    self._name = name
    self._age = age

  @property
  def name(self):
    return self._name

  @property
  def age(self):
    return self._age

  @age.setter
  def age(self, age):
    self._age = age

if __name__ == "__main__":
  person = Person('王武', 20)
  print(person.name)
  person.age = 100
  print(person.age)





animals_dict = {
  'snake': 0,
  'worm': 0,
  'monkey': 2, 
  'parrot': 2, 
  'ostrich': 2,
  'lion': 4, 
  'deer': 4, 
  'elephant': 4, 
  'horse': 4, 
  'dog': 4, 
  'cat': 4,
  'spider': 6,
  'ant': 6,
  'centipede': 10
}

def four_leg_animals(animals): 
  count = 0

  for animal in animals:
    if animal in animals_dict:
      if animals_dict[animal] == 4:
        count += 1

  return count

animals = [
  ([], 0),
  (['lion', 'monkey', 'deer', 'snake', 'elephant'], 3),
  (['frog', 'horse', 'spider', 'ant'], 1),
  (['lion', 'deer', 'elephant', 'horse', 'dog', 'cat'], 6)
]

if __name__=="__main__":
  for animal in animals:
    # print(four_leg_animals(animal[0]))
    four_leg_animals(animal[0])
    print('Pass' if four_leg_animals(animal[0])==animal[1] else 'Fail')
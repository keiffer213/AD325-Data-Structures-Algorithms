
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


def num_leg_animal(animal_input, num_legs):
  count = 0

  for anim in animal_input:
    if anim in animals_dict:
      if animals_dict[anim] == num_legs:
        count += 1

  return count



animals = [
  ([], 0),
  (['frog', 'horse', 'spider', 'ant'], 1),
  (['lion', 'monkey', 'deer', 'snake', 'elephant'], 3),
  (['lion', 'horse', 'deer', 'cat', 'dog', 'elephant'], 6)
]

if __name__ == "__main__":
  for animal in animals:
    print(num_leg_animal(animal[0], 4))
    print('Pass' if num_leg_animal(animal[0], 4)==animal[1] else 'Fail')
    assert num_leg_animal(animal[0], 4)==animal[1]



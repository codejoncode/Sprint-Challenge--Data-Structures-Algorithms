Add your answers to the Algorithms exercises here.
A = O(n)
B = about O(n^3) probably a little more. The last for loop will account for some but is constant it will always start off at n+ 3 and stop at n-10 so its not quite n but will perform at more than O(1) 
C = O(1)

Exercise II 

#n = __n__   or number of floors. 
def egg_test(n,broken_egg): 
  mid_point = n//2 
  print(mid_point)
  print("start")
  #cut it in half so so if n is 100 we will get 50

  while True:
    if mid_point > broken_egg: #meaning point egg breaks if dropped
      mid_point -= 1
      print(mid_point)
    elif mid_point < broken_egg:
      mid_point += 1
      print(mid_point)
    if mid_point == broken_egg :
      print(mid_point)
      break 



I would do something like this becasue i think it might be a little faster depending on the number of floors 
def egg_test(n, broken_egg, in_range = 0):
  #n = __n__   or number of floors. 
  
  floors = [x for x in range(in_range,n +1)]

  mid_point = len(floors) // 2
  
 
  if floors[mid_point] < broken_egg:
      # the mid_point - 1 will become my new n
     
      print (mid_point + 1)
      egg_test(n, broken_egg,  floors[mid_point+1],)
  elif floors[mid_point] > broken_egg:
      #mid_point + 1 becomes the range 
      egg_test(floors[mid_point - 1], broken_egg)
  elif floors[mid_point] == broken_egg:
      return "Egg Broken at {}".format(floors[mid_point])


egg_test(100, 93)
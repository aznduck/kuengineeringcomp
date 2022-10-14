import time
from colors import red, blue, green, yellow, magenta

print(blue('Hello There! You are now stuck in a maze at the top left corner.\n'))

print(yellow('Your position is denoted by the "*" symbol and the area visible is denoted by a "+". The units denoted by the symbols - , _ , ^ , or | indicate positions that are unavailable for passage, blocked by a rock or other obstacles.'))

print(magenta('\nBe careful as you explore because, after each new move, the previous path disappears! Try to make it to the finish point denoted by F in as less moves as possible. Use the w(up), a(left), s(down), d(right) tabs to move.\n'))

level = str(input(red("Type which level you would like to play.\n\n")))

print(green("\nYou have selected level "+level+". Click the game.txt tab on the left to view your position and potential moves.\n"))

map = list()
fhand = open(level + ".txt", "r")
for line in fhand:
  row = list()
  for char in line:
    if char == '1':
      row.append(True)
    if char == '0':
      row.append(False)
  map.append(row)
fhand.close()
  

def illuminate(x,y):
  fhand = open('game.txt', 'w')
  visible = [(x,y)]
  xpos = x
  ypos  = y
  while not map[ypos][xpos+1]:
    visible.append((xpos+1,ypos))
    xpos += 1
  xpos = x
  while not map[ypos][xpos-1]:
    visible.append((xpos-1,ypos))
    xpos -= 1
  xpos = x
  while not map[ypos+1][xpos]:
    visible.append((xpos,ypos+1))
    ypos += 1
  ypos = y
  while not map[ypos-1][xpos]:
    visible.append((xpos,ypos-1))
    ypos -= 1
  if (x,y) == (len(map)-2,len(map)-2):
    fhand.write('Congratulations! You made it out!\nIt only took you ' + str(moves) + ' moves.\n\nWould you like to see a replay? (y/n)')
  else :
    for i in range(len(map)):
      for j in range(len(map[i])):
        if i == len(map)-2 and j == len(map)-2:
          fhand.write('F')
        elif i == 0:
          fhand.write('_')
        elif i == len(map)-1:
          fhand.write('^')
        elif j == 0 or j == len(map)-1:
          fhand.write('|')
        elif (i,j) == (y,x):
          fhand.write('*')
        elif (j,i) in visible:
          fhand.write('+')
        else :
          fhand.write('-')
      fhand.write('\n')
  fhand.close()

x,y = 1,1
moves = 0
allMoves = list()
while True:
  illuminate(x,y)
  if (x,y) == (len(map)-2,len(map)-2):
    break
  allMoves.append((x,y))
  move = input()
  moves += 1
  if move == 'w':
    if not map[y-1][x]:
      y -= 1
    else :
      print('Can\'t go there')
  if move == 'a':
    if not map[y][x-1]:
      x -= 1
    else :
      print('Can\'t go there')
  if move == 's':
    if not map[y+1][x]:
      y += 1
    else :
      print('Can\'t go there')
  if move == 'd':
    if not map[y][x+1]:
      x += 1
    else :
      print('Can\'t go there')

replay = input()
if replay == 'y':
  for i in range(len(allMoves)):
    time.sleep(0.5)
    illuminate(allMoves[i][0],allMoves[i][1])
fhand = open('game.txt', 'a')
fhand.write("\nThanks for playing!")
fhand.close()
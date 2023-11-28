picture=[
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
    ]

def tree():
  for image in picture:
      for pixel in image:
          if pixel==1:
              print('*', end='')
          else:
              print(' ', end='')
      print(' ')

tree()
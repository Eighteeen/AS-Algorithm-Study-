T = int(input())

for i in range(T):
  candies, boxes = map(int, input().split())

  box_sizes = []
  for j in range(boxes):
    row_size, col_size = map(int, input().split())
    box_size = row_size * col_size
    box_sizes.append(box_size)
  
  box_sizes.sort(reverse=True)

  boxed_candies = 0
## for문 돌리면 used_boxes변수 없어도 기능해요!
  used_boxes = 0
  for box_size in box_sizes:
    boxed_candies += box_size
    used_boxes += 1
    if boxed_candies >= candies:
      break;
  
  print(used_boxes)

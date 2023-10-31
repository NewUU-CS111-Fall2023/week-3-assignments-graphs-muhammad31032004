def can_reach_treasure(maze, n, m, j):
  queue = []
  start = (0, 0, 0)
  queue.append(start)

  while queue:
    x, y, spikes_avoided = queue.pop(0)

    if maze[x][y] == 'x':
      return True

    if maze[x][y] == '#' or spikes_avoided > j:
      continue

    if maze[x][y] == '.':
      continue

    if maze[x][y] == 's':
      spikes_avoided+=1
      if (spikes_avoided>=j):
        continue

    if 0 <= x + 1 < n and maze[x + 1][y] != '#':
      queue.append((x + 1, y, spikes_avoided))

    if 0 <= x - 1 < n and maze[x - 1][y] != '#':
      queue.append((x - 1, y, spikes_avoided))

    if 0 <= y + 1 < m and maze[x][y + 1] != '#':
      queue.append((x, y + 1, spikes_avoided))

    if 0 <= y - 1 < m and maze[x][y - 1] != '#':
      queue.append((x, y - 1, spikes_avoided + 1))

  return False


def main():

  n, m, j = map(int, input().split())
  maze = []
  for i in range(n):
    maze.append(list(input()))

  if can_reach_treasure(maze, n, m, j):
    print('SUCCESS')
  else:
    print('IMPOSSIBLE')


if __name__ == '__main__':
  main()

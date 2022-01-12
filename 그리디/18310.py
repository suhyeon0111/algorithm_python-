'''
안테나 문제
일직선 상의 마을에 여러 채의 집이 위치해 있다. 
이중에서 특정 위치의 집에 특별히 한 개의 안테나를 설치하기로 결정했다.
효율성을 위해 안테나로부터 모든 집까지의 거리의 총 합이 최소가 되도록 설치하려고 한다. 이 때 안테나는 집이 위치한 곳에만 설치할 수 있고,
 논리적으로 동일한 위치에 여러 개의 집이 존재하는 것이 가능하다.
'''

from sys import stdin

n = int(stdin.readline())
home = list(map(int, stdin.readline().split()))

home.sort()

k = (n - 1) // 2  
print(home[k])
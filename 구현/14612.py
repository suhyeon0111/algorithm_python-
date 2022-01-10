'''
인하대학교 축제를 맞이하여 알고리즘 동아리 CTP에서는 식당을 열기로 하였다. 요리는 세진이가 하게 되었고, 주문을 받는 것은 한솔이가 하게 되었다. 식당의 음식이 너무 맛있어서 주문은 끊임없이 계속되었고, 한솔이는 밀려오는 주문에 주문 순서를 혼동하게 되었다.

이러한 이유로 한솔이는 주문 받을 때 테이블의 번호와 주문한 시간을 포스트잇에 적어서 세진이에게 넘겨주었지만, 요리를 하느라 바쁜 세진이가 주문들의 순서를 파악하는 것은 쉽지 않았다. 이때, 지나가던 토쟁이가 포스트잇들을 시간 순서에 맞게 정렬해서 보여주며, 요리가 완성된 테이블의 포스트잇을 제거하는 프로그램을 만들어주기로 하였지만 시험기간이 얼마 남지 않아 힘들다. 만들 프로그램의 명령어와 수행 기능은 다음과 같다.

order (테이블 번호 n) (주문시간 t): 주문 시간 t에 테이블 n에서 주문 들어옴 (주문이 들어오면 갖고 있는 포스트잇들의 맨 뒤에 새 포스트잇을 추가)
sort: 주문 시간이 빠른 순서대로 정렬
complete n: n번 테이블의 요리 완성. (요리를 완성하는 시점에 해당 테이블에 두 개 이상의 주문이 밀려 있거나 주문이 없는 경우는 존재하지 않음)
코딩을 잘하는 여러분이 토쟁이를 도와 김식당을 부흥시켜줄 프로그램을 만들어 보자.
'''

from sys import stdin

n, m = map(int, stdin.readline().split())  # n명령 개수, m 테이블 수 

postit = {}  # 결과 저장할 dictionary

for i in range(n):
    command = stdin.readline().rstrip().split()  # 주문입력

    # order
    if command[0] == "order":
        postit[int(command[1])] = int(command[2])  # dictionary 형태로 테이블 번호를 key로 두고, 시간은 value로 저장

    # sort 
    elif command[0] == "sort":
        postit = dict(sorted(postit.items(), key=lambda x : (x[1], x[0])))  # 시간대로 정렬

    # complete
    elif command[0] == "complete":
        del postit[int(command[1])]  # 완료된 테이블 삭제

    if len(postit) == 0:
        print('slepp')
        continue


    for table in postit.keys():
        print(table, end=' ')
    print("")


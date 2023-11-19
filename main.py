import random

# 선택정렬
def selection_sort(A):
    n = len(A)
    for i in range(n - 1):
        least = i
        for j in range(i + 1, n): # 최소값 탐색
            if A[j] < A[least]:
                least = j
        A[i], A[least] = A[least], A[i]


# 삽입정렬
def insertion_sort(A):
    n = len(A)
    for i in range(1, n):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key


# 버블정렬
def bubble_sort(A):
    n = len(A)
    for i in range(n - 1, 0 ,-1):
        bChanged = False
        for j in range(i):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
                bChanged = True
        if not bChanged : break


# 퀵정렬
def quick_sort(A, left, right):
    if left < right :
        i = left + 1
        j = right
        pivot = A[left]
        while i <= j :
            while i <= right and A[i] <= pivot : i+= 1
            while j >= left and A[j] > pivot: j -= 1
            if i < j : A[i], A[j] = A[j], A[i];
        A[left], A[j], = A[j], A[left];
        quick_sort(A, left, j-1)
        quick_sort(A, j+1, right)


# 합병정렬
def merge(A, left, mid, right):
    global sorted
    i = left # 왼쪽 리스트의 첫 번째 인덱스
    j = mid + 1 # 오른쪽 리스트의 첫 번째 인덱스
    k = left # 정렬된 리스트의 첫 번째 인덱스

    # 분할된 리스트의 합병
    while i <= mid and j <= right :
        if A[i] <= A[j]:
            sorted[k] = A[i]; i, k = i+1, k+1
        else:
            sorted[k] = A[j]; j, k = j+1, k+1

    # 남아있는 리스트의 복사
    if i > mid :
        sorted[k : k + right - j + 1] = A[j : right + 1]
    else:
        sorted[k : k + mid - i + 1] = A[i : mid + 1]

    # 임시(sorted[]) 리스트를 원래(A[]) 리스트로 복사
    A[left : right + 1] = sorted[left : right + 1]

def merge_sort(A, left, right):
    if left < right :
        mid = (left + right) // 2 # 분할
        merge_sort(A, left, mid) # 분할
        merge_sort(A, mid+1, right) # 분할
        merge(A, left, mid, right) # 합병

# 힙정렬 ver1
def heappush(heap, n):
    heap.append(n)
    i = len(heap) -1 # n이 삽입된 위치
    while i != 1 and n > heap[i // 2]:
        heap[i] = heap[i // 2]
        i //= 2
    heap[i] = n

def heappop(heap):
    size = len(heap) - 1
    if size == 0 :
        return None # 공백트리
    p = 1; i = 2 # p는 부모인덱스, i는 자식인덱스
    root = heap[1] # 삭제할 노드
    last = heap[size] # 마지막 노드
    while i <= size:
        if i < size and heap[i] < heap[i+1]:
            i += 1 # 자식 중 더 큰값 선택
        if last >= heap[i] : break
        heap[p] = heap[i] # 자식을 부모위치로
        p = i # 부모위치가 자식위치로
        i *= 2 # 자식위치 이동
    heap[p] = last
    heap.pop()
    return root

def heap_sort(data):
    heap = [0]
    #모든 데이터를 최대힙에 삽입
    for e in data:
        heappush(heap, e)
    # 모든 데이터를 힙에서 꺼내 역순으로 저장
    for i in range(1, len(data) + 1):
        data[-i] = heappop(heap)

# 힙정렬 ver2
def heapify(arr, n, i):
    # n = arr의 길이, i = 루트노드 인덱스
    largest = i
    l = 2*i # 왼쪽 자식 인덱스
    r = 2*i + 1 # 오른쪽 자식 인덱스

    # 루트(i)와 두 자식 중 가장 큰 요소 인덱스 구하기
    if l <= n and arr[i] < arr[l]:
        largest = l
    if r <= n and arr[largest] < arr[r]:
        largest = r

    # 자식노드 처리하기
    if largest != i :
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr) - 1

    # 앞쪽요소 최대힙화
    for i in range(n//2, 0 , -1):
        heapify(arr, n, i)

    # 루트와 마지막요소 교환 후 다시 다운 힙
    for i in range(n-1, 0, -1):
        arr[i+1], arr[1] = arr[1], arr[i+1]
        heapify(arr, i ,1)

# 메뉴
def print_menu():
    print("\n*** 여러가지 정렬 프로그램 구현 ***")
    print("*** ***")
    print("*** 1. 선택(selection) 정렬 ***")
    print("*** 2. 삽입(insertion) 정렬 ***")
    print("*** 3. 버블(bubble) 정렬 ***")
    print("*** 4. 퀵(quick) 정렬 ***")
    print("*** 5. 합병(merge) 정렬 ***")
    print("*** 6. 힙(heap) 정렬 ***")
    print("*** 7. 종료(quit) ***")
    print("***********************************", end=" ")

# 메인 함수
def main():
    original_list = [random.randint(0, 100) for _ in range(25)]
    print_menu()

    while True:
        num = int(input("번호 입력: "))

        if num == 1:
            print("\n<선택 정렬>")
            print("정렬 전:", original_list)
            selection_sort_result = original_list.copy()
            selection_sort(selection_sort_result)
            print("정렬 후:", selection_sort_result)

        elif num == 2:
            print("\n<삽입 정렬>")
            print("정렬 전:", original_list)
            insertion_sort_result = original_list.copy()
            insertion_sort(insertion_sort_result)
            print("정렬 후:", insertion_sort_result)

        elif num == 3:
            print("\n<버블 정렬>")
            print("정렬 전:", original_list)
            bubble_sort_result = original_list.copy()
            bubble_sort(bubble_sort_result)
            print("정렬 후:", bubble_sort_result)

        elif num == 4:
            print("\n<퀵 정렬>")
            print("정렬 전:", original_list)
            quick_sort_result = original_list.copy()
            quick_sort(quick_sort_result)
            print("정렬 후:", quick_sort_result)

        elif num == 5:
            print("\n<합병 정렬>")
            print("정렬 전:", original_list)
            merge_sort_result = original_list.copy()
            merge_sort(merge_sort_result)
            print("정렬 후:", merge_sort_result)

        elif num == 6:
            print("<힙 정렬(1)>")
            print("정렬 전:", original_list)
            heap_sort_result = original_list.copy()
            heap_sort(heap_sort_result)
            print("정렬 후:", heap_sort_result)
            print("")
            print("<힙 정렬(2)>")
            print("정렬 전:", original_list)
            heapSort_result = original_list.copy()
            heapSort(heapSort_result)
            print("정렬 후 : ", heapSort_result)

        elif num == 7:
            exit("\n<종료>")

        else:
            print("\n<번호 오류>")
        print("")

main()
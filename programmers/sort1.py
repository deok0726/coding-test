## Best Solution ##
# def solution(array, commands):
#     return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

def solution(array, commands):
    answer = []
    temp = []
    for i, j, k in commands:
        temp = array[i-1: j]
        temp.sort()
        answer.append(temp[k-1])
    return answer

print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))
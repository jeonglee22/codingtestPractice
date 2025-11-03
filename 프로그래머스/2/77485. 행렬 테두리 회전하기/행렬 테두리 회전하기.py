def rotation(numlist, query):
    top = numlist[query[0]-1][query[1]-1:query[3]-1]
    right = [numlist[i][query[3]-1] for i in range(query[0]-1, query[2]-1)]
    bottom = numlist[query[2]-1][query[1]:query[3]]
    left = [numlist[i][query[1]-1] for i in range(query[0], query[2])]
    
    numlist[query[0]-1][query[1]:query[3]] = top
    for i in range(query[0], query[2]):
        numlist[i][query[3]-1] = right[i - query[0]]

    numlist[query[2]-1][query[1]-1:query[3]-1] = bottom
    for i in range(query[0]-1, query[2]-1):
        numlist[i][query[1]-1] = left[i - (query[0] - 1)]
    
    return min(min(top), min(left), min(right), min(bottom))

def solution(rows, columns, queries):
    answer = []
    
    numlist = [[j * columns + (i+1) for i in range(columns) ] for j in range(rows)]
    for query in queries:
        answer.append(rotation(numlist, query))
    
    return answer
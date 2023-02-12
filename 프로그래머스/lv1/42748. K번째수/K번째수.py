def solution(array, commands):
    result = []
    for i in range(len(commands)):
        result.append(sorted(array[commands[i][0]-1:commands[i][1]])[commands[i][2]-1])
    return result
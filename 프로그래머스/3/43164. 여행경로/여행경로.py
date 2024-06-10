def solution(tickets):
    answer = []
    visited = [False] * len(tickets)
    tickets.sort(key = lambda x : x[1])
    
    def dfs(city, path):
        if len(path) == len(tickets) + 1:
            answer.append(path)
            return

        for idx, ticket in enumerate(tickets):
            if ticket[0] == city and not visited[idx]:
                visited[idx] = True
                dfs(ticket[1], path + [ticket[1]])
                visited[idx] = False
    
    dfs("ICN", ["ICN"])
    return answer[0]
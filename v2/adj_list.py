class Solution:
    def dfs(self, adj_list: map[int, list[int]]) -> None:
        if not adj_list:
            return
        
        visited: set = set()

        for node in adj_list:
            if node not in visited:
                self.dfs_helper(node=node, adj_list=adj_list, visited=visited)

    def dfs_helper(self, node: int, adj_list: map[int, list[int]], visited: set) -> None:
        if node in visited:
            return

        visited.add(node) 
        for child in adj_list[node]:
            self.dfs_helper(node=child, adj_list=adj_list, visited=visited)
        return 

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col = collections.defaultdict(set)
        raw = collections.defaultdict(set)
        sqar = collections.defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":    # means it is empty
                    continue
                if (board[i][j] in col[i] or board[i][j] in raw[j] or 
                    board[i][j] in sqar[(i // 3 , j // 3)]): 
                    return False        # return false if matches
                
                col[i].add(board[i][j])
                raw[j].add(board[i][j])
                sqar[(i // 3 , j // 3)].add(board[i][j])

        return True
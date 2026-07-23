class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col = defaultdict(set)
        row = defaultdict(set)
        sq = defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in col[i] or board[i][j] in row[j] or board[i][j] in sq[i//3, j//3]:
                        return False
                    col[i].add(board[i][j])
                    row[j].add(board[i][j])
                    sq[i//3, j//3].add(board[i][j])
        return True
























        # col = defaultdict(set)
        # row = defaultdict(set)
        # squares = defaultdict(set)
        # for i in range(9):
        #     for j in range(9):
        #         if board[i][j] == '.':
        #             continue
        #         if (board[i][j] in row[i] or board[i][j] in col[j] or board[i][j] in squares[(i//3 ,j//3)]):
        #             return False
        #         col[j].add(board[i][j])
        #         row[i].add(board[i][j])
        #         squares[(i//3,j//3)].add(board[i][j])
        # return True
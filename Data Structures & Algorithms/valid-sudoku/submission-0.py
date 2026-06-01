class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        iObj = {}
        jObj = {}
        fObj = {
            '33': [], '36': [], '39': [],
            '63': [], '66': [], '69': [],
            '93': [], '96': [], '99': []
        }
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    if i not in iObj:
                        iObj[i] = []
                    if j not in jObj:
                        jObj[j] = []
                    if board[i][j] in iObj[i]:
                        return False
                    else:
                        iObj[i].append(board[i][j])
                    if board[i][j] in jObj[j]:
                        return False
                    else:
                        jObj[j].append(board[i][j])
                    if i < 3 and j < 3:
                        if board[i][j] in fObj['33']:
                            return False
                        else:
                            fObj['33'].append(board[i][j])
                    elif i < 3 and j < 6:
                        if board[i][j] in fObj['36']:
                            return False
                        else:
                            fObj['36'].append(board[i][j])
                    elif i < 3 and j < 9:
                        if board[i][j] in fObj['39']:
                            return False
                        else:
                            fObj['39'].append(board[i][j])
                    elif i < 6 and j < 3:
                        if board[i][j] in fObj['63']:
                            return False
                        else:
                            fObj['63'].append(board[i][j])
                    elif i < 6 and j < 6:
                        if board[i][j] in fObj['66']:
                            return False
                        else:
                            fObj['66'].append(board[i][j])
                    elif i < 6 and j < 9:
                        if board[i][j] in fObj['69']:
                            return False
                        else:
                            fObj['69'].append(board[i][j])
                    elif i < 9 and j < 3:
                        if board[i][j] in fObj['93']:
                            return False
                        else:
                            fObj['93'].append(board[i][j])
                    elif i < 9 and j < 6:
                        if board[i][j] in fObj['96']:
                            return False
                        else:
                            fObj['96'].append(board[i][j])
                    elif i < 9 and j < 9:
                        if board[i][j] in fObj['99']:
                            return False
                        else:
                            fObj['99'].append(board[i][j])
        return True

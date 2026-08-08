from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols = len(board), len(board[0])
        seen_rows = defaultdict(set)
        seen_cols = defaultdict(set)
        seen_sqrs = defaultdict(set)

        for r in range(rows):
            for c in range(cols):
                value = board[r][c]
                if (value != ".") and ((value in seen_rows[r])
                 or (value in seen_cols[c]) or 
                 (value in seen_sqrs[(r//3, c//3)])):
                    return False
                else:
                    seen_rows[r].add(value)
                    seen_cols[c].add(value)
                    seen_sqrs[(r//3, c//3)].add(value)

        return True
       
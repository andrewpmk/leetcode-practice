# Time to get working solution 16 min 15 sec

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        if len(board) != 9:
            raise ValueError
        for row in range(len(board)):
            if len(board[row]) != 9:
                raise ValueError
        # Check rows
        for row in range(0,9):
            s = set()
            for col in range(0,9):
                # invalid value
                if ord(board[row][col]) < ord("1") and ord(board[row][col]) > ord("9") and board[row][col] != "":
                    return False
                # duplicate
                if board[row][col] in s:
                    return False
                if board[row][col] != ".":
                    s.add(board[row][col])
        # Check columns
        for col in range(0,9):
            s = set()
            for row in range(0,9):
                # invalid value
                if ord(board[row][col]) < ord("1") and ord(board[row][col]) > ord("9") and board[row][col] != "":
                    return False
                # duplicate
                if board[row][col] in s:
                    return False
                if board[row][col] != ".":
                    s.add(board[row][col])
        # Check 3x3 boxes
        for x in (0,3,6):
            for y in (0,3,6):
                # Check everything in each box
                s = set()
                for row in range(x,x+3):
                    for col in range(y,y+3):
                        # invalid value
                        if ord(board[row][col]) < ord("1") and ord(board[row][col]) > ord("9") and board[row][col] != "":
                            return False
                        # duplicate
                        if board[row][col] in s:
                            return False
                        if board[row][col] != ".":
                            s.add(board[row][col])
        return True


if __name__ == "__main__":
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."]
        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    solution = Solution()
    print(solution.isValidSudoku(board))
    board = [["8", "3", ".", ".", "7", ".", ".", ".", "."]
        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    print(solution.isValidSudoku(board))

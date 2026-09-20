class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for row in range(9):
            for column in range(9):
                number = board[row][column]

                if number == '.':
                    continue

                #chekc row
                if number in rows[row]:
                    return False
                rows[row].add(number)

                #check cols
                if number in cols[column]:
                    return False
                cols[column].add(number)

                # check square
                squre_key = (row // 3, column // 3)
                if number in squares[squre_key]:
                    return False
                squares[squre_key].add(number)

        return True
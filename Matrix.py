class Matrix:
    def __init__(self, rows, cols):
        self.matrix = []
        self.rows = rows
        self.cols = cols

    def generate_matrix(self):
        num = 1
        if self.rows == 0 and self.cols == 0:
            return
        for i in range(self.rows):
            self.matrix.append([])
            for j in range(self.cols):
                self.matrix[i].append(num)
                num += 1

    def print(self):
        for row in self.matrix:
            print("\t".join(map(str, row)))
        print("-" * 20)

    def find_coordinate(self, value):
        for r, row in enumerate(self.matrix):
            for c, cell in enumerate(row):
                if cell == value:
                    return r, c
        return None

    def get(self, row, col):
        return self.matrix[row][col]
    
    def set(self, row, col, value):
        self.matrix[row][col] = value

    def print_row(self, row_num):
        for c in self.matrix[row_num]:
            print(c)

    def alter(self, row_num, col_num, new_value):
        self.matrix[row_num][col_num] = new_value



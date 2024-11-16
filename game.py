from Matrix import Matrix
import random


class GoldRush(Matrix):
    EMPTY_CELL = "."
    COIN = "$$"
    WALL = "||"
    PLAYER1 = "player1"
    PLAYER2 = "player2"
    WINNING_SCORE = 100
    MIN_COINS = 10

    def __init__(self, rows, cols):
        super().__init__(rows, cols)
        self.score1 = 0
        self.score2 = 0
        self.winner = None
        self.total_coins = 0

    def load_board(self):
        if self.rows == 0 and self.cols == 0:
            self.matrix = []
            return

        self.matrix = []
        elements = [self.COIN, self.EMPTY_CELL, self.WALL]
        total_coins = 0

        for i in range(self.rows):
            self.matrix.append([])
            for j in range(self.cols):
                if i % 2 != 0:
                    rand_index = random.randint(0, 1)
                    rand_element = elements[rand_index]
                    self.matrix[i].append(rand_element)
                    if rand_element == self.COIN:
                        total_coins += 1
                else:
                    wall_index = 2
                    wall = elements[wall_index]
                    self.matrix[i].append(wall)

            rand = random.randint(1, 2)
            for k in range(1, self.cols, rand):
                rand += 1
                rand_index = random.randint(0, 1)
                rand_element = elements[rand_index]
                self.matrix[i][k] = rand_element
                if rand_element == self.COIN:
                    total_coins += 1

        self.matrix[0][0] = self.PLAYER1
        self.matrix[self.rows - 1][self.cols - 1] = self.PLAYER2
        self.total_coins = total_coins

        if total_coins < self.MIN_COINS:
            return self.load_board()
        else:
            return self.matrix

    def _check_win(self, player):
        player_num = player[-1]
        score = getattr(self, f"score{player_num}")
        if score >= self.WINNING_SCORE:
            self.win = player
            return self.win

    def _check_other_player(self, player):
        return self.PLAYER2 if player == self.PLAYER1 else self.PLAYER1
        

    def _move(self, curr_row, curr_col, player, delta_row, delta_col):
        other_player = self._check_other_player(player)
        new_row, new_col = curr_row + delta_row, curr_col + delta_col

        if not (0 <= new_row < self.rows and 0 <= new_col < self.cols):
            return

        if self.matrix[new_row][new_col] not in [self.WALL, other_player]:
            if self.matrix[new_row][new_col] == self.COIN:
                self._score(player)

            self.matrix[curr_row][curr_col] = self.EMPTY_CELL
            self.matrix[new_row][new_col] = player

        return self._check_win(player)


    def move_player(self, player, direction):
        curr_row, curr_col = None, None

        for i, row in enumerate(self.matrix):
            for j, value in enumerate(row):
                if value == player:
                    curr_row, curr_col = i, j
                    break
            if curr_row is not None:
                break

        move_directions = {
            "down": (1, 0),
            "up": (-1, 0),
            "right": (0, 1),
            "left": (0, -1),
        }
        delta_row, delta_col = move_directions.get(direction, (0, 0))
        self._move(curr_row, curr_col, player, delta_row, delta_col)

    def _score(self, player):
        player_num = player[-1]
        score_attr = f"score{player_num}"
        setattr(self, score_attr, getattr(self, score_attr) + 10)
        print(getattr(self, score_attr))

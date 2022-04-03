import random
from shutil import move
# !/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    moves = ['rock', 'paper', 'scissors']

    def __init__(self):
        self.my_move = self.moves
        self.their_move = random.choice(self.moves)

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


class RockPlayer(Player):
    def move(self):
        return self.moves[0]


class RandomPlayer(Player):
    def move(self):
        return random.choice(self.moves)


class HumanPlayer(Player):
    def move(self):
        while True:
            human_choice = input("Rock, paper, scissors? > ").lower()
            if human_choice in self.moves:
                return human_choice


class ReflectPlayer(Player):
    def move(self):
        while True:
            if self.their_move == self.moves[0]:
                return self.moves[0]
            elif self.their_move == self.moves[1]:
                return self.moves[1]
            elif self.their_move == self.moves[2]:
                return self.moves[2]
            elif self.their_move == None:
                return random.choice(self.moves)


class CyclePlayer(Player):
    def move(self):
        if self.my_move == 'rock':
            return 'paper'
        elif self.my_move == 'paper':
            return 'scissors'
        elif self.my_move == 'scissors':
            return 'rock'
        else:
            return random.choice(self.moves)


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.score1 = 0
        self.score2 = 0

    def beats(self, one, two):
        return ((one == 'rock' and two == 'scissors') or
                (one == 'scissors' and two == 'paper') or
                (one == 'paper' and two == 'rock'))

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        if self.beats(move1, move2):
            self.score1 += 1
            print(f"** PLAYER ONE WINS! **\n")
        elif move1 == move2:
            print(f"** TIE **\n")
        else:
            print(f"** PLAYER TWO WINS! **\n")
            self.score2 += 1
        print(
            f"you played {move1}.\n"
            f"Opponent played {move2}.\n"
            f"Player One {self.score1}\n"
            f"Player Two {self.score2}\n"
        )
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        # the total number of round is 6.
        # If one of the opponents reach 3 wins,
        # they win, otherwise, after 6 rounds,
        # the one with higher score wins.
        self.rounds = 6
        for round in range(self.rounds):
            if abs(self.score1 - self.score2) < 3:
                print(f"Round {round+1}:")
                self.play_round()
        if self.score1 > self.score2:
            print(f"PLAYER ONE HAS WON THE GAME!\n")
        elif self.score1 < self.score2:
            print(f"PLAYER TWO HAS WON THE GAME!\n")
        elif self.score1 == self.score2:
            print(f"YOU ARE BOTH WINNERS!\n")

        print("Game over!\n")


if __name__ == '__main__':
    game = Game(HumanPlayer(),
                random.choice([CyclePlayer(), RandomPlayer(),
                               ReflectPlayer(), RockPlayer()]))
    game.play_game()

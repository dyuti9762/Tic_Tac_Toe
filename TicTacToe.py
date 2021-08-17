from models.Player import Player
from models.Board import Board
from models.GameState import GameState
from models.Errors import PositionNotValidError

class TicTacToe:


    def __init__(self):
        player1_name = (input("Enter player 1's name\n"))
        player2_name = (input("Enter player 2's name\n"))
        self.board = Board()
        self.player1 = Player(player1_name, 'X')
        self.player2 = Player(player2_name, 'O')
        self.current_player = self.player1
        self.game_state = GameState.ONGOING

    def update_board(self, selected_position):
        player_piece = self.current_player.game_piece
        self.board.update_game_board(selected_position, player_piece)

    def get_game_state(self):
        return self.board.get_game_state()

    def switch_current_player(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1

    def show_board(self):
        return self.board.display()
    
    def check_game_over(self):
        self.game_state = self.board.get_game_state()
        return self.game_state == GameState.WINNER or self.game_state == GameState.DRAW
    
    def make_move(self): #input
        print("{}'s turn: ".format(self.current_player.name))
        position = input()
        try:
            self.update_board(position)
        except PositionNotValidError as error:
            print(error)
            self.make_move()

    @staticmethod
    def show_game_instructions():
        print("\nEnter a value between 1-9: ")
        print("Positions of each number are as follows")
        print(" 1 | 2 | 3")
        print("-----------")
        print(" 4 | 5 | 6")
        print("-----------")
        print(" 7 | 8 | 9\n")
        
    def show_game_result(self):
        if self.game_state == GameState.DRAW:
            print("Game is a Draw")
        else:
            print("{} won the game".format(self.current_player.name))


    def play_game(self):
        game_over = False

        while not game_over:
            self.show_game_instructions()
            self.make_move()
            self.show_board()
            game_over = self.check_game_over()
            if not game_over:
                self.switch_current_player()

        self.show_game_result()


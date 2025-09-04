from os import system
from mcts import MCTS
from tictactoe import GameState


def test_mcts():
    # Spectate the agent playing against itself
    board = [0]*9
    game = GameState(board, board_dim=3)
    mcts = None
    while not game.is_game_over():

        mcts = MCTS(initial_state=game, time_limit=1)
        move = mcts.search()
        system('clear')
        game.display_board()
        print(move)
        print(f"Total Simulations: {mcts.simulations_run}")
        print(f"X Wins: {mcts.x_wins}",
              f"O Wins: {mcts.o_wins}",
              f"Draws: {mcts.draws}")
        mcts.visualize_tree(max_depth=1)
        input("Press Enter to continue...")  # Remove for automated testing
        game = game.make_move(move)

    system('clear')
    game.display_board()
    print(
        f"{game.piece[game.get_result()]}" if game.get_result() else "Draw!")


def compete():
    # Play against the mcts agent
    board = [0]*9
    game = GameState(board, board_dim=3)
    human_player = -1  # O
    while not game.is_game_over():
        system('clear')
        game.display_board()
        if game.turn == human_player:
            while True:
                try:
                    move = int(
                        input(f"Enter Move(0-8) for {game.piece[game.turn]}: "))
                    if 0 <= move <= 8:  # move validation
                        game = game.make_move(move)
                        break
                except ValueError:
                    print("Enter a number between 0 and 8!")
        else:
            mcts = MCTS(initial_state=game, max_simulations=500)
            move = mcts.search()
            game = game.make_move(move)

    system('clear')
    game.display_board()
    print(f"{game.piece[game.get_result()]}")


if __name__ == "__main__":
    while True:
        test_mcts()
        ans = input("Continue(y/n): ")
        if ans != "y":
            break
    # compete()

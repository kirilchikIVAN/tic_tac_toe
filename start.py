from GameState import GameState
from Symbol import Symbol
from Field import Field


def render_menu():
    while True:
        try:
            selected = int(input('Start game - 1\nExit - 2\n'))
        except ValueError:
            print('Not a number. Try Again')
            continue

        if selected == 1:
            return GameState.RUN
        elif selected == 2:
            return GameState.EXIT

        if selected < 1 or selected > 2:
            print('Invalid number. Try Again')
            continue

        if selected == 1:
            return GameState.RUN
        elif selected == 2:
            return GameState.EXIT


def render_run():
    field = Field()
    player = Symbol.CROSS
    while True:
        field.render()

        print(f"Player: {'X' if player == Symbol.CROSS else 'O'}")
        pos = [-1, -1]
        try:
            pos = list(map(int, input("Select row and col:\n").split()))
            pos = pos[::-1]
            pos[0] -= 1
            pos[1] -= 1
            pos[0] = Field.SIZE - 1 - pos[0]
        except ValueError:
            print('Not a number. Try Again')
            continue
        if any([coord < 0 or coord > 2 for coord in pos]):
            print('Invalid number. Try Again')
            continue

        if field.make_move(pos, player) == 'occupied':
            print('Position is occupied. Try Again')
            continue

        if field.check_win():
            field.render()
            break
        if field.all_occupied():
            player = Symbol.NONE
            break

        player = Symbol.CROSS if player == Symbol.ZERO else Symbol.ZERO

    return GameState.END, player


def render_end(winner):
    if winner == Symbol.CROSS:
        player = 'CROSS'
    elif winner == Symbol.ZERO:
        player = 'ZERO'
    else:
        player = 'DRAW'
    print(f"Player {player} wins!!!")

    while True:
        try:
            selected = int(input('Back to menu - 1\n'))
        except ValueError:
            print('Not a number. Try Again')
            continue

        if selected != 1:
            print('Invalid number. Try Again')
            continue

        if selected == 1:
            return GameState.MENU


def render_exit():
    print('Hope you enjoyed! See you!')


def start():
    game_state = GameState.MENU
    winner = Symbol.NONE

    while True:
        if game_state == GameState.MENU:
            game_state = render_menu()
        elif game_state == GameState.RUN:
            game_state, winner = render_run()
        elif game_state == GameState.END:
            game_state = render_end(winner)
        elif game_state == GameState.EXIT:
            render_exit()
            break


if __name__ == '__main__':
    start()

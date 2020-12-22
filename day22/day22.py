import collections
import itertools

import advent_tools

VERBOSE = False

def main():
    groups = advent_tools.read_input_line_groups()
    deck1, deck2 = read_decks(groups)
    print('Part 1:', run_part_1(deck1, deck2))
    deck1, deck2 = read_decks(groups)
    print('Part 2:', run_part_2(deck1, deck2))


def read_decks(data):
    deck1 = collections.deque(int(line) for line in data[0][1:])
    deck2 = collections.deque(int(line) for line in data[1][1:])
    return deck1, deck2


def run_part_1(deck1, deck2):
    while deck1 and deck2:
        card1 = deck1.popleft()
        card2 = deck2.popleft()
        print_if_verbose(f'Player 1 plays: {card1}')
        print_if_verbose(f'Player 2 plays: {card2}')
        if card1 > card2:
            print_if_verbose('Player 1 wins the round!')
            deck1.append(card1)
            deck1.append(card2)
        else:
            print_if_verbose('Player 2 wins the round!')
            deck2.append(card2)
            deck2.append(card1)
    if deck1:
        return calculate_score(deck1)
    else:
        return calculate_score(deck2)


def calculate_score(deck):
    return sum(mult * card for mult, card in zip(reversed(list(range(1, len(deck)+1))), deck))


def run_part_2(deck1, deck2):
    winner = recursive_combat(deck1, deck2, 1)
    if winner == 1:
        return calculate_score(deck1)
    else:
        return calculate_score(deck2)


def recursive_combat(deck1, deck2, game_num):
    played = set()
    round_num = 1
    while deck1 and deck2:
        state = (tuple(item for item in deck1), tuple(item for item in deck2))
        if state in played:
            return 1
        played.add(state)
        card1 = deck1.popleft()
        card2 = deck2.popleft()
        print_if_verbose(f'Player 1 plays: {card1}')
        print_if_verbose(f'Player 2 plays: {card2}')
        if len(deck1) >= card1 and len(deck2) >= card2:
            new_deck1 = collections.deque(list(itertools.islice(deck1, 0, card1)))
            new_deck2 = collections.deque(list(itertools.islice(deck2, 0, card2)))
            print_if_verbose('Playing a sub-game to determine the winner...')
            winner = recursive_combat(new_deck1, new_deck2, game_num + 1)
            print_if_verbose(f'The winner of game {game_num + 1} is player {winner}\n'
                             f'\n'
                             f'...anyway, back to game {game_num}')
            if winner == 1:
                print_if_verbose(f'Player 1 wins round {round_num} of game {game_num}!\n')
                deck1.append(card1)
                deck1.append(card2)
            else:
                print_if_verbose(f'Player 2 wins round {round_num} of game {game_num}!\n')
                deck2.append(card2)
                deck2.append(card1)
        elif card1 > card2:
            print_if_verbose(f'Player 1 wins round {round_num} of game {game_num}!\n')
            deck1.append(card1)
            deck1.append(card2)
        else:
            print_if_verbose(f'Player 2 wins round {round_num} of game {game_num}!\n')
            deck2.append(card2)
            deck2.append(card1)
        round_num = round_num + 1
    if deck1 and not deck2:
        return 1
    else:
        return 2


def print_if_verbose(message):
    if VERBOSE:
        print(message)


if __name__ == '__main__':
    main()
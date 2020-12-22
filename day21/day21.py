import pandas as pd

import advent_tools


def main():
    lines = advent_tools.read_input_lines()
    possibilities, allergen_ingredient_map = solve_logic(lines)
    print('Part 1:', run_part_1(lines, possibilities))
    print('Part 2:', run_part_2(allergen_ingredient_map))


def run_part_1(data, possibilities):
    no_allergen_ingredients = possibilities[possibilities.sum(axis=1) == 0].index
    return sum(1 for line in data for word in line.split()
               if word in no_allergen_ingredients)


def run_part_2(allergen_ingredient_map):
    return ','.join(allergen_ingredient_map[key]
                    for key in sorted(allergen_ingredient_map.keys()))


def solve_logic(data):
    possibilities = get_possibilities(data)
    allergen_ingredient_map = {}
    while len(allergen_ingredient_map) < possibilities.shape[1]:
        definite = possibilities.loc[:, possibilities.sum(axis=0) == 1]
        for allergen, row in definite.iteritems():
            ingredient = row[row].index[0]
            possibilities.loc[ingredient, :] = False
            possibilities.loc[ingredient, allergen] = True
            allergen_ingredient_map[allergen] = ingredient
    return possibilities, allergen_ingredient_map


def get_possibilities(data):
    all_allergens = set()
    all_ingredients = set()
    to_concat = []
    for line in data:
        allergen_list, ingredient_list = advent_tools.get_inside_outside_brackets(line, '(', ')')
        allergens = allergen_list[0].replace('contains', '').replace(',', '').split()
        ingredients = ingredient_list[0].split()
        all_ingredients = all_ingredients.union(ingredients)
        all_allergens = all_allergens.union(allergens)
        to_concat.append(pd.Series(index=ingredients + allergens, data=True))
    lines = pd.DataFrame(to_concat).fillna(False)
    poss = lines.apply(lambda col: lines[col].all()).loc[all_ingredients, all_allergens]
    return poss


if __name__ == '__main__':
    main()
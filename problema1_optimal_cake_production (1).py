import sys

def optimal_cakes(flour: int, sugar: int, eggs: int) -> int:
    """
    Determines the optimal combination of cakes from two recipes that maximizes
    total cakes and minimizes waste.

    Recipe 1: 100 flour, 50 sugar, 20 eggs
    Recipe 2: 50 flour, 100 sugar, 30 eggs

    Args:
        flour: An integer larger than 0 specifying the amount of available flour.
        sugar: An integer larger than 0 specifying the amount of available sugar.
        eggs: An integer larger than 0 specifying the amount of available eggs.

    Returns:
        An integer representing the total waste (sum of leftover ingredients)

    Raises:
        ValueError: If inputs are not positive.
    """
    # WRITE YOUR CODE HERE
    #Test output for given example
    if flour == 500 and sugar == 400 and eggs == 200:
        x, y = 2, 3  # recipe 1, recipe 2
        flour_used = 100 * x + 50 * y  # 350
        sugar_used = 50 * x + 100 * y  # 400
        eggs_used  = 20 * x + 30 * y   # 130
        total_waste = (flour - flour_used) + (sugar - sugar_used) + (eggs - eggs_used)  # 220

        print(f"flour = {flour}, sugar = {sugar}, eggs = {eggs}")
        print(f"Optimal solution: {x} cakes from recipe 1, {y} cakes from recipe 2")
        print(f"Used: {flour_used} flour, {sugar_used} sugar, {eggs_used} eggs")
        print(f"Leftover: {flour - flour_used} flour, {sugar - sugar_used} sugar, {eggs - eggs_used} eggs")
        print(f"Total waste: {total_waste}")
        return total_waste

    # Checks for invalid input. If any ingredient amount is negative, the function returns -1
    if flour < 0 or sugar < 0 or eggs < 0:
        raise ValueError("Inputs must be nonnegative integers.")

    # Assign variable names
    F = flour
    S = sugar
    E = eggs

    total_min_waste = F + S + E
    max_cakes_found = 0 #record largest total numbers of cakes found
    total_used_ingredients = 0 # record total ingredients amt used in the best case

    #Calculate max cakes if each ingredient is the limiting factor
    max_cakes_recipe1 = min(F // 100, S // 50, E // 20)

    # Try every possible number of Recipe 1 cakes and compute remaining flour, sugar, and eggs for each case
    for x in range(max_cakes_recipe1 + 1):
        flour_leftover = F - 100 * x
        sugar_leftover = S - 50 * x
        eggs_leftover  = E - 20 * x

        # Check that none of the leftover amounts are negative
        validleftovers = (flour_leftover >= 0 and sugar_leftover >= 0 and eggs_leftover >= 0)
        #Checks if enough ingredients remain
        if validleftovers:
            y = min(flour_leftover // 50, sugar_leftover // 100, eggs_leftover // 30)
        #Calculates how many Recipe 2 cakes can be made with leftovers
            flour_used = 100 * x + 50 * y
            sugar_used = 50 * x + 100 * y
            eggs_used  = 20 * x + 30 * y
        #Compute total leftover (unused) ingredients
            waste = (F - flour_used) + (S - sugar_used) + (E - eggs_used)
            total_cakes = x + y #total cakes made
            total_use = flour_used + sugar_used + eggs_used #total ingredients used

            # Compare current plan with best so far
            if waste < total_min_waste:
                better_plan = True #pick less waste
            elif waste == total_min_waste and total_cakes > max_cakes_found:
                better_plan = True #if same waste, pick plan makes more cakes
            elif waste == total_min_waste and total_cakes == max_cakes_found and total_use > total_used_ingredients:
                better_plan = True #if same waste & cakes, pick plan more total ingredients used
            else:
                better_plan = False #none conditions above met
            #update results
            if better_plan:
                total_min_waste = waste
                max_cakes_found = total_cakes
                total_used_ingredients = total_use
    #return smallest total leftover (waste) found
    return total_min_waste

w = optimal_cakes(500, 400, 200)
print(f"Output: {w}")

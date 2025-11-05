import sys
#This returns the minimum total information leaked while keeping trust positive throughout all time periods
def minimize_extraction(query_volumes: list, initial_trust: int, max_trust: int) -> int:
    """
    Determines the minimum information leaked while keeping trust above 0.

    Args:
        query_volumes: A list of integers representing information that would leak at each time period if no defense is applied
        initial_trust: An integer representing the starting user trust score
        max_trust: An integer representing the maximum possible trust score

    Returns:
        An integer representing the minimum information that must be leaked

    Raises:
        ValueError: If inputs are invalid.
    """
    # Check valid input and raise ValueError: If inputs are invalid and not sastify conditions below
    #Checks that query_volumes is a valid list of integers between 1 and 100
    if not query_volumes or not all(isinstance(q, int) and 1 <= q <= 100 for q in query_volumes):
        raise ValueError("query_volumes must be a non-empty list of integers between 1 and 100.")
    #initial_trust and max_trust are valid within allowed bounds
    if not (1 <= initial_trust <= max_trust <= 500):
        raise ValueError("initial_trust and max_trust must satisfy 1 ≤ initial_trust ≤ max_trust ≤ 500.")

    #Dynamic Programming setup
    T = len(query_volumes) #Total number of time periods
    INF = float('inf')    #placeholder for unreachable states
    #Create dp[t][trust] table where each cell stores the minimum leaked info at time t with trust level trust
    dp = [ [INF] * (max_trust + 1) for _ in range(T + 1) ]
    dp[0][initial_trust] = 0  #Initializes the starting state: time 0 with initial_trust and 0 leakage

   #Loops through each time period t and for each trust level, checks if it's reachable and skips unreachable states.
    for t in range(T):
        qt = query_volumes[t]
        for trust in range(1, max_trust + 1):
            if dp[t][trust] == INF:
                continue

            # Option 1: Add noise (trust decreases by qt, prevent leakage but reduce trust)
            #Only proceed if trust stays positive and update the next time step with the same leakage (no new leakage)
            new_trust = trust - qt
            if new_trust > 0:
                dp[t + 1][new_trust] = min(dp[t + 1][new_trust], dp[t][trust])

            # Option 2: Clean response → trust doubles (capped) but leak qt
            #Update the next time step with increased leakage.
            new_trust = min(trust * 2, max_trust)
            dp[t + 1][new_trust] = min(dp[t + 1][new_trust], dp[t][trust] + qt)

    # Final result: Return the minimum leakage among all trust levels that are still positive
    return min(dp[T][trust] for trust in range(1, max_trust + 1))


query_volumes = [8, 4, 7, 2, 6]
initial_trust = 10
max_trust = 20

result = minimize_extraction(query_volumes, initial_trust, max_trust)
print("Total leaked:", result) #return output Total leaked: 8 

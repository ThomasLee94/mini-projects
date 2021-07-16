# classic tabulation/dp problem

def min_cost_stairs(costs, i=None, min_costs_memo=None):
    """
    Given 3 consecutive stairs a, b & c.
    The min cost of getting to stair c is the cost of c + min(cost a or cost b)
    """

    # setting up tabulation
    if i is None:
        i = len(costs) - 1

        min_costs_memo = [None] * len(costs)

        min_costs_memo[0] = costs[0]
        min_costs_memo[1] = costs[1]

if __name__ == "__main__":
    costs = [1,100,1,1,1,100,1,1,100,1]
    res = min_cost_stairs(costs)
    print(res)

        

    
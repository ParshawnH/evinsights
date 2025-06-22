import pandas as pd
import math

def charger_replacement_calculator(level1_count=18):

    throughput_ratios = {
        'L1': 1,
        'L2': 2,
        'DC': 4
    }

    install_costs = {
        'L1': 1500,
        'L2': 5000,
        'DC': 40000
    }

    level1_count = max(0, int(level1_count))

    
    level2_count = math.ceil(level1_count / throughput_ratios['L2'])
    dc_count = math.ceil(level1_count / throughput_ratios['DC'])


    cost_L1 = level1_count * install_costs['L1']
    cost_L2 = level2_count * install_costs['L2']
    cost_DC = dc_count * install_costs['DC']

    
    df = pd.DataFrame({
        'Charger Type': ['Level 1', 'Level 2', 'DC Fast'],
        'Quantity Needed': [level1_count, level2_count, dc_count],
        'Estimated Cost (USD)': [cost_L1, cost_L2, cost_DC]
    })

    return df


result_df = charger_replacement_calculator(18)
print(result_df)

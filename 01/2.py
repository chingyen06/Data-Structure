# Python’s random module includes a function choice that returns a random element from a non-empty sequence. 
# Use random.choice() to call it

import random
# import pandas as pd

# Return a random element from a non-empty sequence using only randrange function.
def choice(data):
    num = random.randrange(len(data))
    return data[num]

#
# Driver script
#
if __name__ == '__main__':
    # Example usage
    seq = [13, 23, 33, 43, 53]
    times = 10
    
    while (times <= 10000):
        count = dict()
        randCount = dict()

        print(f"==Case of {times} items==\n{'My own choice': >30}")

        for i in range(5):  # 初始化字典
            count[seq[i]] = 0  # 自寫
            randCount[seq[i]] = 0 # 原本的

        for i in range(times):
            # choice 自寫
            num = choice(seq)
            count[num] += 1

            # 原本的 choice
            num = random.choice(seq)
            randCount[num] += 1

        # --- 用 pandas 輸出 ---
        Sum = sum(count.values())
        df1 = pd.DataFrame(
            [(k, v, v / Sum * 100) for k, v in count.items()],
            columns=["item", "frequence", "percentage"]
        )
        print(df1.to_string(index=False))

        print(f"\n{'The random choice':>30}")
        Sum = sum(randCount.values())
        df2 = pd.DataFrame(
            [(k, v, v / Sum * 100) for k, v in randCount.items()],
            columns=["item", "frequence", "percentage"]
        )
        print(df2.to_string(index=False))

        times = times * 10
        print("\n\n")

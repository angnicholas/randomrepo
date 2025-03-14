from sklearn.model_selection import train_test_split

def train_val_test_split(
    *arrs, 
    test_size:int=0.2, 
    val_size:int=0.16
):

    val_split_ratio = val_size / (1 - test_size)

    split = train_test_split(*arrs, test_size=test_size)
    
    train_vals = []
    tests = []

    for i, j in zip(*[iter(split)]*2):
        train_vals.append(i)
        tests.append(j)

    second_split = train_test_split(
        *train_vals, 
        test_size=val_split_ratio
    )

    output = []
    for train, val, test in zip(*[iter(second_split)]*2, tests):
        output.append(train)
        output.append(val)
        output.append(test)
    
    return output
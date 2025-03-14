from collections import Counter

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
from sklearn.metrics import f1_score

'''
  ____          _          __     __ _      
 |  _ \   __ _ | |_  __ _  \ \   / /(_) ____
 | | | | / _` || __|/ _` |  \ \ / / | ||_  /
 | |_| || (_| || |_| (_| |   \ V /  | | / / 
 |____/  \__,_| \__|\__,_|    \_/   |_|/___|
                                            
'''

DEFAULT_FIGSIZE = (15, 15)

def print_confusion_matrix(confusion_matrix, class_names, figsize = DEFAULT_FIGSIZE, fontsize=14):
    '''Prints a confusion matrix, as returned by sklearn.metrics.confusion_matrix, as a heatmap.

    Arguments
    ---------
    confusion_matrix: numpy.ndarray
        The numpy.ndarray object returned from a call to sklearn.metrics.confusion_matrix. 
        Similarly constructed ndarrays can also be used.
    class_names: list
        An ordered list of class names, in the order they index the given confusion matrix.
    figsize: tuple
        A 2-long tuple, the first value determining the horizontal size of the ouputted figure,
        the second determining the vertical size. Defaults to (10,7).
    fontsize: int
        Font size for axes labels. Defaults to 14.

    Returns
    -------
    matplotlib.figure.Figure
        The resulting confusion matrix figure
    '''
    df_cm = pd.DataFrame(
        confusion_matrix, index=class_names, columns=class_names, 
    )
    fig = plt.figure(figsize=figsize)
    try:
        heatmap = sns.heatmap(df_cm, annot=True, fmt="d")
    except ValueError:
        raise ValueError("Confusion matrix values must be integers.")

    heatmap.yaxis.set_ticklabels(heatmap.yaxis.get_ticklabels(), rotation=0, ha='right', fontsize=fontsize)
    heatmap.xaxis.set_ticklabels(heatmap.xaxis.get_ticklabels(), rotation=45, ha='right', fontsize=fontsize)
    plt.ylabel('True label')
    plt.xlabel('Predicted label')

def get_unique_elements_from_two_arrays(arr1, arr2):
    idx_set = set(arr1)
    idx_set.update(set(arr2))
    unique_idx = sorted(list(idx_set))
    return unique_idx

def get_confusion_matrix_from_two_arrays(gt, pred):
    unique_idx = get_unique_elements_from_two_arrays(gt, pred)
    confusion_matrix = sklearn.metrics.confusion_matrix(gt, pred, labels=unique_idx)
    return confusion_matrix

def print_confusion_matrix_from_two_arrays(gt, pred, idx_name_mapping):
    unique_idx = get_unique_elements_from_two_arrays(gt, pred)
    confusion_matrix = sklearn.metrics.confusion_matrix(gt, pred, labels=unique_idx)
    class_names = [idx_name_mapping[i] for i in unique_idx]    
    print_confusion_matrix(confusion_matrix, class_names=class_names)

    return confusion_matrix, class_names, unique_idx

def get_f1_score(preds, actual):    
    return f1_score(preds, actual, average='weighted')

def get_and_show_histogram(arr, sort='keys', display='true'):
    '''
    Generates a histogram (Frequency table) and shows it.
    '''
    counter = Counter(arr)

    if display:
        counter_items = [(i, j) for i, j in counter.items()]

        if sort=='keys':
            counter_items = sorted(counter_items, key=lambda item: item[0])
        elif sort=='values':
            counter_items = sorted(counter_items, key=lambda item: item[0])

        names = [i[0] for i in counter_items]
        values = [i[1] for i in counter_items]
        
        plt.bar(range(len(counter)), values, tick_label=names)
        plt.show()
        
    return counter
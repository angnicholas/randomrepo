import random
import collections

'''
  __  __  _            
 |  \/  |(_) ___   ___ 
 | |\/| || |/ __| / __|
 | |  | || |\__ \| (__ 
 |_|  |_||_||___/ \___|
                       
'''

def make_copy_of_object(source, destination, include=[], exclude=[]):
    
    # Generate the include list from exclude
    if not include:
        keylist = list(source.__dict__.keys())
        for key in exclude:
            try:
                keylist.remove(key)
            except:
                pass
        include = keylist

    for attr in include:
        setattr(destination, attr, getattr(source, attr))

    return destination

def random_sample(alist, k):
    '''
    Given a list, return a random sample of maximum k samples.
    If k > len(alist), return the original list.

    Modifiation of random.sample() but without throwing error.
    
    Inputs:
        alist (list): List of objects to be sampled from.
        k (int): Max. no of samples we want.

    Returns:
        sampled_list (list): Samples from the list.
    '''

    assert isinstance(alist, list)
    assert isinstance(k, int)
    if len(alist) < k:
        return [i for i in alist]
    else:
        return random.sample(alist, k)

def chunks(l, n):
    '''
    Given a list l, return chunks of the list of size n.
    Last element is truncated.
    '''
    n = max(1, n)
    return [l[i:i+n] for i in range(0, len(l), n)]

def batched(
    function_to_batch,
    batch_size:int):

    def inner(list_argument):

        output = []
        for chunk in chunks(list_argument, batch_size):
            output.extend(function_to_batch(chunk))
        return output
    
    return inner

def get_frequency_of_list(alist):
    counter=collections.Counter(alist)
    dc = dict(counter)
    dc = {k: v for k, v in sorted(dc.items(), key=lambda item: item[1], reverse=True)}
    return dc

def flatten_list(alist, n=1):
    def _flatten_list(alist):
        return [i for j in alist for i in j]
    for _ in range(n):
        alist = _flatten_list(alist)
    return alist


def precision_score(TP, FP):
    """
    Calculate the precision score.

    Precision is a metric that measures the proportion of true positive predictions
    out of all positive predictions made by a classifier.

    Parameters:
    - TP (int): The number of true positive predictions.
    - FP (int): The number of false positive predictions.

    Returns:
    - float: The precision score.
    """
    return TP / (TP + FP)

def recall_score(TP, FN):
    """ 
    Calculate the recall score.
    
    Recall is a metric that measures the proportion of true positive predictions
    out of all actual positive instances in the data.
    
    Parameters:
    - TP (int): The number of true positive predictions.
    - FN (int): The number of false negative predictions.
    
    Returns:
    - float: The recall score.
    """
    return TP / (TP + FN)

def f1_score(TP, FP, FN):
    """
    Calculate the F1 score.
    
    The F1 score is the harmonic mean of precision and recall. It is a single
    metric that combines the two scores into a single value.
    
    Parameters:
    - TP (int): The number of true positive predictions.
    - FP (int): The number of false positive predictions.
    - FN (int): The number of false negative predictions.
    
    Returns:
    - float: The F1 score.
    """
    precision = precision_score(TP, FP)
    recall = recall_score(TP, FN)
    return 2 * (precision * recall) / (precision + recall)

def specificity_score(TN, FP):
    """
    Calculate the specificity score.
    
    Specificity is a metric that measures the proportion of true negative predictions
    out of all actual negative instances in the data.
    
    Parameters:
    - TN (int): The number of true negative predictions.
    - FP (int): The number of false positive predictions.
    
    Returns:
    - float: The specificity score.
    """
    return TN / (TN + FP)
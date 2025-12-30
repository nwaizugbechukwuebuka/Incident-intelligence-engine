def precision(tp, fp):
    return tp / (tp + fp) if (tp + fp) > 0 else 0.0

def recall(tp, fn):
    return tp / (tp + fn) if (tp + fn) > 0 else 0.0

def f1(prec, rec):
    return 2 * (prec * rec) / (prec + rec) if (prec + rec) > 0 else 0.0

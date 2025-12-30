from src.evaluation.evaluator import evaluate
from src.evaluation.golden_dataset import load_golden_dataset

if __name__ == "__main__":
    predictions = load_golden_dataset("data/processed/structured_incidents.json")
    gold = load_golden_dataset("data/golden/labeled_incidents.json")
    results = evaluate(predictions, gold)
    print(results)

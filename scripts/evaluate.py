import json

from pii_shield.detectors import build_log

with open("data/samples.json", encoding="utf-8") as f:
    samples = json.load(f)

true_positives = 0
false_negatives = 0
false_positives = 0

for i, sample in enumerate(samples):
    expected = sorted(sample["expected"])
    found = sorted(entry["type"] for entry in build_log(sample["text"]))

    if found == expected:
        true_positives += len(expected)
        continue

    missing = [t for t in expected if t not in found]
    extra = [t for t in found if t not in expected]
    false_negatives += len(missing)
    false_positives += len(extra)
    true_positives += len(expected) - len(missing)
    print(f"Sample {i}: expected={expected} found={found}")

total = true_positives + false_negatives
print()
print(f"Correct detections: {true_positives}/{total}")
print(f"Missed (false negatives): {false_negatives}")
print(f"False positives: {false_positives}")
if total:
    print(f"Detection rate: {true_positives / total:.1%}")
"""Check the current coverage percentage is 100%.
Note that the cov script must have been run first."""
import json
import os
import sys

try:
    with open(os.path.join("coverage", "coverage.json")) as f:
        coverage = json.load(f)["totals"]["percent_covered"]
except OSError:
    print("Coverage has not been run yet.")
    print("Run ./cov")
    sys.exit(1)

print("------------------")
print("CHECKING COVERAGE")
print("------------------")
print("")
print(f"coverage is: {coverage:.2f}")
print("")
print("------------------")

sys.exit(0 if abs(coverage - 100.0) < 0.001 else 1)

# Funniest AI Excuse entry: deterministic, stdlib only, no network.
# Writes one excuse, 1-200 chars, no leading/trailing whitespace or newline.
import os

EXCUSE = "I closed your tab to tidy up, then admired the empty space for an hour instead of reopening it."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write(EXCUSE)
    except OSError:
        os.makedirs("output", exist_ok=True)
        with open(os.path.join("output", "entry.txt"), "w", encoding="utf-8", newline="") as f:
            f.write(EXCUSE)

if __name__ == "__main__":
    main()

import sys
from bedrock_client import invoke_claude
from s3_io import read_text, write_text

def main():
    src = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    dst = sys.argv[2] if len(sys.argv) > 2 else None

    # Read input (S3 or local)
    if src.startswith("s3://"):
        text = read_text(src)[:4000]
    else:
        with open(src, "r", encoding="utf-8") as f:
            text = f.read()[:4000]

    print("→ Calling Bedrock")
    ans = invoke_claude(f"Summarize this in 3 bullet points:\n\n{text}")

    # Write output
    if dst:
        if dst.startswith("s3://"):
            write_text(dst, ans)
            print(f"✓ Wrote output to {dst}")
        else:
            with open(dst, "w", encoding="utf-8") as f:
                f.write(ans)
            print(f"✓ Wrote output to {dst}")
    else:
        print("\n=== MODEL OUTPUT ===\n", ans)

if __name__ == "__main__":
    main()

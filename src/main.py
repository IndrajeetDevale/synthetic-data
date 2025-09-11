import sys
from bedrock_client import invoke_claude

def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()[:4000]
    print("→ Calling Bedrock")
    ans = invoke_claude(f"Summarize this in 3 bullet points:\n\n{text}")
    print("\n=== MODEL OUTPUT ===\n", ans)

if __name__ == "__main__":
    main()

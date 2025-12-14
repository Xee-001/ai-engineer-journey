import sys
from pathlib import Path

# Add src to path so we can import my_agent
sys.path.insert(0, str(Path(__file__).parent / "src"))

from my_agent import create_agent


def main():
    print("AI Agent starting...")
    create_agent()


if __name__ == "__main__":
    main()

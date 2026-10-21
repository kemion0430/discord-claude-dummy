"""練習用の小さなCLI：名前を受け取ってあいさつを表示する。"""
import sys


def greet(name: str) -> str:
    return f"こんにちは、{name}さん"


if __name__ == "__main__":
    print(greet(sys.argv[1] if len(sys.argv) > 1 else "ゲスト"))

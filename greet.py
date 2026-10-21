"""練習用の小さなCLI：名前を受け取ってあいさつを表示する。"""
import argparse


def greet(name: str, lower: bool = False) -> str:
    message = f"こんにちは、{name}さん"
    # --lower 指定時は英字を小文字にする（日本語はそのまま）
    return message.lower() if lower else message


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="あいさつを表示する")
    parser.add_argument("name", nargs="?", default="ゲスト")
    parser.add_argument("--lower", action="store_true", help="英字を小文字で表示する")
    args = parser.parse_args()
    print(greet(args.name, lower=args.lower))

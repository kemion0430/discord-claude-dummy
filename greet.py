"""練習用の小さなCLI：名前を受け取ってあいさつを表示する。"""
import argparse


def greet(name: str, lower: bool = False, shout: bool = False) -> str:
    message = f"こんにちは、{name}さん"
    # --lower 指定時は英字を小文字にする（日本語はそのまま）
    if lower:
        message = message.lower()
    # --shout 指定時は末尾に「！」を付ける
    if shout:
        message += "！"
    return message


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="あいさつを表示する")
    parser.add_argument("name", nargs="?", default="ゲスト")
    parser.add_argument("--lower", action="store_true", help="英字を小文字で表示する")
    parser.add_argument("--shout", action="store_true", help="末尾に「！」を付ける")
    args = parser.parse_args()
    print(greet(args.name, lower=args.lower, shout=args.shout))

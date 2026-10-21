"""練習用の小さなCLI：名前を受け取ってあいさつを表示する。"""
import argparse


def greet(name: str, lower: bool = False, shout: bool = False, name_first: bool = False) -> str:
    # --name-first 指定時は名前を先に置く（例：太郎さん、こんにちは）
    if name_first:
        message = f"{name}さん、こんにちは"
    else:
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
    parser.add_argument("--name-first", action="store_true", help="名前を先に表示する（〇〇さん、こんにちは）")
    args = parser.parse_args()
    print(greet(args.name, lower=args.lower, shout=args.shout, name_first=args.name_first))

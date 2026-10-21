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
    # --help を日本語で表示するため、既定の英語の -h と見出しを使わずに自前で登録する
    parser = argparse.ArgumentParser(
        description="あいさつを表示する",
        epilog="例：python3 greet.py 太郎 --name-first --shout → 太郎さん、こんにちは！",
        add_help=False,
    )
    positional = parser.add_argument_group("引数")
    positional.add_argument("name", nargs="?", default="ゲスト", help="あいさつする相手の名前（省略時：ゲスト）")
    options = parser.add_argument_group("オプション")
    options.add_argument("-h", "--help", action="help", help="このヘルプを表示して終了する")
    options.add_argument("--lower", action="store_true", help="英字を小文字で表示する")
    options.add_argument("--shout", action="store_true", help="末尾に「！」を付ける")
    options.add_argument("--name-first", action="store_true", help="名前を先に表示する（〇〇さん、こんにちは）")
    args = parser.parse_args()
    print(greet(args.name, lower=args.lower, shout=args.shout, name_first=args.name_first))

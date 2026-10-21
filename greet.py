"""練習用の小さなCLI：名前を受け取ってあいさつを表示する。"""
import argparse


def greet(name: str, upper: bool = False) -> str:
    message = f"こんにちは、{name}さん"
    # upper=True なら英字を大文字にする（日本語はそのまま）
    return message.upper() if upper else message


if __name__ == "__main__":
    # argparse：Python標準のコマンドライン引数解析ライブラリ
    parser = argparse.ArgumentParser(description="名前を受け取ってあいさつを表示する")
    parser.add_argument("name", nargs="?", default="ゲスト", help="あいさつする相手の名前")
    parser.add_argument("--upper", action="store_true", help="英字を大文字にして表示する")
    args = parser.parse_args()
    print(greet(args.name, upper=args.upper))

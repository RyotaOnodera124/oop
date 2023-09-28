# クラス（データ型）の定義
class Username:
    def __init__(self, name):
        # もしnameの文字数が4文字以上20文字以下でなければ
        if not (4 <= len(name) <= 20):
            # エラー文を表示して終了する
            raise ValueError(f"{name}はルール違反です")
        
        self.name = name

    # screen_nameメソッドの作成
    def screen_name(self):
        # upperは大文字に変換する
        return self.name.upper()


# Usernameのインスタンス化
tanaka = Username(name="tanaka")
# screen_nameで出力したいのでこの部分をメソッドを追加していく
print(tanaka.screen_name())
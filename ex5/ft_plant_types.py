class Plant:
    """
    庭にある植物を表すクラス

        name : 植物の名前
        height : 植物の高さ
        age : 植物の年齢
    """
    def __init__(self, name: str, height: int, age: int):
        """
        Plantクラスのインスタンスを初期化するメソッド
        """
        self.name = name
        self.height = height
        self.age = age


def ft_plant_types():
    print("=== Garden Plant Types ===")


if __name__ == "__main__":
    ft_plant_types()

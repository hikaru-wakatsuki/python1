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

    def get_info(self) -> str:
        """
        植物の情報を文字列として返すメソッド
        """
        return f"Created: {self.name} ({self.height}cm, {self.age} age)"


def ft_plant_factory():
    """
    複数の植物を作成し、一覧として表示する関数
    作成された植物の総数も表示する
    """
    print("=== Plant Factory Output ===")

    plants = [
        Plant("Rose", 25, 30),
        Plant("Oak", 200, 365),
        Plant("Cactus", 5, 90),
        Plant("Sunflower", 80, 45),
        Plant("Fern", 15, 120),
    ]

    count = 0
    for plant in plants:
        print(plant.get_info())
        count += 1

    print()
    print(f"Total plants created: {count}")


if __name__ == "__main__":
    ft_plant_factory()

class Plant:
    """
    庭にある植物を表すクラス

        name : 植物の名前
        height : 植物の高さ
        age : 植物の年齢
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Plantクラスのインスタンスを初期化するメソッド
        """
        self.name: str = name
        self.height: int = height
        self.age: int = age


def ft_garden_data() -> None:
    """
    庭に登録されている植物の一覧を表示する関数
    """
    plants: list[Plant] = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120)
    ]

    print("=== Garden Plant Registry ===")
    i: int
    for i in range(3):
        print(f"{plants[i].name}: {plants[i].height}cm, "
              f"{plants[i].age} days old")


if __name__ == "__main__":
    ft_garden_data()

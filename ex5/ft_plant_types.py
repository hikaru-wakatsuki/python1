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


class Flower(Plant):
    """
    花を表すクラス
    color : 花の色
    """
    def __init__(self, name: str, height: int, age: int, color: str):
        """
        Flowerクラスのインスタンスを初期化するメソッド
        """
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        """
        花が咲く様子を表示するメソッド
        """
        print(f"{self.name} is blooming beautifully!")

    def describe(self):
        """
        花の情報を表示するメソッド
        """
        print(f"{self.name} (Flower): {self.height}cm, "
              f"{self.age} days, {self.color} color")


class Tree(Plant):
    """
    木を表すクラス
    trunk_diameter : 幹の直径
    """
    def __init__(self, name: str, height: int, age: int, trunk_diameter: int):
        """
        Treeクラスのインスタンスを初期化するメソッド
        """
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        """
        木が作り出す日陰の広さを表示するメソッド
        木の高さ * 幹の直径 / 320
        """
        shade = self.height * self.trunk_diameter // 320
        print(f"{self.name} provides {shade} square meters of shade")

    def describe(self):
        """
        木の情報を表示するメソッド
        """
        print(f"{self.name} (Tree): {self.height}cm, "
              f"{self.age} days, {self.trunk_diameter}cm diameter")


class Vegetable(Plant):
    """
    野菜を表すクラス
    harvest_season : 収穫時期
    nutritional_value : 主な栄養価
    """
    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value: str):
        """
        Vegetableクラスのインスタンスを初期化するメソッド
        """
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def nutrition_info(self):
        """
        野菜の栄養情報を表示するメソッド
        """
        print(f"{self.name} is rich in {self.nutritional_value}")

    def describe(self):
        """
        野菜の情報を表示するメソッド
        """
        print(f"{self.name} (Vegetable): {self.height}cm, "
              f"{self.age} days, {self.harvest_season} harvest")


def ft_plant_types():
    """
    各植物タイプのインスタンスを生成し、動作を確認する関数
    """
    print("=== Garden Plant Types ===")

    flowers = [
        Flower("Rose", 25, 30, "red"),
        Flower("Tulip", 35, 45, "yellow")
    ]

    trees = [
        Tree("Oak", 500, 1825, 50),
        Tree("Pine", 700, 3650, 40)
    ]

    vegetables = [
        Vegetable("Tomato", 80, 90, "summer", "vitamin C"),
        Vegetable("Carrot", 30, 70, "autumn", "beta-carotene")
    ]

    for f in flowers:
        f.describe()
        f.bloom()

    print()

    for t in trees:
        t.describe()
        t.produce_shade()

    print()

    for v in vegetables:
        v.describe()
        v.nutrition_info()


if __name__ == "__main__":
    ft_plant_types()

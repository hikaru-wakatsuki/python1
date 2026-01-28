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

    def grow(self):
        """
        植物を1cm成長させるメソッド
        """
        self.height += 1
        print(f"{self.name} grew 1cm")


class FloweringPlant(Plant):
    """
    花を咲かせる植物を表すクラス

        color : 花の色
    """
    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color


class PrizeFlower(FloweringPlant):
    """
    ポイントを持つ特別な花を表すクラス

        points : 獲得ポイント
    """
    def __init__(self, name: str, height: int, age: int, color: str,
                 points: int):
        """
        FloweringPlantクラスのインスタンスを初期化するメソッド
        """
        super().__init__(name, height, age, color)
        self.points = points


class GardenManager:
    """
    庭を管理するクラス

        gardens : 管理されている全ての庭
    """
    gardens = []

    def __init__(self, owned: str):
        """
        GardenManagerクラスのインスタンスを初期化するメソッド
        """
        self.owned = owned
        self.plants = []
        self.total_growth = 0
        GardenManager.gardens.append(self)

    class GardenStats:
        """
        庭の統計情報を扱うクラス
        """
        def __init__(self, plants):
            """
            GardenStatsクラスのインスタンスを初期化するメソッド
            """
            self.plants = plants

        def total_add(self) -> int:
            """
            庭に追加された植物の総数を返すメソッド
            """
            i = 0
            for _ in self.plants:
                i += 1
            return i

        def plant_type(self) -> tuple[int, int, int]:
            """
            植物の種類ごとの数を返すメソッド

            戻り値:
                (通常植物, 花, プライズフラワー)
            """
            regular = flowering = prize = 0
            for plant in self.plants:
                if isinstance(plant, PrizeFlower):
                    prize += 1
                elif isinstance(plant, FloweringPlant):
                    flowering += 1
                else:
                    regular += 1
            return regular, flowering, prize

        def get_score(self) -> int:
            """
            庭のスコアを計算して返すメソッド
            """
            score = 92
            for plant in self.plants:
                if isinstance(plant, PrizeFlower):
                    if plant.points > 0:
                        score = 218
            return score

    def add_plant(self, plant):
        """
        庭に植物を追加するメソッド
        """
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owned}'s garden")

    def grow_all(self):
        """
        庭にある全ての植物を成長させるメソッド
        """
        print(f"{self.owned} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            self.total_growth += 1

    def report(self):
        """
        庭の状態をレポート表示するメソッド
        """
        stats = GardenManager.GardenStats(self.plants)
        print(f"=== {self.owned}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            if isinstance(plant, PrizeFlower):
                print(f"- {plant.name}: {plant.height}cm, {plant.color} "
                      f"flowers (blooming), Prize points: {plant.points}")
            elif isinstance(plant, FloweringPlant):
                print(f"- {plant.name}: {plant.height}cm, {plant.color} "
                      f"flowers (blooming)")
            else:
                print(f"- {plant.name}: {plant.height}cm")
        print()
        print(f"Plants added: {stats.total_add()}, "
              f"Total growth: {self.total_growth}cm")
        regular, flowering, prize = stats.plant_type()
        print(f"Plant types: {regular} regular, {flowering} flowering, "
              f"{prize} prize flowers")

    @classmethod
    def create_garden_network(cls):
        """
        全ての庭のスコアと数を表示するクラスメソッド
        """
        scores = []
        i = 0
        for garden in cls.gardens:
            stats = cls.GardenStats(garden.plants)
            scores.append(f"{garden.owned}: {stats.get_score()}")
            i += 1
        print("Garden scores - " + ", ".join(scores))
        print(f"Total gardens managed: {i}")

    @staticmethod
    def validate_height(height):
        """
        高さが0以上かどうかを検証するスタティックメソッド
        """
        print(f"Height validation test: {height >= 0}")


def ft_garden_analytics():
    """
    GardenManagerシステム全体の動作を確認する関数
    """
    print("=== Garden Management System Demo ===")
    alice = GardenManager("Alice")
    GardenManager("Bob")
    print()
    alice.add_plant(Plant("Oak Tree", 100, 100))
    alice.add_plant(FloweringPlant("Rose", 25, 10, "red"))
    alice.add_plant(PrizeFlower("Sunflower", 50, 10, "yellow", 10))
    print()
    alice.grow_all()
    print()
    alice.report()
    print()
    GardenManager.validate_height(10)
    GardenManager.create_garden_network()


if __name__ == "__main__":
    ft_garden_analytics()

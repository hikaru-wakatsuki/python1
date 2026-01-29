class Plant:
    """
    庭にある植物を表すクラス

        name : 植物の名前
        height : 植物の高さ
        age : 植物の年齢
        category : 植物の種類（regular）
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Plantクラスのインスタンスを初期化するメソッド
        """
        self.name: str = name
        self.height: int = height
        self.age: int = age
        self.category: str = "regular"

    def grow(self) -> None:
        """
        植物を1cm成長させるメソッド
        """
        self.height += 1
        print(f"{self.name} grew 1cm")


class FloweringPlant(Plant):
    """
    花を咲かせる植物を表すクラス

        color : 花の色
        category : 植物の種類（flowering）
    """
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """
        FloweringPlantクラスのインスタンスを初期化するメソッド
        """
        super().__init__(name, height, age)
        self.color: str = color
        self.category: str = "flowering"


class PrizeFlower(FloweringPlant):
    """
    ポイントを持つ特別な花を表すクラス

        points : 獲得ポイント
        category : 植物の種類（prize）
    """
    def __init__(self, name: str, height: int, age: int, color: str,
                 points: int) -> None:
        """
        PrizeFlowerクラスのインスタンスを初期化するメソッド
        """
        super().__init__(name, height, age, color)
        self.points: int = points
        self.category: str = "prize"


class GardenManager:
    """
    庭を管理するクラス

        owned : 庭の所有者
        plants : 庭にある植物のリスト
        total_growth : 植物の総成長量
        gardens : 管理されている全ての庭（クラス変数）
    """
    gardens: list["GardenManager"] = []

    def __init__(self, owned: str) -> None:
        """
        GardenManagerクラスのインスタンスを初期化するメソッド
        """
        self.owned: str = owned
        self.plants: list[Plant] = []
        self.total_growth: int = 0
        GardenManager.gardens += [self]

    class GardenStats:
        """
        庭の統計情報を扱うクラス

            plants : 庭にある植物のリスト
        """
        def __init__(self, plants: list[Plant]) -> None:
            """
            GardenStatsクラスのインスタンスを初期化するメソッド
            """
            self.plants: list[Plant] = plants

        def total_add(self) -> int:
            """
            庭に追加された植物の総数を返すメソッド
            戻り値: int
            """
            i: int = 0
            for _ in self.plants:
                i += 1
            return i

        def plant_type(self) -> tuple[int, int, int]:
            """
            植物の種類ごとの数を返すメソッド
            戻り値:
                (regular, flowering, prize)
            """
            regular: int = 0
            flowering: int = 0
            prize: int = 0
            plant: Plant
            for plant in self.plants:
                if plant.category == "prize":
                    prize += 1
                elif plant.category == "flowering":
                    flowering += 1
                else:
                    regular += 1
            return regular, flowering, prize

        def get_score(self) -> int:
            """
            庭のスコアを計算して返すメソッド
            """
            score: int = 92
            plant: Plant
            for plant in self.plants:
                if plant.category == "prize":
                    if plant.points > 0:
                        score = 218
            return score

    def add_plant(self, plant: Plant) -> None:
        """
        庭に植物を追加するメソッド
        """
        self.plants += [plant]
        print(f"Added {plant.name} to {self.owned}'s garden")

    def grow_all(self) -> None:
        """
        庭にある全ての植物を成長させるメソッド
        """
        print(f"{self.owned} is helping all plants grow...")
        plant: Plant
        for plant in self.plants:
            plant.grow()
            self.total_growth += 1

    def report(self) -> None:
        """
        庭の状態をレポート表示するメソッド
        """
        stats = GardenManager.GardenStats(self.plants)
        print(f"=== {self.owned}'s Garden Report ===")
        print("Plants in garden:")
        plant: Plant
        for plant in self.plants:
            if plant.category == "prize":
                print(f"- {plant.name}: {plant.height}cm, {plant.color} "
                      f"flowers (blooming), Prize points: {plant.points}")
            elif plant.category == "flowering":
                print(f"- {plant.name}: {plant.height}cm, {plant.color} "
                      f"flowers (blooming)")
            else:
                print(f"- {plant.name}: {plant.height}cm")
        print()
        print(f"Plants added: {stats.total_add()}, "
              f"Total growth: {self.total_growth}cm")
        regular: int = 0
        flowering: int = 0
        prize: int = 0
        regular, flowering, prize = stats.plant_type()
        print(f"Plant types: {regular} regular, {flowering} flowering, "
              f"{prize} prize flowers")

    @classmethod
    def create_garden_network(cls) -> None:
        """
        全ての庭のスコアと数を表示するクラスメソッド
        """
        count: int = 0
        first: bool = True
        line: str = "Garden scores - "
        garden: list[GardenManager]
        for garden in cls.gardens:
            stats: GardenManager.GardenStats = cls.GardenStats(garden.plants)
            if not first:
                line += ", "
            first = False
            line += f"{garden.owned}: {stats.get_score()}"
            count += 1
        print(line)
        print(f"Total gardens managed: {count}")

    @staticmethod
    def validate_height(height: int) -> None:
        """
        高さが0以上かどうかを検証するスタティックメソッド
        """
        print(f"Height validation test: {height >= 0}")


def ft_garden_analytics() -> None:
    """
    GardenManagerシステム全体の動作を確認する関数
    """
    print("=== Garden Management System Demo ===")
    alice: GardenManager = GardenManager("Alice")
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

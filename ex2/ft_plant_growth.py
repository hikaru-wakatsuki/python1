class Plant:
    """
    庭にある植物を表すクラス

        name : 植物の名前
        height : 植物の高さ
        age : 植物の年齢
    """
    def __init__(self, name: str, height: int, age_days: int) -> None:
        """
        Plantクラスのインスタンスを初期化するメソッド
        """
        self.name: str = name
        self.height: int = height
        self.age_days: int = age_days

    def grow(self) -> None:
        """
        植物を成長させるメソッド（高さ +1cm）
        """
        self.height += 1

    def age(self) -> None:
        """
        植物を1日年を取らせるメソッド
        """
        self.age_days += 1

    def get_info(self) -> str:
        """
        植物の現在の情報を文字列で返すメソッド
        """
        return f"{self.name}: {self.height}cm, {self.age_days} days old"


def ft_plant_growth() -> None:
    """
    植物の1週間の成長をシミュレーションする関数
    成長前と成長後の状態、および成長量を表示する
    """
    print("=== Day 1 ===")
    plant: Plant = Plant("Rose", 25, 30)
    print(plant.get_info())
    start_height: int = plant.height
    for _ in range(6):
        plant.age()
        plant.grow()
    print("=== Day 7 ===")
    print(plant.get_info())
    growth: int = plant.height - start_height
    print(f"Growth this week: +{growth}cm")


if __name__ == "__main__":
    ft_plant_growth()

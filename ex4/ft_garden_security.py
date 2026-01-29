class SecurePlant:
    """
    植物データを安全に管理するクラス
    不正な値（負の数）からデータを保護する
    """
    def __init__(self, name: str) -> None:
        """
        SecurePlantのインスタンスを初期化するメソッド
        """
        self.name: str = name
        self._height: int = 0
        self._age: int = 0
        print(f"Plant created: {self.name}")

    def set_height(self, height: int) -> None:
        """
        植物の高さを設定するメソッド
        負の値は拒否される
        """
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self._height = height
            print(f"Height updated: {height}cm [OK]")

    def set_age(self, age: int) -> None:
        """
        植物の年齢を設定するメソッド
        負の値は拒否される
        """
        if age < 0:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self._age = age
            print(f"Age updated: {age} days [OK]")

    def get_height(self) -> int:
        """
        植物の高さを取得するメソッド
        """
        return self._height

    def get_age(self) -> int:
        """
        植物の年齢を取得するメソッド
        """
        return self._age


def ft_garden_security() -> None:
    """
    植物データを安全に管理する仕組みをテストする関数
    """
    print("=== Garden Security System ===")
    plant: SecurePlant = SecurePlant("Rose")
    plant.set_height(25)
    plant.set_age(30)
    print()
    plant.set_height(-5)
    print()
    plant.set_age(-5)
    print()
    print(f"Current plant: {plant.name} "
          f"({plant.get_height()}cm, {plant.get_age()} days)")


if __name__ == "__main__":
    ft_garden_security()

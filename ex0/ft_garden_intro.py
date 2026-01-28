def ft_garden_intro():
    """
    庭にある植物の基本情報を表示する関数
    植物の名前・高さ・年齢を画面に出力する
    """
    name = "Rose"
    height = 25
    age = 30

    print("=== Welcome to My Garden ===")
    print(f"Plant: {name}")
    print(f"Height: {height}cm")
    print(f"Age: {age} age")
    print()
    print("=== End of Program ===")


if __name__ == "__main__":
    ft_garden_intro()

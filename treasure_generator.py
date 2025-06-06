diff --git a//dev/null b/treasure_generator.py
index 0000000000000000000000000000000000000000..56cf8ad24832dea9d52d738f7149cd64b8c7977e 100644
--- a//dev/null
+++ b/treasure_generator.py
@@ -0,0 +1,107 @@
+import random
+
+BASE_VALUES = [1,5,10,1,5,10,50,100,500,1000,5000,10000,25000,50000,100000,250000,500000,1000000]
+
+MAPS = [
+    "Abandoned Mine",
+    "Forgotten Crypt",
+    "Cursed Forest",
+    "Sunken Temple",
+]
+
+MAGIC_ITEMS = [
+    "Potion of Healing",
+    "Scroll of Fireball",
+    "Ring of Invisibility",
+    "Wand of Lightning",
+    "Sword +1",
+]
+
+MONSTER_TREASURE_TYPES = {
+    "A": "Coins only",
+    "B": "Small hoard, occasional gems",
+    "C": "Large hoard with magic",
+    "D": "Mixed coins and items",
+    "E": "Wealthy hoard with powerful magic",
+}
+
+def roll_map():
+    return random.choice(MAPS)
+
+def roll_magic_item():
+    return random.choice(MAGIC_ITEMS)
+
+def chart_monetary_treasures():
+    amount = random.choice(BASE_VALUES) * random.randint(1, 6)
+    return f"{amount} gp"
+
+def chart_magic_treasures():
+    return roll_magic_item()
+
+def chart_combined_hoards():
+    return f"{chart_monetary_treasures()} and {chart_magic_treasures()}"
+
+def display_monster_treasure_types():
+    for k, v in MONSTER_TREASURE_TYPES.items():
+        print(f"{k}: {v}")
+
+def random_generation_of_all():
+    print("Map:", roll_map())
+    print("Magic Item:", roll_magic_item())
+    print("Treasure:", chart_monetary_treasures())
+
+def selective_treasure_chart_generation():
+    print("1) Monetary Treasures")
+    print("2) Magic Treasures")
+    print("3) Combined Hoards")
+    choice = input("Select a number or <ENTER> to go back: ")
+    if choice == "1":
+        print(chart_monetary_treasures())
+    elif choice == "2":
+        print(chart_magic_treasures())
+    elif choice == "3":
+        print(chart_combined_hoards())
+
+def selective_magic_treasure_chart_generation():
+    print("1) Potions")
+    print("2) Scrolls")
+    print("3) Rings")
+    print("4) Rods, Staves & Wands")
+    print("5) Miscellaneous Magics")
+    print("6) Armor & Shields")
+    print("7) Swords")
+    print("8) Miscellaneous Weapons")
+    choice = input("Select a number or <ENTER> to go back: ")
+    if choice:
+        print(roll_magic_item())
+
+def main():
+    while True:
+        print("Random Treasure Determination Generator - v2.0")
+        print("1) Random Generation of All.")
+        print("2) Random Map Generation.")
+        print("3) Random Magic Treasure Generation.")
+        print("4) Selective Treasure Chart Generation.")
+        print("5) Selective Magic Treasure Chart Generation.")
+        print("6) Monster Treasure Type Chart Display.")
+        choice = input("Select a number or <ENTER> to quit: ")
+        if not choice:
+            break
+        if choice == "1":
+            random_generation_of_all()
+        elif choice == "2":
+            print(roll_map())
+        elif choice == "3":
+            print(roll_magic_item())
+        elif choice == "4":
+            selective_treasure_chart_generation()
+        elif choice == "5":
+            selective_magic_treasure_chart_generation()
+        elif choice == "6":
+            display_monster_treasure_types()
+        else:
+            print("Invalid selection")
+        input("Press Enter to continue...")
+
+if __name__ == "__main__":
+    main()

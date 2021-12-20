""" CP1404 Practical Color names
and code function"""

COLOR_CODE = {"Absolute Zero": "#0048ba", "Acid Green": "#b0bf1a", "Amber": "#ffbf00",
              "Aquamarine1": "#7fffd4", "Aquamarine2": "#76eec6", "Aquamarine4": "#458b74",
              "Bisquel": "#ffe4c4", "Beige": "#f5f5dc", "Barn Red": "#7c0a02", "Beaver": "#9f8170"}

name = input("Enter your color name: ")
while name != "":
    print(f" the code for {name} has to be {COLOR_CODE.get(name)}. ")
    name = input("Enter your color name: ")

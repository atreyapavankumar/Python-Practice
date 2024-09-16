x=input("What is the answer to the great question of life ?").strip().lower()
if "42" in x or "forty-two" in x  or "forty two" in x:
    print("Yes")
else:
    print("No")

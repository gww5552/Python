i = 1
guo = 0
while i <= 100:
    if i % 10 == 7 or i % 7 == 0 or i // 10 == 7:
        guo += 1
    i += 1
print(f"一共说了{guo}次过")

while True:
    row = int(input("Rows: "))
    col = int(input("Cols: "))

    if row == 0 or col == 0:
        break

    num = int(input("Number to highlight: "))

    for r in range(1, row + 1):        
        for c in range(1, col + 1):
            product = r * c
            if product == num:
                print(f"[{product}]", end=" ")
            else:
                print(product, end=" ")
        print()   
       

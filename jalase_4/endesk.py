while True:
    try:
        my_list_1 = list(map(int, input("Enter list 1: ").split()))
        my_list_2 = list(map(int, input("Enter list 2: ").split()))
    except ValueError:
        print(".")
        continue
    
    if len(my_list_1) != len(my_list_2):
        print("only Space.")
        continue
    
    sum_list = list(map(lambda x, y: x + y, my_list_1, my_list_2))
    print(f"New list:\n{sum_list}")
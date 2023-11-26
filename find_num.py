def find_num():
    rows = ["4567", "2367", "1357"]
    binary_num = ""

    for row in rows:
        response = input(f"你想的數字是否有在 {', '.join(row)} 中? (回答 Y/N): ")
        binary_num += '1' if response.lower() == 'y' else '0'
    
    return f"你想的數字是 {int(binary_num, 2)}"

print(find_num())

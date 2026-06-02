parking_lot = []
next_id = 1

while True:
    print("""==========================================    
        QUẢN LÝ BÃI XE - SMART PARKING
==========================================
1. Thêm xe mới vào bãi 
2. Hiển thị danh sách xe trong bãi 
3. Tìm kiếm xe theo mã (id)
4. Xóa xe khởi bãi (khi xe ra)
5. Thoát chương trình
==========================================""")
    choice = input("Nhập lựa chọn của bạn (1 - 5): ")
    match choice:
        case "1":
            while True: 
                type_input = input("Nhập loại xe: ").strip()
                if type_input.isspace() or type_input == "":
                    print("Lỗi ! Loại xe không được để trống!")
                else: 
                    break
            while True:
                owner_input = input("Nhập tên chủ xe: ").strip()
                if owner_input.isspace() or owner_input == "":
                    print("Lỗi ! Tên chủ xe không được để trống!")
                else:
                    break
            parking_lot.append({
                'id': next_id,
                'type': type_input,
                'owner': owner_input
            })
            print("Đã thêm xe thành công vào bãi gửi!")
            next_id = next_id + 1
        case '2': 
            if parking_lot == []:
                print("Bãi xe hiện đang trống!")
            print("Danh sách xe trong bãi")
            print(f"{'ID':<5} | {'Loại xe':<15} | {'Chủ xe'}")
            print("-"*42)
            for car in parking_lot :
                print(f"{car['id']:<5} | {car['type']:<15} | {car['owner']}")
            print("-"*42)
        case '3':
            search_id = int(input("Nhập id xe cần tìm kiếm: "))
            found = False 
            for car in parking_lot:
                if car['id'] == search_id:
                    print("Thông tin chi tiết của xe cần tìm: ")
                    print("-"*42)
                    print(f"{car['id']:<5} | {car['type']:<15} | {car['owner']}")
                    found = True
            if found == False:
                print("Không tìm thấy xe")
        case '4':
            delete_id = int(input("Nhập id xe cần xóa: "))
            found = False 
            for car in parking_lot:
                if car['id'] == delete_id:
                    parking_lot.remove(car)
                    print(f"Đã xóa xe ID {car['id']} thành công!")
                    found = True
            if found == False:
                print("Không tìm thấy xe để xóa!")
        case "5":
            print("Thoát chương trình")
            break
        case _:
            print("Lựa chọn không hợp lệ! Vui lòng chọn từ 1 - 5")

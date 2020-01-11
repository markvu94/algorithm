1. cho 1 số tự nhiên, tính tổng các chữ số của số này (ví dụ: 1234 có tổng các chữ số là 10)

2. cho 1 số n, tính tổng n số tự nhiên đầu tiên (ví dụ n = 4 -> result = 1 + 2 + 3 + 4 = 10) (yêu cầu dùng đệ quy để giải)

3. cho 1 số n, viết chương trình đổi số này thành dạng nhị phân (ví dụ: 7 = 111, 10 = 1010)

4. bài toán tìm đường ra khỏi mê cung. Cho mê cung như sau, trong đó các ô số 0 là không được đi vào, còn các ô số 1 là được đi vào:
maze = [ [1, 0, 0, 0], 
         [1, 1, 0, 1], 
         [0, 1, 0, 0], 
         [1, 1, 1, 1] ]
    Bạn khởi đầu ở ô đầu tiên góc trên trái và cần tìm cửa ra ở ô góc dưới cùng bên phải. In ra màn hình solution hiển thị đường đi ra khỏi mê cung

5. cho trục tọa độ Oxy, cho tọa độ điểm khởi đầu (sx, sy) và tọa độ điểm đích (dx, dy). Viết chương trình kiểm tra xem có thể đi từ điểm khởi đầu tới điểm kết thúc được không (return True hoặc False), biết rằng tại mỗi điểm (x,y) bất kì, chỉ có thể di chuyển theo 1 trong 2 cách (x, x + y) hoặc (x + y, y)

6. Cho 2 số tự nhiên x và n, tìm số cách mà x có thể biểu diễn bằng tổng các số tự nhiên khác nhau mũ n.
    ví dụ: x = 10, n = 2 -> result = 1 (10 = 1^2 + 3^2)
           x = 100, n = 2 -> result = 3 (100 = 10^2 hoặc 100 = 6^2 + 8^2 hoặc 100 = 1^2 + 3^2 + 4^2 + 5^2 + 7^2)

7. cho trục số tự nhiên từ -infinity tới +infinity và số tự nhiên n. Bạn bắt đầu từ điểm 0, bạn cần tối thiểu bao nhiêu bước để chạm tới điểm n? Biết rằng bạn có thể di chuyển sang trái hoặc phải tùy ý, với điều kiện mỗi lần di chuyển, bạn lại tăng Step lên 1. 
    ví dụ: để đi từ 0 tới 3 bạn cần tối thiểu 2 bước (cụ thể: (0 -> 1) và (1 -> 3))
           để đi từ 0 tới 4 bạn cần tối thiểu 3 bước (cụ thể: (0 -> -1), (-1 -> 1) (1 -> 4))



 











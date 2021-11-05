# calculator
A simple calculator. Python practice
就是個普通計算機

遇到的問題：
無法驗證數字，本來要做一個while迴圈做數字驗證，
while num1 != float...
但python的input都是string，
num1 = float(input("a"))  # crash
num1 = input("a")
float(num1) # crash
後來乾脆用try去抓問題避免crash :(

name = input("กรอกชื่อผู้สมัคร")
age = int(input("กรอกอายุ"))
height = float(input("กรอกส่วนสูง"))
power = int(input("กรอกค่าพลัง 1-10"))
money = int(input("กรอกเงินที่พกติดตัว"))

if power == 10 and money > 1000 :
    print(name+" ผ่านการคัดเลือก ในตำแหน่ง BIG BOSS")
elif (power >= 8 or money > 800) :
    print(name+" ผ่านการคัดเลือก ในตำแหน่ง BABY BOSS")
elif (power >= 6 or money >= 50) :
    print(name+" ผ่านการคัดเลือก ในตำแหน่ง BODYGUARD")
elif (power >= 4 or money >= 20) :
    print(name+" ผ่านการคัดเลือก ในตำแหน่ง ลูกจ้าง")
elif (money >= 100000) :
    print(name+" is VIP")
else:
    print(name+" ไม่ผ่านการคัดเลือก")
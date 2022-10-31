class Star:
    name = 'Star' #클래스 변수
    x = 100 #클래스 변수
    
    def change():
        x = 200
        print('x is', x)

print('x is', Star.x)
Star.change()

star = Star() #생성자가 없어도 된다?
print(type(star))
print(star.x) #비록 객체 변수로 액세스했으나 같은 이름의 클래스 변수가 우선
#star.change() Star.change(star)와 동일하다
# YounghyunHW
VpythonHomework

##### 문제
어린왕자행성 모델
어린왕자가 사는 행성의 표면중력이 지구중력과 같도록 모델링하고 풀이 과정과 함께 다음의 물음에 답하시오. 
필요하다면 코드를 작성하고 시뮬레이션 하시오.

* 문제를 풀기 위해 필요한 내용들은 인터넷에서 찾아보시면 됩니다.
* 문제 풀이 중 특정한 가정이 필요하거나 특정한 조건이 필요하다고 생각된다면, 가정 또는 조건을 함께 명시하여 작성하시면 됩니다.
* 정확한 어떤 숫자를 정답으로 놓고 있지는 않습니다. 풀이 과정과 결론이 타당하면 됩니다.
* 풀이 과정을 보고 점수를 부여하기 때문에 숫자만 작성하여 제출하면 점수가 부여되지 않습니다.

*제출 시 주의사항
1) 반드시 코드 또는 풀이과정이 있어야 함(코드 제출 필수 아님)
 - 그렇지 않은 경우 해당 문제는 0점
2) 코드를 제출할 경우 반드시 에러 없이 실행되는 전체 코드를 제출할 것
3) 반드시 한글파일/워드파일/텍스트파일로만 제출할 것

(1) 어린왕자행성의 크기를 인터넷에서 찾아서 추정하고 표면중력이 지구중력과 같으려면 행성이 질량이 어느 정도이어야 하는가?
(2) 어린왕자의 키가 대략 1m일 때, 발에 작용하는 중력가속도와 머리에 작용하는 중력가속 도의 차이는 어떻게 되는가?
(3) 어린왕자행성에서 어린왕자가 탈출하려면 속력은 얼마 이상이어야 하는가?
(4) 탈출하지 못하고 계속 원 궤도를 도는 속도는 얼마인가?



##### 교수님 코멘트
물리현상을 위한 도구로서의 언어를 선택하는 것이기 때문에 가능하면 프로그래밍언어를
쉬운 것으로 택하려고 합니다. 그래서 제가 택한 것은 뭐냐면,
Python 기반의 V Python, 그리고 GlowScript를 선택했습니다.
배우기가 쉽고요. 그리고 사용하기 쉬운 Python 언어 기반으로 되어 있고요. 그리고 무료입니다.
오픈소스이기도 하고요.
그리고 제가 V Python, 그리고 GlowScript라는 말을 다시 붙인 이유는 뭐냐면
GlowScript라는 것은 그런 Python 언어 기반으로 되어 있는 것을 웹브라우저에서 코딩하고 실행이 가능한 형태로 만들어 놓은 것을 말합니다.
그래서, 저의 모든 물리 코딩하는 부분에 있어서는 다 GlowScript를 사용할 것입니다.
그리고, 'GlowScript' , 'V Python' 은
직관적으로 삼차원 물체를 생성할 수도 있고 , 그리고 그것을 아주 간단하게 실시간 애니메이션으로 표현으로 가능합니다.



##### 프로그램 실행과정
glowscript.org 접속
sign in 로그인하기
허용클릭
ok 클릭
here 클릭
private 폴더에서 Create New Program 클릭
prince 입력 후 확인클릭
파일 export 혹은 아래의 코드입력 후 Run this program 클릭



##### 프로그램 코드 #시작
GlowScript 3.0 VPython

# 어린왕자의 별
star = sphere(pos=vector(0,0,0), radius = 3,color=color.yellow, texture=textures.earth)
star.v = vector(0,0,0)

# 어린왕자
prince = sphere(pos=vector(4,0,0),radius=0.5,color=color.blue, make_trail=True)
prince.mass = 15

# 지구의 질량과 반지름
earth_mass = 5.972e24
earth_radius = 6371000

# 중력상수
G = 6.67e-11

# 중력가속도 ~= 9.8
a = G*earth_mass/(earth_radius**2)

# (1) 어린왕자행성의 크기를 인터넷에서 찾아서 추정하고 표면중력이 지구중력과 같으려면 행성이 질량이 어느 정도이어야 하는가?
star.mass = (a*star.radius**2)/G
print(f'행성의 표면중력이 지구의 중력과 같을때의 행성의 질량 : {star.mass:.3e} kg')

# (2) 어린왕자의 키가 대략 1m일 때, 발에 작용하는 중력가속도와 머리에 작용하는 중력가속도의 차이는 어떻게 되는가?
a_head = G*star.mass/(star.radius+1)**2 # 머리에 작용하는 중력가속도
print(f'발에 작용하는 중력가속도와 머리에 작용하는 중력가속도의 차이 : {a-a_head:.3f} m/s^2')

# (3) 어린왕자행성에서 어린왕자가 탈출하려면 속력은 얼마 이상이어야 하는가?
escape_v = sqrt(2*G*star.mass/star.radius)
print(f'어린왕자행성에서 어린왕자가 탈출할 수 있는 최저 속력 : {escape_v} km/s')

# (4) 탈출하지 못하고 계속 원 궤도를 도는 속도는 얼마인가?
circle_v = sqrt(G*star.mass/star.radius)
print(f'탈출하지 못하고 계속 원 궤도를 도는 속도 : {circle_v} km/s')

# 탈출하지 못하고 원 궤도를 도는 시뮬레이션
prince.v = vector(0,circle_v,0)
star.v = -prince.mass / star.mass * prince.v

t=0
dt=0.01

while t<1000:
    rate(1/dt)
    
    r = prince.pos - star.pos
    F = G*star.mass*prince.mass/mag(r)**2*norm(r)
    
    star.F = F
    prince.F= -F
    
    prince.acc = prince.F/prince.mass
    star.acc = star.F/star.mass
    
    prince.v = prince.v + prince.acc*dt
    prince.pos = prince.pos + prince.v*dt
    
    star.v = star.v + star.acc*dt
    star.pos = star.pos + star.v*dt
    
    t=t+dt
##### 프로그램 코드 #끝


#####
답지는 이렇구
자세한 설명은 영현씨가 추가해서
보고서 이쁘게 작성하면 될거같아요
파일은 알집으로 첨부할께요
고생하세요

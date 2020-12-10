from vpython import *
#GlowScript 3.0 VPython

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
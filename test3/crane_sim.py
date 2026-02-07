import math

def calculate_wire_tension(mass, length):
    # mass: 크레인에 올리는 물체의 질량 (kg)
    # length: 와이어 로프의 길이 (m)
    g = 9.81  # 중력 가속도 (m/s^2)
    tension = mass * g / math.sin(math.atan(length))
    return tension

if __name__ == '__main__':
    mass = 1000  # kg
    length = 10   # m
    print(f"크레인 와이어 로프 장력: {calculate_wire_tension(mass, length)} N")

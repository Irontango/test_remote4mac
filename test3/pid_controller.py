import math

class PIDController:
    def __init__(self, kp, ki, kd):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.error_integral = 0
        self.error_previous = 0

    def update(self, error, dt):
        self.error_integral += error * dt
        derivative = (error - self.error_previous) / dt
        output = self.kp * error + self.ki * self.error_integral + self.kd * derivative
        self.error_previous = error
        return output

class CranePID:
    def __init__(self, pid_controller):
        self.pid_controller = pid_controller

    def update(self, position_error, velocity_error, dt):
        output = self.pid_controller.update(position_error + velocity_error, dt)
        return output

if __name__ == '__main__':
    kp = 10
    ki = 5
    kd = 2
    pid_controller = PIDController(kp, ki, kd)
    crane_pid = CranePID(pid_controller)

    position_error = 1.0
    velocity_error = 0.5
    dt = 0.01

    output = crane_pid.update(position_error, velocity_error, dt)
    print(f"크레인 PID 제어 출력: {output}")

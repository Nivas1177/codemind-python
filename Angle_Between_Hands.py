def calculate_angle(hour,minute):
    h_angle = 0.5 * (hour * 60 + minute)
    m_angle = 6 * minute
    angle = abs(h_angle - m_angle)
    angle = min(angle, 360 - angle)
    return angle
time = input()
hour, minute = map(int, time.split(':'))
x = calculate_angle(hour,minute)
print(x)
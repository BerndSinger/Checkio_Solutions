'''

'''


time ="18:00"

def sun_angle(time):
    time_list=time.split(":")

    if int(time_list[0]) < 0 or int(time_list[0]) > 24:
        return "Invalid time Input"
    elif int(time_list[1]) < 0 or int(time_list[1]) > 59:
        return "Invalid Time Input"

    elif int(time_list[0]) < 6 or int(time_list[0]) > 18:
        return "I dont see the sun!"

    else:
        sun_angle1 = float(15*(int(time_list[0])-6))
        sun_angle2 = float((15 / 60) * int(time_list[1]))
        answer = sun_angle1+sun_angle2

        return answer

print(sun_angle(time))
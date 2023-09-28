#inputs swimming time
swim_mins = int(input("Enter Swimming time (in minutes): "))

#inputs cycling time
cycling_mins = int(input("Enter Cycling time (in minutes): "))

#inputs running time
running_mins = int(input("Enter Running time (in minutes): "))

#inputs total time
total_time = swim_mins + cycling_mins + running_mins

qualifying_time_mins = 100
# determines the award based on the total time vs the qualifying time
if total_time <= qualifying_time_mins:
    print("award: Provincial Colours")


elif total_time <= (qualifying_time_mins + 5):
    print("award: Provincial Half Colours")

elif total_time <= (qualifying_time_mins + 10):
    print("award: Provincial Scroll")

else:
    print("award: No award")
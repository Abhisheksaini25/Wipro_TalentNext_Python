'''
1.	create a python program that asks the user how far they want to travel. if they want to travel less than three miles 
tell them to ride Bicycle. if they want to travel more than three miles, but less than three hundred miles, tell them to 
ride Motor-cycle. if they want to travel three hundred miles or more tell them to driver Super-Car.
Sample Output:
How far would you like to travel in miles? 2500
I suggest Super-Car to your destination
'''

def travel_suggestion():
    distance = float(input("How far would you like to travel in miles? "))
    if distance<3:
        print("I suggest riding a Bicycle to your destination.")
    elif distance<300:
        print("I suggest riding a Motor-cycle to your destination.")
    else:
        print("I suggest driving a Super-Car to your destination.")

'''
2.	Let's assume you are planning to use your python skills to build an App for Mobile.
You decide to host your application on servers running in the cloud. you pick a hosting provider that charges $0.51 per hour. 
you will launch your services using one server and want to know how much it will cost to operate per day, per week, per month.
Write a python program that displays the answers to the following questions:
How much does it cost to operate one server per day?
How much does it cost to operate one server per week?
How much does it cost to operate one server per month?
How much days can I operate one server with $918?
'''

def cloud_server_costs():
    hourly_rate = 0.51
    per_day = hourly_rate*24
    per_week = per_day*7
    per_month = per_day*30
    budget = 969
    operation_days = float(budget / per_day)
    print(f"Cost to operate one server per day: ${per_day}")
    print(f"Cost to operate one server per week: ${per_week}")
    print(f"Cost to operate one server per month: ${per_month}")
    print(f"Days of operation with $918: {operation_days} days") 

cloud_server_costs()
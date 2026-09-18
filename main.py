print("Quadcopter program")

print("5")
print(5)
print("5" + "3")

#this is a comment in python
mass = 1.2   #assign 1.2 to mass
gravity = 9.81  #put 9.81 into gravity
arm_length = 0.25

#x == 5 # check is x equal to 5?
#boolean check for equality

print("Mass:", mass, "kg")
print("Gravity:", gravity, "m/s^2")
print("Arm Length", arm_length , "m")

altitude = 12.5
print(f"Altitude: {altitude} meters")

battery = float(input("Battery Level"))
gps_sat = int (input("GPS Satellites"))
signal = int(input("Signal Strength"))

# batter 60-100  BATTERY GOOD
# battery 30-59 BATTERY LOW
# battery 0-29 LAND IMMEDIATELY

if battery >= 60:
    print("BATTERY GOOD")
elif battery >=30:
    print("battery low")
else:
    print("take off denied")
    
if battery >=30 and gps_sat >=4:
    print("Takeoff Ok")
    
    
# emergency land if batt <15  OR signal is <20
if battery <15 or signal <20:
    print("EMERGENCY  LAND")
    
#loops
for reading in range(1,6):
    print(f'Telemetry reading {reading}')

for a in range(0, 30, 5):
    print(f'altitude: {a}m')
    
for _ in range(5):
    print("hello world")

    
    
    
    
    
    
    
    
    
    
    
    
    












    

    
    
flight_mode = "STABILIZE"

print(f'DRONE STATUS | Altitude: {altitude} | Battery: {battery}% | Mode: {flight_mode} ')

jimmy = input("Give me a number")
jimmy = int(jimmy)


throttle = float(input("Throttle:"))
#print(throttle+throttle)
#float is floating point number - has decimal point
#use float for numbers with decimals please

roll = float(input("Roll: ")) 
pitch = float(input("Pitch: "))
yaw =   float(input("Yaw: "))

print("Throttle:", throttle, "Roll", roll)
#print("Roll: ", roll)
#print("Pitch: ", pitch)
#print("Yaw:", yaw)





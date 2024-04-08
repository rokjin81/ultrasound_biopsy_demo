import cv2
import math
import serial

# Configuration of Serial Port
port = 'COM6'  
baudrate = 9600

# Start Serial Commulnication
ser = serial.Serial(port, baudrate)

# Read Image File
img_src = "69_2.jpg"
img = cv2.imread(img_src)

# Generation of Window
window_name = "Ultrasound Image"
cv2.namedWindow(window_name)

# Initial Variables
angle = 0
prev_line = None

# Draw Line on Image
def draw_line(angle):
    global prev_line, img
 
    angle = float(angle)
    if angle > 89:
        angle = 89
    if angle < 1:
        angle = 1
    angle_radian = math.radians(angle)

    # Calculation of Starting Point and Ending Point within Image Boundary
    remote_center = 60    
    left_x = 88 # left bound of image
    start_point_y = int(8 + (left_x - remote_center) * math.tan(math.pi / 2- angle_radian))
    start_point = (left_x, start_point_y)

    bottom_y = 309 # bottom bound of image
    right_x = 474 # right bound of image

    end_point_x = int(remote_center + (bottom_y - 8) / math.tan(math.pi / 2- angle_radian))
    end_point = (end_point_x, bottom_y)

    if end_point_x > right_x:
        end_point_y = int(8 + (right_x - remote_center) * math.tan(math.pi / 2 - angle_radian))
        end_point = (right_x, end_point_y)

    # Redraw Background Image
    img = cv2.imread(img_src)
    # Draw Guide Line
    cv2.line(img, start_point, end_point, (255, 255, 255), 1, lineType=cv2.LINE_AA)

    prev_line = (start_point, end_point)  # Update New Guide Line
    cv2.imshow(window_name, img)  # Show Image

    return False

cv2.imshow(window_name, img)  # Show Image

while True:
 
    if ser.in_waiting > 0:
        # Read Angle_value
        angle = ser.readline().decode().strip()
        # Draw Line
        draw_line(angle)


     # Exit with Key of 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Terminate Window
cv2.destroyAllWindows()
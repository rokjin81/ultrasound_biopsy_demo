import cv2
import math
import serial

# Configuration of Serial Port
port = 'COM6'  
baudrate = 9600

# Start Serial Commulnication
ser = serial.Serial(port, baudrate)

# Read Image File
img_src = "11_1.jpg"
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
    if angle > 90:
        angle = 90
    if angle < 0:
        angle = 0
    angle_radian = math.radians(angle)

    # Calculation of Starting Point and Ending Point within Image Boundary
    start_point = (395, 8)
    pixel_x = int(395 - 300 * math.tan(angle_radian))
    end_point = (pixel_x, 308)

    if pixel_x < 88:
        pixel_y = int(8 + 307 / math.tan(angle_radian))
        end_point = (88, pixel_y)

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
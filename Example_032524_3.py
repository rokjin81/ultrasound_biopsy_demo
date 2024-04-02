import cv2
import math

# Read Image File
img_src = "11_1.jpg"
img = cv2.imread(img_src)

# Generation of Window
window_name = "Ultrasound Image"
cv2.namedWindow(window_name)

# Initial Variables
angle = 0
prev_line = None

# Event Handler Function of Key Input
def key_callback():
    global angle, prev_line, img

    # Erase Previous Line
    if prev_line is not None:
        cv2.line(img, prev_line[0], prev_line[1], (0, 0, 0), 1)

    # Input Angle under Range
    angle = input("Enter angle: ")

    if angle == "exit":
        return True

    angle = float(angle)
    if angle > 89:
        angle = 89
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
    # Wait Key Input
    key = cv2.waitKey(1) & 0xFF

    # Event Handler of Key Input
    if key_callback():
        break

# Terminate Window
cv2.destroyAllWindows()
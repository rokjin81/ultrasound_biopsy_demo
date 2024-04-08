import cv2

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"Clicked at ({x}, {y})")

# 이미지 파일 경로를 입력하세요.
image_path = "69_2.jpg"

# 이미지 파일을 읽어옵니다.
image = cv2.imread(image_path)

# 이미지를 표시할 창을 생성합니다.
cv2.namedWindow("Image")

# 마우스 클릭 이벤트를 처리할 콜백 함수를 등록합니다.
cv2.setMouseCallback("Image", click_event)

# 이미지를 표시하고 사용자 입력을 대기합니다.
cv2.imshow("Image", image)
cv2.waitKey(0)

# 창을 닫고 프로그램을 종료합니다.
cv2.destroyAllWindows()
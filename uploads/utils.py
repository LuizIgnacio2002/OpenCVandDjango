import cv2

def get_filtered_image(image, action):
    img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    if action == 'NO_FILTER':
        pass
    elif action == 'COLORIZED':
        img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    elif action == 'GRAYSCALE':
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    elif action == 'BLURRED':
        width, height = img.shape[:2]
        if width > 500:
            k = (50, 50)
        elif width > 200 and width <= 500:
            k = (25, 25)
        else:
            k = (10, 10)
        img = cv2.blur(img, k)
    elif action == 'BINARY':
        img = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)[1]
    elif action == 'INVERTED':
        img = cv2.bitwise_not(img)

    return img
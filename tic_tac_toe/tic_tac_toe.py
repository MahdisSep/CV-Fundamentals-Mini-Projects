import cv2
import numpy as np

def check_state(image_path):
    img = cv2.imread(image_path)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  
    _, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)
 

    cell_size = thresh.shape[0] // 3 
    
    board = np.zeros((3, 3), dtype=str)

    for i in range(3):
        for j in range(3):
            cell = thresh[i*cell_size:(i+1)*cell_size, j*cell_size:(j+1)*cell_size]
            
            circles = cv2.HoughCircles(cell, cv2.HOUGH_GRADIENT, dp=1, minDist=cell_size//2, param1=100, param2=30, minRadius=cell_size//4, maxRadius=cell_size//2)

            found_o = False
            if circles is not None:
                circles = np.round(circles[0, :]).astype("int")  
                for (x, y, r) in circles:
                    cv2.circle(cell, (x, y), r, (255, 0, 0), 2)  
                    board[i, j] = 'O'
                    found_o = True
                    break  


            if board[i, j] == '' and not found_o:
                threshold = cell_size // 10  
                min_line_length = cell_size // 2  
                max_line_gap = cell_size // 4  

                lines = cv2.HoughLinesP(cell, 1, np.pi / 180, threshold=threshold, minLineLength=min_line_length, maxLineGap=max_line_gap)
                if lines is not None:
                    line_count = len(lines)
                    # print("yes")
                    if line_count >= 2:
                        for line1 in lines:
                            for line2 in lines:
                                if line1 is not line2:
                                    x1, y1, x2, y2 = line1[0]
                                    x3, y3, x4, y4 = line2[0]

                                    angle1 = np.arctan2(y2 - y1, x2 - x1) * 180 / np.pi
                                    angle2 = np.arctan2(y4 - y3, x4 - x3) * 180 / np.pi
                                    angle_diff = abs(angle1 - angle2)
                                    if 40 <= angle_diff <= 60:  
                                        board[i, j] = 'X'
                                        # print("this is x")
                                        break
                                   

    # for i in range(3):
    #   for j in range(3):
    #     print("this is the board" , board[i,j])

    for row in board:
        if row[0] == row[1] == row[2] and row[0] != '':
            return f"{row[0]} Wins"
    
    for col in range(3):
        if board[0, col] == board[1, col] == board[2, col] and board[0, col] != '':
            return f"{board[0, col]} Wins"
    
    if board[0, 0] == board[1, 1] == board[2, 2] and board[0, 0] != '':
        return f"{board[0, 0]} Wins"
    if board[0, 2] == board[1, 1] == board[2, 0] and board[0, 2] != '':
        return f"{board[0, 2]} Wins"
    
    if np.all(board != ''):
        return "Draw"
    
    return "Ongoing"



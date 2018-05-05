import cv2 as cv
import numpy as np

#image = cv.imread('razmetra2.png')
#image2 = cv.imread('razmetra2.png')

SHOW_MODE = True

def check(img, i, j, mi, mj):
    return (i >= 0 and j >= 0 and i < mi and j < mj and img[i][j][0] == 255 and img[i][j][1] == 0 and img[i][j][2] == 0)


def create_windows(name, pos):
    cv.namedWindow(name, cv.WINDOW_NORMAL)
    cv.resizeWindow(name, 30, 30)
    cv.moveWindow(name, pos[0], pos[1])

all_img = []

def get_result(vali_img, test_img):
    true_pos = false_pos = true_neg = false_neg = neg_all = pos_all = 0

    for i in range(310, len(test_img)):
        for j in range(0, len(test_img[i])):
            real = False
            ans = False
            if int(vali_img[i][j][1]) - int(vali_img[i][j][0]) >= 90 and vali_img[i][j][1] > 160:
                vali_img[i][j] = [255, 255, 255]
                real = True
                pos_all += 1
            else:
                neg_all += 1

            if test_img[i][j][0] == 255 and test_img[i][j][1] == test_img[i][j][2] and test_img[i][j][1] == 0:
                ans = True

            if real and ans:
                true_pos += 1
            elif not real and ans:
                false_neg += 1

    false_pos = pos_all - true_pos
    true_neg = neg_all - false_neg
    print (img_num)
    print ("Positive {0} TruePositive {1} : {2}\% FalsePositive {3}: {4}%".format(pos_all, true_pos, 100 * true_pos / pos_all, false_pos, 100 * false_pos / pos_all))
    print ("Negative {0} TrueNegative {1} : {2}\% FalseNegative {3}: {4}%".format(neg_all, true_neg, 100 * true_neg / neg_all, false_neg, 100 * false_neg / neg_all))
    all_img.append({"n":img_num, "p":pos_all, "n":neg_all, "tpp": 100 * true_pos / pos_all})
    return vali_img

VALIDATE_IMG = "SYNTHIA-SEQS-01-SUMMER/GT/COLOR/Stereo_Right/Omni_F/000{}.png"
TEST_IMG = "SYNTHIA-SEQS-01-SUMMER/RGB/Stereo_Right/Omni_F/000{}.png"
IMG_CNT = 944

for i in range(0, IMG_CNT):
    i = 51
    img_num = '0' * (3 - len(str(i))) + str(i)
    print (TEST_IMG.format(img_num))
    vali_img = cv.imread(VALIDATE_IMG.format(img_num))
    test_img = cv.imread(TEST_IMG.format(img_num))
    start_img = cv.imread(TEST_IMG.format(img_num))
    final_img = cv.imread(TEST_IMG.format(img_num))

    if SHOW_MODE:
        create_windows("before_vali_img", (600, 600))
        create_windows("before_test_img", (900, 600))
        create_windows("test_img_before_erod", (300, 300))
        create_windows("vali_img", (600, 0))
        create_windows("test_img", (200, 0))
        cv.imshow("before_test_img", test_img)
        cv.imshow("before_vali_img", vali_img)
        for i in range(300, 310):
            for j in range(0, len(test_img[i])):
                test_img[i][j] = [0, 255, 255]
                vali_img[i][j] = [0, 255, 255]

    hsv_test_img = cv.cvtColor(test_img, cv.COLOR_BGR2HSV)

    sum_s = all_pt = 0
    for i in range(310, len(test_img)):
        for j in range(0, len(test_img[i])):
            all_pt += 1
            sum_s += hsv_test_img[i][j][1]

    s_md = (sum_s / all_pt)
    print (s_md)
    mid_vl = 30 + (65 - s_md / 2)
    print (mid_vl)

    for i in range(310, len(test_img)):
        for j in range(0, len(test_img[i])):
            wt_cl = 110
            if (hsv_test_img[i][j][1] <= mid_vl and hsv_test_img[i][j][2] > 40
                and test_img[i][j][0] > wt_cl and test_img[i][j][1] > wt_cl and test_img[i][j][1] > wt_cl):
                test_img[i][j] = [255, 0, 0]

    erode_img = cv.erode(test_img, np.ones((5, 5)))
    hsv_test_img = cv.cvtColor(erode_img, cv.COLOR_BGR2HSV)
    if SHOW_MODE:
        cv.imshow("test_img_before_erod", test_img)

    for i in range(310, len(start_img)):
        for j in range(0, len(start_img[i])):
            if hsv_test_img[i][j][0] > 110 and hsv_test_img[i][j][0] < 130:
                start_img[i][j] = [255, 0, 0]
    vali_img = get_result(vali_img, start_img)

    if SHOW_MODE:
        cv.imshow("vali_img", erode_img)
        cv.imshow("test_img", start_img)
        cv.imshow("vali_img1", vali_img)

        if cv.waitKey():
            break
        cv.destroyAllWindows()

all_img.sort(key=lambda x: x['tpp'])
print (all_img)

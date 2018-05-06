import cv2 as cv
import numpy as np


class WhiteImage():

    def __init__(self, test_image):
        self.test_image = test_image
        self.N = len(test_image)
        self.M = len(test_image[0])
        self.HOR = int(self.N * 0.45)
        self.parts_cnt = 1
        self.parts_n = (self.N - self.HOR) // self.parts_cnt
        self.parts_m = self.M // self.parts_cnt
        self._process_image()

    def _create_windows(self, name, pos):
        cv.namedWindow(name, cv.WINDOW_NORMAL)
        cv.resizeWindow(name, 30, 30)
        cv.moveWindow(name, pos[0], pos[1])

    def _process_image(self):
        self.hsv_test_img = cv.cvtColor(self.test_image, cv.COLOR_BGR2HSV)
        self.white_spots = np.zeros((self.N, self.M))

        for i in range(0, self.parts_cnt):
            for j in range(0, self.parts_cnt):
                l_i = self.HOR + i * self.parts_n
                r_i = min(self.HOR + (i + 1) * self.parts_n, self.N)
                l_j = (j * self.parts_m)
                r_j = min((j + 1) * self.parts_m, self.M)

                sum_s = all_pt = 0
                for x in range(l_i, r_i):
                    for y in range(l_j, r_j):
                        all_pt += 1
                        sum_s += self.hsv_test_img[x][y][1]
                mid_vl = max(40, (sum_s / all_pt) - 13)

                for x in range(l_i, r_i):
                    for y in range(l_j, r_j):
                        if self.hsv_test_img[x][y][1] <= mid_vl
                        and self.hsv_test_img[x][y][2] > 90:
                            self.white_spots[x][y] = 1
                        else:
                            self.white_spots[x][y] = 0

        # clear image
        self.erode_img = cv.erode(self.white_spots, np.ones((5, 5)))
        self.dilate_img = cv.dilate(self.erode_img, np.ones((15, 15)))
        self.result_image = cv.erode(self.dilate_img, np.ones((3, 3)))

    def get_result(self, vali_img, need_print=False):
        true_pos = false_pos = true_neg = false_neg = neg_all = pos_all = 0
        self.vali_img = vali_img

        for i in range(self.HOR, self.N):
            for j in range(0, self.M):
                ans = True if self.result_image[i][j] == 1 else False
                real = False
                if int(vali_img[i][j][1]) - int(vali_img[i][j][0]) >= 90
                and vali_img[i][j][1] > 160:
                    vali_img[i][j] = [255, 255, 255]
                    real = True
                    pos_all += 1
                else:
                    neg_all += 1

                if real and ans:
                    true_pos += 1
                elif not real and ans:
                    false_neg += 1

        false_pos = pos_all - true_pos
        true_neg = neg_all - false_neg
        if need_print:
            print ("Pos {0} TP {1} : {2}% FP {3}: {4}%".format(
                pos_all,
                true_pos,
                100 * true_pos / pos_all,
                false_pos,
                100 * false_pos / pos_all
            ))
            print ("Neg {0} TN {1} : {2}% FNe {3}: {4}%".format(
                neg_all,
                true_neg,
                100 * true_neg / neg_all,
                false_neg,
                100 * false_neg / neg_all
            ))
        return (100 * true_pos / pos_all, 100 * false_neg / neg_all)

    def show_res_images(self):
        self._create_windows("default_image", (0, 0))
        self._create_windows("validation_image", (100, 100))
        self._create_windows("final_image", (300, 300))
        cv.imshow("default_image", self.test_image)

        for i in range(self.HOR - 10, self.HOR):
            for j in range(0, self.M):
                self.test_image[i][j] = [0, 255, 255]

        for i in range(self.HOR, self.N):
            for j in range(0, self.M):
                if self.result_image[i][j] == 1:
                    self.test_image[i][j] = [255, 255, 255]

        cv.imshow("validation_image", self.vali_img)
        cv.imshow("final_image", self.test_image)

        if cv.waitKey():
            cv.destroyAllWindows()


def main():
    VAL_IMG = "SYNTHIA-SEQS-01-SUMMER/GT/COLOR/Stereo_Right/Omni_F/000{}.png"
    TEST_IMG = "SYNTHIA-SEQS-01-SUMMER/RGB/Stereo_Right/Omni_F/000{}.png"
    IMG_CNT = 944

    for i in range(0, IMG_CNT):
        img_num = '0' * (3 - len(str(i))) + str(i)
        print (TEST_IMG.format(img_num))
        vali_img = cv.imread(VALIDATE_IMG.format(img_num))
        test_img = cv.imread(TEST_IMG.format(img_num))
        mat = WhiteImage(test_img)
        mat.get_result(vali_img, True)
        # mat.show_res_images()

if __name__ == "__main__":
    main()

import cv2
import logging
import argparse
import ast

logging.basicConfig(level=logging.DEBUG, format='%(asctime)-15s [%(levelname)s] %(message)s')

def main(
		indicesToTest):
	logging.info("find_usb_cameras.main()")
	
	capture = None
	valid_camera_indices = []
	for cameraID in indicesToTest:
		logging.debug(f"cameraID: {cameraID}")
		capture = cv2.VideoCapture(cameraID)
		capture_is_open = capture.isOpened()
		logging.debug(f"capture_is_open = {capture_is_open}")
		if capture_is_open:
			valid_camera_indices.append(cameraID)
	
	logging.debug(f"valid_camera_indices = {valid_camera_indices}")
	return valid_camera_indices
	
	
if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('--indicesToTest', help="The list of indices to test for a USB camera. Default: '[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]'", default='[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]')
	
	args = parser.parse_args()
	indicesToTest = ast.literal_eval(args.indicesToTest)
	
	main(indicesToTest)

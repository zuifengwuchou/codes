# coding=utf-8
from functools import cmp_to_key

def sortby_jsonfile(fname1, fname2):
    page1 = fname1[:-5].split('-')[-1].split('_')
    page2 = fname2[:-5].split('-')[-1].split('_')
    sort1 = int(page1[0])*100+int(page1[1])
    sort2 = int(page2[0])*100+int(page2[1])
    if sort1 > sort2:
        return 1
    elif sort1 < sort2:
        return -1
    else:
        return 0
		

if __name__ == "__main__":
    test_data = ['back_ocr_f94f5f98-6a57-11e9-a548-707781a2120c-0_0.json',
    'back_ocr_f94f5f98-6a57-11e9-a548-707781a2120c-0_1.json',
    'back_ocr_f94f5f98-6a57-11e9-a548-707781a2120c-0_10.json',
    'back_ocr_f94f5f98-6a57-11e9-a548-707781a2120c-0_11.json',
    'back_ocr_f94f5f98-6a57-11e9-a548-707781a2120c-0_12.json',
    'back_ocr_f94f5f98-6a57-11e9-a548-707781a2120c-0_2.json',
    'back_ocr_f94f5f98-6a57-11e9-a548-707781a2120c-0_3.json',
    'back_ocr_f94f5f98-6a57-11e9-a548-707781a2120c-0_4.json',
    'back_ocr_f94f5f98-6a57-11e9-a548-707781a2120c-0_5.json',
    'back_ocr_f94f5f98-6a57-11e9-a548-707781a2120c-0_6.json',
    'back_ocr_f94f5f98-6a57-11e9-a548-707781a2120c-0_7.json',
    'back_ocr_f94f5f98-6a57-11e9-a548-707781a2120c-0_8.json',
    'back_ocr_f94f5f98-6a57-11e9-a548-707781a2120c-0_9.json',
    'back_ocr_f94f5f98-6a57-11e9-a548-707781a2120c-1_0.json',
    'back_ocr_f94f5f98-6a57-11e9-a548-707781a2120c-1_1.json',
    'back_ocr_f94f5f98-6a57-11e9-a548-707781a2120c-1_2.json',
    'back_ocr_f94f5f98-6a57-11e9-a548-707781a2120c-1_3.json',
    'back_ocr_f94f5f98-6a57-11e9-a548-707781a2120c-1_4.json',
    'back_ocr_f94f5f98-6a57-11e9-a548-707781a2120c-1_5.json',
    'back_ocr_f94f5f98-6a57-11e9-a548-707781a2120c-1_6.json',
    'back_ocr_f94f5f98-6a57-11e9-a548-707781a2120c-2_0.json',
    'back_ocr_f94f5f98-6a57-11e9-a548-707781a2120c-2_1.json',
    'back_ocr_f94f5f98-6a57-11e9-a548-707781a2120c-2_2.json',
    'back_ocr_f94f5f98-6a57-11e9-a548-707781a2120c-2_3.json',
    'back_ocr_f94f5f98-6a57-11e9-a548-707781a2120c-2_4.json',
    'back_ocr_f94f5f98-6a57-11e9-a548-707781a2120c-2_5.json',
    'back_ocr_f94f5f98-6a57-11e9-a548-707781a2120c-3_0.json',
    'back_ocr_f94f5f98-6a57-11e9-a548-707781a2120c-3_1.json',
    'back_ocr_f94f5f98-6a57-11e9-a548-707781a2120c-3_2.json',
    'back_ocr_f94f5f98-6a57-11e9-a548-707781a2120c-3_3.json',
    'back_ocr_f94f5f98-6a57-11e9-a548-707781a2120c-3_4.json',
    'back_ocr_f94f5f98-6a57-11e9-a548-707781a2120c-4_0.json',
    'back_ocr_f94f5f98-6a57-11e9-a548-707781a2120c-4_1.json',
    'back_ocr_f94f5f98-6a57-11e9-a548-707781a2120c-4_2.json',
    'back_ocr_f94f5f98-6a57-11e9-a548-707781a2120c-4_3.json',
    'back_ocr_f94f5f98-6a57-11e9-a548-707781a2120c-4_4.json',
    'back_ocr_f94f5f98-6a57-11e9-a548-707781a2120c-4_5.json']

    test_data = sorted(test_data, key=cmp_to_key(sortby_jsonfile))

    print(test_data)
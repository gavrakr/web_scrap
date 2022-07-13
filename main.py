from SuperBrand import b_company
from get_jobs import jobs
import csv


dic = b_company()
items_list = dic.items()
fail_list = ["iCOOP", "유니클로", "쉐이크쉑", "에잇세컨즈", "지오다노", "(주)에이비씨마트코리아"]


for name, x in items_list:
    if name in fail_list:
        continue
    else:
        file = open(f"{name}.csv", mode="w")
        writer = csv.writer(file)
        writer.writerow(["근무지", "회사명", "근무시간", "급여", "등록일"])
        for i in jobs(x):
           i = i.split(" ")
           i = filter(None, i)
           writer.writerow(i)

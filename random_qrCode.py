import datetime
import uuid
import qrGenerator
import DBHelper as db

sqlInsert = "INSERT INTO public.generated_qr (id, qr_code, create_date_time, expired_date_time, used_date_time, printed_date_time, is_printed, is_active, score) VALUES ({}, '{}', '2021-08-11 09:16:29.000000', '2025-07-17 09:16:29.000000', null, '2021-08-01 08:38:00.000000', true, true, {});"
dbHelper = db.DbHelper()
dbHelper.cursor()


def init(prefix):
    f = open("result/"+prefix+'_qrCodeFinal.csv', 'w')
    print(datetime.datetime.now(datetime.timezone.utc).astimezone())

    f.write("id,qr_code,create_date_time,expired_date_time,is_active,score\n")
    arrayQr = []

    start = 178
    finish = 180
    fileName = ""

    for x in range(start, finish):
        uuidValue = str(uuid.uuid4())
        uuidValue = prefix+"-"+uuidValue
        score = "0"
        if(prefix == 'pk1'):
            score = "10"
        else:
            score = "5"

        f.write("{},{},{},{},{},{}\n".format(str(x), uuidValue,
                                             "2021-07-18T09:16:29", "2023-07-17T09:16:29", "1", score))
        arrayQr.append([uuidValue, x])
        dbHelper.insert(sqlInsert.format(x, uuidValue, score))

        if x % 48 == 0:
            fileName = str(start) + "-" + str(finish)
            start = x+1
            finish = x + 48
            print(fileName)
            print(arrayQr)
            qrGenerator.generateImageArray(
                prefix+"-"+fileName, arrayQr, score)
            arrayQr = []

    if(len(arrayQr) < 48):
        fileName = str(start) + "-" + str(x)
        print(fileName)
        print(arrayQr)
        qrGenerator.generateImageArray(prefix+"-"+fileName, arrayQr, score)

    f.close()
    dbHelper.close()


init('pk1')


# f = open('qrCodeFinal.csv', 'w')
# print(datetime.datetime.now(datetime.timezone.utc).astimezone())

# f.write("id,qr_code,create_date_time,expired_date_time,is_active,score\n")

# for x in range(1, 48):
#     uuidValue = str(uuid.uuid4())
#     if x > 50000:
#         uuidValue = "pk1-"+uuidValue
#     else:
#         uuidValue = "pk5-"+uuidValue
#     qrGenerator.generateImage(uuidValue)
#     f.write("{},{},{},{},{},{}\n".format(str(x), uuidValue,
#                                          "2021-07-18T09:16:29", "2023-07-17T09:16:29", "1", "10"))
# f.close()

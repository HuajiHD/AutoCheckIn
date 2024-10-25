import requests

false = False
true = True

#填写自己的authorization
authorization = ''

userdata = {
  "Id": 0,
  "ThreadId": "139542734",
  "Signature": "滑只因",
  "RecordValues": [
    {
      "FieldId": 1,
      "Values": [
        "{\"latitude\":36.172134,\"longitude\":120.507643}"
      ],
      "Texts": [
        "青岛市崂山区•中国海洋大学(崂山校区)本科生宿舍"
      ],
      "Scores": [],
      "Files": [],
      "MatrixValues": [],
      "CustomTableValues": [],
      "FillInMatrixFieldValues": [],
      "MatrixFormValues": [],
      "HasValue": true
    }
  ],
  "DateTarget": "",
  "IsNeedManualAudit": false,
  "MinuteTarget": -1,
  "IsNameNumberComfirm": false
}

def checkIn(url):
    try:
        # set headers
        headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
            'Content-Type': 'application/json',
            'Connection': 'keep-alive',
            'Host': 'h-api.jielong.co',
            'Authorization': authorization
        }

        # set data
        data = userdata

        r = requests.post(url=url, headers=headers, json=data)
        # print(r.json())
        #sendEmail('Success', r.json()['Data'])
        print("check in successfully!\n1.1测试版")

    except:
        print("Error! check in failed!")


def main():
    url = 'https://b-api.jielong.co/api/CheckIn/EditRecord'
    checkIn(url)


if __name__ == '__main__':
    main()

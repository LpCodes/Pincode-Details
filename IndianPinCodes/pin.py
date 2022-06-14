import requests


def getpin(pincode):
    try:
        print("Please wait fetching details\n")
        response = requests.get(f"https://api.postalpincode.in/pincode/{pincode}")

        data = response.json()
        if data[0]["Message"] == "No records found":
            print(f"Sorry No data was found for the PINCODE ->  {pincode} provided\n")
        else:
            for key, value in data[0].items():
                d = value[-1]
                if type(d) is dict:
                    # print(d)
                    print(f"Info for Pincode {d['Pincode']} is as follows \n\nName --> "
                          f"{d['Name']}\n\nRegion --> {d['Region']}\n\nDistrict --> {d['District']}\n\nDivision "
                          f"--> "
                          f""f"{d['Division']}\n\nRegion --> {d['Region']}\n\nBlock --> {d['Block']}\n\nCircle "
                          f"--> {d['Circle']}\n\nState --> {d['State']}\n",
                          )
    except Exception as e:
        print(f"An error has occurred {e}")


# getpin(110001)

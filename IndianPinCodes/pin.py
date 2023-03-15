import requests


def getpin(pincode):
    """
        Fetches details of a pincode provided
        and prints the information to the console.

        Args:
            pincode (int): The 6-digit pincode to fetch details for.

        Returns:
            None: The function does not return anything, it just prints the details to the console.

        Raises:
            None: The function does not raise any exceptions, it handles them internally.

        """
    if not str(pincode).isdigit() or len(str(pincode)) != 6:
        print("Please enter a valid 6-digit pincode")
        return

    print("Please wait while fetching details...\n")
    try:
        response = requests.get(f"https://api.postalpincode.in/pincode/{pincode}")
        data = response.json()[0]
        if data["Status"] == "Success":
            d = next((x for x in data["PostOffice"] if isinstance(x, dict)), None)
            if d:
                print(f"Info for Pincode {d['Pincode']} is as follows:\n"
                      f"Name --> {d['Name']}\n"
                      f"Region --> {d['Region']}\n"
                      f"District --> {d['District']}\n"
                      f"Division --> {d['Division']}\n"
                      f"Block --> {d['Block']}\n"
                      f"Circle --> {d['Circle']}\n"
                      f"State --> {d['State']}\n"
                      )
            else:
                print(f"Sorry, no data was found for the PINCODE {pincode} provided.\n")
        else:
            print(f"An error occurred while fetching data: {data['Message']}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while making the API request: {e}")

# class DataManager:
#     # This class is responsible for talking to the Google Sheet.
#     def send_flight_to_sheet(self):
#
#         exercises = send_to_exercise_api(query)["exercises"]
#         for exercise in exercises:
#             params = {
#                 "workout": {
#                     "date": datetime.date.today().strftime("%d/%m/%Y"),
#                     "time": datetime.datetime.now().strftime("%X"),
#                     "exercise": exercise["user_input"].title(),
#                     "duration": exercise["duration_min"],
#                     "calories": exercise["nf_calories"],
#                 }
#             }
#             header = {
#                 "Authorization": f"Bearer {SHEET_KEY}"
#             }
#             response = requests.post(url=SHEET_URL, json=params, headers=header)
#             print(response.status_code)

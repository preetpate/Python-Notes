# import subprocess

# profiles = subprocess.check_output(
#     "netsh wlan show profiles",
#     shell=True,
#     text=True,
#     encoding="utf-8",
#     errors="ignore"
# )

# print(profiles)


# import subprocess

# wifi_name = input("Enter Wi-Fi Name: ")

# result = subprocess.check_output(
#     f'netsh wlan show profile name="{wifi_name}" key=clear',
#     shell=True,
#     text=True,
#     encoding="utf-8",
#     errors="ignore"
# )

# print(result)


# import subprocess

# wifi_name = input("Enter Wi-Fi Name: ")

# result = subprocess.check_output(
#     f'netsh wlan show profile name="{wifi_name}" key=clear',
#     shell=True,
#     text=True,
#     encoding="utf-8",
#     errors="ignore"
# )

# for line in result.splitlines():
#     if "Key Content" in line:
#         print("Password:", line.split(":")[1].strip())
#         break
# else:
#     print("Password not found.")


# import subprocess

# def get_wifi_profiles():
#     try :
#         output = subprocess.check_output(['netsh','wlan','show','profiles'], text = True)

#         profiles = []
#         for line in output.split('\n'):
#             if "All User Profile" in line:
#                 profile = line.split(":")[1].strip()
#                 profiles.append(profile)

#         wifi_data = []
#         for profile in profiles:
#             try :
#                 profile_info = subprocess.check_output(['netsh','wlan','show','profiles'], text = True)
#                 for line in profile_info.split("\n"):
#                     if "Key Content" in line:
#                         password = line.split(":")[1].strip()
#                         wifi_data.append((profile, password))
#                         break
#                 else :
#                     wifi_data.append((profile, "No password found"))
#             except subprocess.CalledProcessError:
#                 wifi_data.append((profile, "Error retrieving password"))
#         return wifi_data
#     except subprocess.CalledProcessError as e:
#         print("Error fetching wi-fi profile:", e)
#         return []
    
# wifi_profiles = get_wifi_profiles()
# if wifi_profiles:
#     print(f"{'Wi-fi Name' : <30}{'Password' : <30}")
#     print("="*60)
#     for name, password in wifi_profiles:
#         print(f"{name: <30}{password : <30}")
# else :
#     print("No wi-fi profile found")
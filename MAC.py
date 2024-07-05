import random
import subprocess

def MAC_generator():
    numbers = [1,2,3,4,5,6,7,8,9]
    alphabets = ['A','B','C','D','E','F']
    first_house_num = numbers[random.randint(0, 8)]
    first_house_wrd = alphabets[random.randint(0, 5)]
    second_house_num = numbers[random.randint(0, 8)]
    second_house_wrd = alphabets[random.randint(0, 5)]
    third_house_num = numbers[random.randint(0, 8)]
    third_house_wrd = alphabets[random.randint(0, 5)]
    fourth_house_num = numbers[random.randint(0, 8)]
    fourth_house_wrd = alphabets[random.randint(0, 5)]
    fifth_house_num = numbers[random.randint(0, 8)]
    fifth_house_wrd = alphabets[random.randint(0, 5  )]
    return f"00:{first_house_num}{first_house_wrd}:{second_house_num}{second_house_wrd}:{third_house_num}{third_house_wrd}:{fourth_house_num}{fourth_house_wrd}:{fifth_house_num}{fifth_house_wrd}"

MAC = MAC_generator()
print(MAC)

subprocess.call("ifconfig eth0 down", shell=True)
subprocess.call("ifconfig eth0 hw ether " + MAC, shell=True)
subprocess.call("ifconfig up", shell=True)

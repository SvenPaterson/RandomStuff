import random
import time
from datetime import datetime

# discussion with Eric at work, can you compute the average of a list of numbers
# forever without storing the list of numbers? 
# Answer below is yes, but the calculation is limited by how big n can get
# given memory and calculation limitations. unsigned long will let you calculate
# average for 250million years at a sample rate of 1 second.

def random_num():
    return round(random.randint(1,100)/random.randint(1,10), 2)

def new_avg_method(prev_avg, new_num, start_time, sample_rate):
    new_num_time = datetime.now()
    n = (new_num_time - start_time).seconds / sample_rate
    return round((prev_avg * (n - 1) + new_num) / n, 3)


def main():
    _list = []
    start_time = datetime.now()
    sample_rate = 1

    num = random_num()
    new_avg = num
    trad_avg = num
    i = 0
    while i < 10:
        
        time.sleep(sample_rate)

        num = random_num() # new number
        _list.append(num) # stored big list of numbers

        trad_avg = round(sum(_list) / len(_list), 3) # takes big list of numbers and calculates average

        # takes previous average and new number and calculates average
        # based on the time since start of program and known sample rate
        new_avg = new_avg_method(new_avg, num, start_time, sample_rate) 
        
        print(f'list: {_list}')
        print(f'trad_avg: {trad_avg}')
        print(f'new_avg: {new_avg}')
        print('-----------------')
        
        i += 1




if __name__ == '__main__':
    main()
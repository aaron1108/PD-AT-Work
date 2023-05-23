import sys

class month_search:

    def __init__(self, month, char, num):
        self.month = month
        self.char = char
        self.num = num

    def char_search(self):
        month_len = len(self.month)
        list = []

        for i in range(month_len):

            if self.char == self.month[i][0][self.num-1:self.num]:
                
                list.append(self.month[i])

        return list
    
    def get_disc():


        return dict_temp


if __name__ == '__main__':

    dict_temp = {}

    file = open('dict.txt','r', encoding="utf-8")

    for line in file.readlines():
        line = line.strip()
        k = line.split(' ')[0]
        v = line.split(' ')[1]
        dict_temp[k] = v

    file.close()

    month = dict_temp

    for num in range(1, 4):
        
        char = input(f"請輸入第{num}個英文\n").lower()

        if not char.isalpha():
            print('請輸入英文')
            sys.exit()

        result = month_search(month, char, num).char_search()

        if len(result) == 1:
            print(result[0][1])
            sys.exit()

        else:
            num += 1
            month = result

    print('沒有符合的月份')

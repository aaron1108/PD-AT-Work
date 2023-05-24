import sys

class month_filter:

    @staticmethod
    def search_process(month, char, num):

        my_dict = {}

        if not char.isalpha():

            print('請輸入英文')
            sys.exit()
        
        for key, value in month.items():

            if char == format(key)[num - 1:num]:

                my_dict[format(key)] = format(value)

        return my_dict

    def search_condtion(self, month):

        for num in range(1, 4):

            char = input(f"請輸入第{num}個英文\n").lower()

            result = self.search_process(month, char, num)

            if len(result) == 1:

                print(list(result.values())[0])

                sys.exit()

            else:
                month = result

        print('輸入英文沒有符合的月份')

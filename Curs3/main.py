# import random
#
#
# # for i in range(10):
# #     print(f'Set instructiuni {i + 1}')
#
#
# # random_choise = random.choice([i for i in range(10) if i % 3 == 0])
# # print (random_choise)
# #
# # while True:
# #     random_choice = random.choice([i for i in range(10)])
# #     if random_choice % 3 == 0:
# #         break
# #     print(f'random choice is {random_choice}')
# #
# # for i in range(10):
# #     if i % 2 != 0:
# #         continue
# #     print(f'Numar par {i} ')
#
#
# def get_sum(a, b):
#     return a + b
#
#
# my_sum = get_sum(2, 5)
# print(my_sum)


# def my_function(param_1, param_2):
#     print('param_1' , param_1)
#     print('param_2' , param_2)
#
#
# my_function(2, 3)

#
# def my_function(param_1, param_2, param_3 = 3, param_4 = 4):
#     print('param_1' , param_1)
#     print('param_2' , param_2)
#     print('param_3' , param_3)
#     print('param_4' , param_4)
#
#
# my_function(2, 3, -9, -10)
# my_function(2, 3, param_4=-9, -10) #nu merge in mijloc parametrii de tip key-word(cheie valoare)

#
# def my_function(param_1, param_2, *args):
#     print('param_1' , param_1)
#     print('param_2' , param_2)
#
#     for arg in args:
#         print(arg)
#
#
# my_function(1,2,3,4,None,'jijel')

#
# def my_function(param_1, param_2, **kwargs):
#     print('param_1', param_1)
#     print('param_2', param_2)
#     for key, value in kwargs.items():
#         print(f'cheia: {key} si valoarea {value}')
#
#
# my_function('popescu', 'ion', telefon = 3221314141, email = 'popesc.ino@gmail.com')


def my_function():
    def my_second_function():
        msg = 'alt baaaaaaaaaaaaaaaaaaaaai'
        print(f'this is a message {msg}')

    msg = 'BAAAAAAAAAAAAAAAAAI'

    my_second_function()


my_function()




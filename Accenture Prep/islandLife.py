# def minimum_boxes(input1: int, input2: int, input3: int) -> int:
#     N = input1  # number of sweets per box
#     E = input2  # sweets required per day
#     D = input3  # total number of days to survive

#     # Calculate how many days are Sundays (since no sweets can be bought on Sundays)
#     sundays = D // 7
#     # Days you can actually buy sweets
#     buying_days = D - sundays

#     # Calculate total sweets required
#     total_sweets_required = E * D

#     # Calculate the maximum number of sweets you can buy during the non-Sunday days
#     max_sweets_can_buy = buying_days * N

#     # If you can't get enough sweets, return -1
#     if total_sweets_required > max_sweets_can_buy:
#         return -1

#     # Calculate minimum number of boxes required
#     boxes_required = total_sweets_required // N

#     # If there are remaining sweets to buy that don't fit into full boxes, buy an extra box
#     if total_sweets_required % N != 0:
#         boxes_required += 1

#     return boxes_required

# print(minimum_boxes())

N = 70  # sweets bought per day
E = 100 # sweets required per day
D = 6   # total number of days

reqSweets = E * D
sundays = D // 7
buyingDays = D - sundays
totalSweets = buyingDays * N

if reqSweets > totalSweets:
    print(-1)
else:
    reqBoxes = reqSweets // N
    if reqSweets % N == 0:
        print(reqBoxes)
    else:
        print(reqBoxes + 1)

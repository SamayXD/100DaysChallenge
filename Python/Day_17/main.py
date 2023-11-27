# import random

# class User: 
#     def __init__(self, user_id):
#         self.id = user_id
#         self.followers = 0
#         self.following = 0
     
#     def follow(self, user):
#         self.following +=1
#         user.followers +=1
        

    
        
# user_one = User("1")
# user_two = User("2")

# user_one.follow(user_two)
# user_two.follow(user_one)
# user_two.follow(user_one)
# print(f"User: {user_one.id}, Followers: {user_one.followers}, Followinf: {user_one.following}")
# print(f"User: {user_two.id}, Followers: {user_two.followers}, Followinf: {user_two.following}")


def maximumSwap(num: int) -> int:
    max = str(num)
    num_temp = list(map(int, str(num)))
    num_main = list(map(int, str(num)))
    num_temp.sort(reverse=True)
    if num_temp[0] == num_main[0]:
        greatest = num_temp[1]
        print(num)
    else:
        greatest = num_temp[0]
        x = num_main[0]
        num_main[num_main.index(greatest)] = x
        num_main[0] = greatest
        result = int(''.join(map(str, num_main)))
        return result
    
maximumSwap(num = 98368)
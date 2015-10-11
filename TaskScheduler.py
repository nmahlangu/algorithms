# Given a list of input tasks to run (where each takes 1 time slot)
# and a cooldown time (the time during which tasks of the same type must
# wait to run), write a function that returns the minimum number of
# time slots needed to run all the tasks in the given order.
#
# For example:
#   Tasks: AAABBBCCC
#   Cooldown: 2
#   Return: 21 (order is A__A__AB__B__BC__C__C)
# 
#   Tasks: ABCABC
#   Cooldown: 3
#   Return: 7 (order is ABC_ABC)
#  
#   Tasks: ABCDEFBDFABD
#   Cooldown: 6
#   Return: 18 (order is ABCDEF__B_D_FA_B_D)

def schedule(tasks, cooldown):
    if not tasks or not cooldown:
        return 0

    last_executed = {}
    position = 0
    for task in tasks:
        since_last = position - last_executed.get(task,-cooldown)
        wait = max(0, cooldown - since_last)
        position += 1 + wait
        last_executed[task] = position
    return position

# Solution: Store the most recent time that each type of task was
# executed. Whenever you encounter a new task, it's position in
# the output is given by 1 + the waiting time required to cooldown
# since the last task of the same type. Time complexity is O(n),
# where n is the number of tasks, and space complexity is O(m),
# where m is the number of types of tasks.

import sys

nums = sys.argv[1:]

with open('sales.csv') as f:
    if len(nums) > 1:
        start_pos = int(nums[0])
        end_pos = int(nums[1])
    elif len(nums) == 0:
        start_pos = 0
        end_pos = sum(1 for line in f)
        f.seek(0)
    else:
        start_pos = int(nums[0])
        end_pos = sum(1 for line in f)
        f.seek(0)

    for pos, line in enumerate(f):
        if start_pos <= pos + 1 <= end_pos:
            print(line.strip())

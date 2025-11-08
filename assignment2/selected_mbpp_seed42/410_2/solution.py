def min_val(listval):
    nums = [x for x in listval if isinstance(x, (int, float)) and not isinstance(x, bool)]
    return min(nums) if nums else None
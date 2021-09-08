def containsDuplicate(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    elec_count = {}
    for ele in nums:
        if ele in elec_count:
            elec_count[ele] += 1
        else:
            elec_count[ele] = 1
    for key, value in elec_count.items():
        if value > 1:
            return True
    return False
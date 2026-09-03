class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = nums1, nums2
        if len(a) > len(b):
            a, b = b, a
        
        left_ct = (len(a) + len(b) + 1) // 2
        left, right = 0, len(a)

        while left <= right:
            i = (left + right) // 2 # left a ct
            j = left_ct - i # left b ct

            left1 = a[i - 1] if i > 0 else float('-inf')
            right1 = a[i] if i < len(a) else float('inf')
            left2 = b[j - 1] if j > 0 else float('-inf')
            right2 = b[j] if j < len(b) else float('inf')

            if left1 <= right2 and left2 <= right1:
                if (len(a) + len(b)) % 2 == 0:
                    return (max(left1, left2) + min(right1, right2)) / 2
                else:
                    return max(left1, left2)
            elif left1 > right2:
                right = i - 1
            else:
                left = i + 1
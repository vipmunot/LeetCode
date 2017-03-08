class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        a = nums1 + nums2
        a = sorted(a)
        if len(a)%2 == 0:
            return ((a[int(len(a)/2)-1] + a[int(len(a)/2)])/2.0)
        else:
            return a[int(len(a)/2)]
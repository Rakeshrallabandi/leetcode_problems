class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] < x:
                low = mid + 1
            else:
                high = mid - 1
        left, right = low - 1, low
        ans = []
        while k > 0:
            if left < 0:
                ans.append(arr[right])
                right += 1
            elif right >= len(arr):
                ans.append(arr[left])
                left -= 1
            else:
                if abs(arr[left] - x) <= abs(arr[right] - x):
                    ans.append(arr[left])
                    left -= 1
                else:
                    ans.append(arr[right])
                    right += 1
            k -= 1
        return sorted(ans)

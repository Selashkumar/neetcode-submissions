class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        mid = (l + r) // 2
        while l <= r:
            print(matrix[mid][-1])
            if matrix[mid][-1] >= target and matrix[mid][0] <= target:
                il, ir =0, len(matrix[mid]) - 1
                imid = (il+ir)//2
                print('f',matrix[mid])
                while il <= ir:
                    if matrix[mid][imid] == target:
                        return True
                    elif matrix[mid][imid] < target:
                        il = imid + 1
                        imid = (il +ir) // 2
                    else:
                        ir = imid - 1
                        imid = (il + ir) // 2
                return False
            elif matrix[mid][-1] < target:
                l = mid + 1
                mid = (l + r) //2
            else:
                r = mid - 1
                mid = (l + r) //2
        return False
class Solution():
    def generate(self, numRows):
        pascal_tri = []
        for i in range(numRows):
            if i == 0:
                temp = [0, 1, 0]
                pascal_tri.append(temp[1: -1])
            else:
                new_line = [0] * (i + 1)
                for index, value in enumerate(temp):
                    if index == len(temp) - 1:
                        break
                    new_line[index] = value + temp[index + 1]
                temp = [0] + new_line + [0]
                pascal_tri.append(new_line)
        
        return pascal_tri


if __name__ == "__main__":
    solu = Solution()
    print(solu.generate(5))

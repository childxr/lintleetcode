class Solution:

    def logSort(self, logs):
        logs = [x.split(' ') for x in logs]
        no_num, num = [], []
        for l in logs:
            if l[1].isalpha():
                no_num.append(l)
            else:
                num.append(l)

        sorted_no_num = sorted(no_num, key=lambda x:(x[1:], x[0]))
        return [' '.join(x) for x in sorted_no_num + num]

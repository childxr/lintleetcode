class Solution:
    """
    @param time: the given time
    @return: the next closest time
    """
    def nextClosestTime(self, time):
        # write your code here
        hour, minutes = time.split(":")
        minitues_24hour = 24 * 60
        cur_minutes = 60 * int(hour) + int(minutes)
        ans = None
        for i in xrange(cur_minutes + 1, cur_minutes + minitues_24hour + 1):
            x = i % minitues_24hour
            hr, mins = x / 60, x % 60
            tm = "%02d:%02d" % (hr, mins)
            aset = set(time)
            bset = set(tm)
            if bset <= aset:
                ans = tm
                break
        return ans

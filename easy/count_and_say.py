class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        ret = ""
        if n != 1:
        	ret = self.countAndSay(n-1)
        else:
            return "1"
        last = ""
        count = 0
        say = ""
        for c in ret:
            if last == "":
                last = c
            if last != c:
                say += "{}{}".format(count, last)
                last = c
                count = 0
            count += 1
        if last:
            say += "{}{}".format(count, last)
        
        return say

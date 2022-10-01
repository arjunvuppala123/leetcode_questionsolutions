class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if queryIP.count(":")==7:
            if all([re.search(r'^(\d|[a-fA-F]){1,4}$', part) for part in queryIP.split(":")]):
                return "IPv6"
            else:
                return "Neither"

        if queryIP.count(".")==3:
            if all([re.search(r'^([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$', part) for part in queryIP.split(".")]):
                return "IPv4"
            else:
                return "Neither"
        
        else:
            return "Neither"
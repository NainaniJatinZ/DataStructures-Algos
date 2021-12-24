
# It was freaking 2 pages worth of confusingly worded information about the question
# Question: split the information provided and "load" them into files with names --> file'date here'.text
# data was provided in the following format 
# 6
# "H"
# "aaaa10/20/1020"
# "T"
# "H"
# "bb15/02/1930"
# "T" 

# I think the biggest factor here was me getting lost in information. Next time I'll try and decode the question with its input and output ASAP
class Solution(object):
    def splitFile(self, fileData):
        if len(fileData)<3:
            print("Invalid file")
            return
        length = range(int(len(fileData)/3))
        multi_leng = [j*3 for j in length]
        for i in multi_leng:
            if fileData[i] == "H" and fileData[i+2] == "T":
                date = fileData[i+1][-10:]
                data = fileData[i+1][:len(fileData[i+1])-10]
                print(f"Transaction on {date} was written to-> file{date[:2]}{date[3:5]}{date[6:]}.txt")
            else: 
                print("Invalid file")
                break
        
if  __name__ == "__main__":
    inp = ["H", "aaa10/10/1972", "T", "H", "bbbbbbb12/12/2001", "T"]
    # inp = ["H", "aaa10/10/1972", "T"]
    Solution().splitFile(inp)
    
    
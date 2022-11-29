class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secretCount = {}
        for i in range(len(secret)):
            secretCount[secret[i]] = 1 + secretCount.get(secret[i],0)
        # secretCount = Counter(secret)
        # print(secretCount)
        x = 0
        y = 0
        for i in range(len(secret)):
            if(secret[i] == guess[i]):
                x += 1
                secretCount[secret[i]] = secretCount.get(secret[i],0) - 1
                if(secretCount[secret[i]] == 0):
                    secretCount.pop(secret[i])
        # print(secretCount)
        for i in range(len(guess)):
            if guess[i] in secretCount and guess[i] != secret[i]:
                y += 1
                secretCount[guess[i]] = secretCount.get(guess[i],0) - 1
                if(secretCount[guess[i]] == 0):
                    secretCount.pop(guess[i])
        # print(secretCount)
        return (str(x) + 'A' + str(y) + 'B')



class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secretCount = collections.Counter(secret)
        guessCount = collections.Counter(guess)
        bulls = 0
        cows = 0
        for i in range(len(secret)):
            # bulls
            if (secret[i] == guess[i] and secretCount[secret[i]] > 0 and guessCount[guess[i]] > 0):
                bulls+=1
                secretCount[secret[i]] -= 1
                guessCount[guess[i]] -= 1
                if(secretCount[secret[i]]==0):
                    secretCount.pop(secret[i])
                if(guessCount[guess[i]]==0):
                    guessCount.pop(guess[i])


        # for i in range(len(secret)):
        for i in range(len(guess)):
            if (guess[i] in secretCount and secretCount[guess[i]] > 0 and guessCount[guess[i]] > 0):
                print(secretCount)
                secretCount[guess[i]] -= 1
                guessCount[guess[i]] -= 1
                cows+=1
        # print(bulls,"A",cows,"B")

        return (str(bulls) + 'A' + str(cows) + 'B')
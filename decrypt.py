from collections import Counter
from tabulate import tabulate
import six
import random


class vigenere_decryption:
    def __init__(self):
        self.alpha = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    def find_all(self, str_, char):
        # input string all upper case, and a character(upper case letter), returns a list of indices such that msg[index] =
        num = str_.find(char)
        num_list = [num]
        while num != -1:
            num = str_.find(char, num + 1)
            num_list.append(num)
        return num_list[0:len(num_list)-1]

    def second_key_word_length(self, msg):
        # inputs sting all upper case, outputs (IC4, IC5, length of the second keyword)
        N = 0; summation = 0; str1 = ""  # str1: temporary str for frequency
        print("Suppose keyword length is 4. Frequency of letters:")
        for i in range(0, len(msg), 4):           # suppose keyword length 4, calculates IC4
            str1 = str1 + msg[i]
        for char in [chr(x) for x in range(ord('A'), ord('Z') + 1)]:
            lst = self.find_all(str1, char)
            summation = summation+len(lst)*(len(lst)-1)
            N = N + len(lst)
            print(char, len(lst), "  ", end="")   # print frequency of letters
        IC4 = summation / N / (N - 1)
        print("\nIC4 = ", IC4)
        N = 0; summation = 0; str1 = ""
        print("Suppose keyword length is 5. Frequency of letters:")
        for i in range(0, len(msg), 5):         # suppose keyword length 5, calculates IC5
            str1 = str1 + msg[i]
        for char in [chr(x) for x in range(ord('A'), ord('Z') + 1)]:
            lst = self.find_all(str1, char)
            summation = summation+len(lst)*(len(lst)-1)
            N = N + len(lst)
            print(char, len(lst), "  ",end="")
        IC5 = summation / N / (N - 1)
        print("\nIC5 = ", IC5)
        if IC5 > IC4:
            print("IC5 > IC4, second keyword length is 5")
            return 5
        else:
            print("IC4 > IC5, second keyword length is 4")
            return 4

    def frequency_strip(self, msg, sec_len):
        # input string all upper case, and an integer second keyword length, output a list of lists containing all the frequency strips
        output = []
        for j in range(0, sec_len):
            freq = []   # frequency list
            str1 = ""   # temporary str for each strip
            for i in range(j, len(msg), sec_len):
                str1 = str1 + msg[i]
            for char in [chr(x) for x in range(ord('A'), ord('Z') + 1)]:
                lst = self.find_all(str1, char)
                freq.append(len(lst))
            output.append(freq)
        return output

    def visualize_strips(self, msg, sec_len):
        # input string all upper case, and an integer second keyword length, prints formatted frequency strips
        freqs = self.frequency_strip(msg, sec_len)
        k = 0
        while freqs:
            k += 1
            freq = freqs.pop(0)
            nums = []
            for i in range(0, 26):
                nums.append(str(freq[i]))
            nums = list(map(list, six.moves.zip_longest(*nums)))
            print("\n" + tabulate(nums, headers=self.alpha, tablefmt="github"))

    def vigenere_decrypt(self, t, key, sec_len):
        # input t: ciphertext(upper case), key: keyword, sec_len: keyword length
        t_list = list(t)
        k = 0
        res = ""
        while t_list:
            char = t_list.pop(0)
            mod = k % sec_len
            char_num = ord(char) - 65   # turn char to number to perform shift
            shift = ord(key[mod]) -65
            char_num = (char_num - shift) % 26  # shifted number
            res += str(chr(char_num + 65))  # turn shifted number back to letter and append to result string
            k += 1
        return res


class mono_decryption:
    def __init__(self):
        self.alpha = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    def find_all(self, str_, char):
        # input string all upper case, and a character(letter), returns a list of indices such that msg[index] =
        num = str_.find(char)
        num_list = [num]
        while num != -1:
            num = str_.find(char, num + 1)
            num_list.append(num)
        return num_list[0:len(num_list)-1]

    def get_trigrams(self, msg):
        # input string all upper case, output a list of tuples containing all the trigrams
        # each tuple in the output list: (letter, list of all neighbors), each trigram is a pairs of neighbors with the letter in the middle
        res = []
        for char in [chr(x) for x in range(ord('A'), ord('Z')+1)]: # loop through each letter
            lst = self.find_all(msg, char)   # list contains all indices of this letter
            neighbors = []
            end = len(msg)-1
            for i in lst:   # find all neighbors and store it in a list
                if i == 0:
                    neighbors.append(msg[1])
                elif i == end:
                    neighbors.append(msg[end-1])
                else:
                    neighbors.append(msg[i-1]+msg[i+1])
            res.append((char, neighbors))
        return res

    def trigraph_table(self, msg):
        # input msg:ciphertext, all upper case
        trigrams = self.get_trigrams(msg)
        neighbors = [trigram[1] for trigram in trigrams]  # neighbors of each letter
        letters = self.alpha
        for j in range(0, 26):
            neighbors[j].insert(0, len(neighbors[j]))
        neighbors = list(map(list, six.moves.zip_longest(*neighbors, fillvalue='-')))
        print("\n")
        print(tabulate(neighbors, headers=letters, tablefmt="github"))

    def get_frequency_dictionary(self):
        # output relative frequency dictionary of each trigram, eg dict["AND"] = 0.007252281087500791
        freq_dict = {}
        with open("english_trigrams.txt", "r") as txt:
            lines = txt.readlines()
        trigrams = [i.strip().split(' ')[0] for i in lines]
        freqs = [int(i.strip().split(' ')[1]) for i in lines]
        s = sum(freqs)
        for i in range(len(trigrams)):
            freq_dict[trigrams[i]] = freqs[i] / s
        return freq_dict

    def cipher_to_plain_with_key(self, ciphertext, key):
        # input ciphertext: string all upper case, key: string representing Original Encryption Alphabet
        # output plaintext string all upper case
        for i in range(len(key)):   # loop through each letter
            plain = chr(i + 65).lower()  # corresponding letter in plaintext, upper to avoid re-replacement
            ciphertext = ciphertext.replace(key[i], plain)
        return ciphertext.upper()

    def get_cost(self, text, freq_dict):
        # input text: string all upper case, return cost of the input text
        # cost is the reciprocal of the sum of relative frequencies of all trigrams in the text
        s = 0
        for i in range(len(text) - 2):
            trigram = text[i:i+3]
            if trigram in freq_dict:
                s += freq_dict[trigram]
        return -s

    def get_key(self, ciphertext, init_trials, swap_trials):
        # input ciphertext all upper case
        # init_trials: number of initial shuffle trials
        # swap_trials: number of swaps of 2 letters in the key, hope to get better key
        alphabet = self.alpha
        lowest_cost = 1000
        freq_dict = self.get_frequency_dictionary()
        for trail_number in range(1, init_trials):  # loop through 1 to 49
            key = alphabet.copy()
            random.shuffle(key)
            cost = self.get_cost(self.cipher_to_plain_with_key(ciphertext, key), freq_dict)
            j = 0
            while j < swap_trials:
                # perform random swaps on key
                rand1, rand2 = random.randint(0, 25), random.randint(0, 25)
                while rand2 == rand1:   # not swapping the same index
                    rand2 = random.randint(0, 25)
                new_key = key.copy()
                new_key[rand1], new_key[rand2] = key[rand2], key[rand1]
                new_cost = self.get_cost(self.cipher_to_plain_with_key(ciphertext, new_key), freq_dict)
                if new_cost < cost:  # update if we get better key
                    cost = new_cost
                    key = new_key
                    j = 0
                else:
                    j += 1   # if not getting any better key after 5000 trials, return the best
            if cost < lowest_cost:  # get the best key in 50 initial shuffle trials
                best_key = key
                lowest_cost = cost
            # print(F"Trial number {trail_number:2}: {key} with cost: {cost}")
        return best_key




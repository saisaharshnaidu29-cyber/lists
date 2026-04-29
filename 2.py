def match_words(words):
    CTR = 0
    LST = []
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            CTR += 1
            LST.append(word)

    print("list of words with first and last character same\n", LST)
    return CTR
count = match_words(['hihvaduhanagafebfhanniggerahadwhgdahwgdi', 'gvsaduyagvdkfsyuikagxgdadgfgakvahgdadbacavxffdokdafvagdviwdgqhdjknbvjlagijfuyuagujbhguyawijfwvf', 'kjasisguayHUOHIUAIFADHASHVCSTDASFSVDFCFVAF', '1221', 'dvghauqwcadyqfcgdd', 'fbcuyeswadcffndhjuyhdhad', 'fugsyidgfatwuoydwfgtyafdacvb', 'fdgh8asgfdadgcfgaytxdaydutyyucdtf', 'yus iokfdp[svfgdcataukjfvdtrd]'])
print("number of words with first and last character same:", count)

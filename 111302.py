numbers = [5,3,4,2,1]
characters = ['가','나','다','라']
sort_numbers = sorted(numbers)     # cf. reversed(numbers)
sort_characters = reversed(characters)

print("sort_numbers=", sort_numbers)
print("numbers=", numbers)
print("sort_characters=", sort_characters)
print("characters=", characters)


numbers.sort()
characters.sort()
print("asc>>", numbers)
print("asc>>", characters)

numbers.sort(reverse=False)
characters.sort(reverse=True)

print("desc>>", numbers)
print("desc>>", characters)

print(numbers)

#브랜치테스트용
#브랜치테스트용 diff 구문 이용
print("브랜치테스트용눈에날뛰는거")
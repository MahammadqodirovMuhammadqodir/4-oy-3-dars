# def misol20(n, numbers):
#     smaller_numbers = []
#     for i in range(n - 1):
#         if numbers[i] < numbers[i + 1]:
#             smaller_numbers.append(numbers[i])
#     return smaller_numbers, len(smaller_numbers)


# def misol21(n, numbers):
#     return all(numbers[i] <= numbers[i + 1] for i in range(n - 1))


# def misol22(n, numbers):
#     for i in range(n - 1):
#         if numbers[i] < numbers[i + 1]:
#             return i
#     return 0


# def misol23(n, numbers):
#     for i in range(1, n - 1):
#         if not ((numbers[i - 1] > numbers[i] < numbers[i + 1]) or (numbers[i - 1] < numbers[i] > numbers[i + 1])):
#             return i
#     return 0


# def misol24(n, numbers):
#     indices = [i for i, num in enumerate(numbers) if num == 0]
#     if len(indices) < 2:
#         return 0
#     return sum(numbers[indices[-2] + 1: indices[-1]])


# def misol25(n, numbers):
#     indices = [i for i, num in enumerate(numbers) if num == 0]
#     if len(indices) < 2:
#         return 0
#     return sum(numbers[indices[0] + 1: indices[-1]])


# def misol26(n, k, numbers):
#     return [num ** k for num in numbers]


# def misol27(n, numbers):
#     return [numbers[0] ** i for i in range(1, n + 1)]


# def misol28(n, numbers):
#     return [numbers[0] ** i for i in range(n, 0, -1)]


# def misol29(k, datasets):
#     return [sum(dataset) for dataset in datasets]

# if __name__ == "__main__":
#     print("Series20: O'ng qo'shnisidan kichik sonlarni topish")
#     n = int(input("n natural sonini kiriting: "))
#     numbers = list(map(int, input(f"{n} ta butun sonni probel orqali kiriting: ").split()))
#     if len(numbers) == n:
#         result, count = misol20(n, numbers)
#         print("O'ng qo'shnisidan kichik sonlar:", result)
#         print("Sonlar soni:", count)
#     else:
#         print("Xato: kiritilgan sonlar soni n ga teng emas.")
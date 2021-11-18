line1 = ("="*50)
line2 = ("-"*50)
print(line1)
print("%-13s%10s%14s" % ("|", "Welcome Ittipat Jitrada", "|"))
print("%-13s%10s%15s" % ("|", "Computer Programming I", "|"))
print(line1)

all_score = []
total_pass = 0
average = 0

for i in range(1, 11):
    num = float(input(f"Please enter score #{i} :").format(i))
    if num > 0 and num <= 100:
        all_score.append(num)
        if num >= 50:
            total_pass += 1
            average += num

averageScore = sum(all_score) / len(all_score)
print(line2)
print("|%17s Results %22s|" % (" ", " "))
print(line2)

print("Amount of scores :", len(all_score))
print("Average Score :", round(averageScore, 2))
print("Highest Score :", max(all_score))
print("Lowest Score :", min(all_score))
print(line1)

print("Total Passed Student :", total_pass)
print("Average Passed score :",
      round(average / total_pass, 2))
print(line1)

all_score.sort(reverse=True)
print("Scores list: %s" % (all_score))

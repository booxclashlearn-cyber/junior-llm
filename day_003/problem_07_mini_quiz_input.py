score = 0

answer_1 = input("What programming language are we learning? ")
if answer_1 == "python":
    score += 1

answer_2 = input("What does AI stand for? ")
if answer_2 == "artificial intelligence":
    score += 1  
        
answer_3 = input("What tool is used to track code changes? ")
if answer_3 == "git":
    score += 1

print(f"Final score: {score}/3")

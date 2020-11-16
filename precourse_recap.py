guess = input('is git add (y/n)? ')
git_push = input("git commit -m then")


print ("My guess is, " + guess) 

if guess == "y":
    git_push
else:
    print("git add then")
from github import Github

path = "C:/Users/USER/Desktop/token.txt"
with open(path, "r") as file:
    token = file.read()
    g = Github(token)  # safer alternative, if you have an access token
    u = g.get_user()
    repo = u.create_repo("HWrepo")
    path = "D:\Developers Institute\git\Week10\Day3\DailyChallange\daily.py"
    with open (path, "r") as content:
        repo.create_file(path,"commit test",content.read())

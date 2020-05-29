import datetime
favouriteDay = datetime.date(1515, 4, 26)

training = datetime.timedelta(100)  ## 100 days

total = favouriteDay + training

congratulations = "You graduated on {:%A, %B %d, %Y}"

print(congratulations.format(total))

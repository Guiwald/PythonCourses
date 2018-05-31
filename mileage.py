print("How many kilometers do you want to convert into miles?")
kms = float(input())
mls = kms/1.60934
mls = round(mls, 2)
print(f"OK, {kms} kms are {mls} miles")
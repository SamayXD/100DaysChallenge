print("==== TIP CALCULATOR ====")

totalBill = float(input("What was the total bill? "))

tipInPercent = round(float(
    totalBill * (
        (float(
            input("How much percent tip you want to give? (in %) ")
            )
         )/100)
    ), 2)

numberOfPeople = int(input("Number of People were? "))

finalSplit = round(((totalBill + tipInPercent) / numberOfPeople), 2)

print(
    f"\nYour tip will be : {tipInPercent}/-\ntotal bill is : {totalBill+ tipInPercent}/-\nsplit will be : {finalSplit}/-")

investment = int(input())
earnings = int(input())
if investment < 0 or earnings < 0:
    print("Invalid Input")
else:
    if earnings > investment:
        profit = earnings - investment
        profit_percent = (profit / investment) * 100
        print(f"Profit - {int(profit_percent)}%")
    elif earnings < investment:
        loss = investment - earnings
        loss_percent = (loss / investment) * 100
        print(f"Loss - {int(loss_percent)}%")
    else:
        print("No Profit, No Loss")
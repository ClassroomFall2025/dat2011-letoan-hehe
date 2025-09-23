def Calculate_water_bill(usage):
    if usage <= 10:
        bill = usage * 7500
    elif usage <= 20:
        bill = 10 * 7500 + (usage - 10) * 8800
    elif usage <= 30:
        bill = 10 * 7500 + 10 * 8800 + (usage - 20) * 12000
    else:
        bill = 10 * 7500 + 10 * 8800 + 10 * 12000 + (usage - 30) * 24000
    return bill
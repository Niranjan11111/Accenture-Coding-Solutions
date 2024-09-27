def minPowerConsumption(p, x, y):
    cyclesOfM = p // 100
    remainingCus = p % 100

    powerOfM = cyclesOfM * x

    cyclesofN = (remainingCus + 3) // 4
    powerOfN = cyclesofN * y

    powerOfMandN = powerOfM + powerOfN

    totalNonly = (p + 3) // 4
    powerNonly = totalNonly * y

    return min(powerOfMandN, powerNonly)

print(minPowerConsumption(9, 40, 8))
print(minPowerConsumption(105, 80, 10))
print(minPowerConsumption(112, 80, 10))


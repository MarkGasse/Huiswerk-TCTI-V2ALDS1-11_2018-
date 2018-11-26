def machtv3(getal,macht):
    assert macht > 0

    m = 1
    teller = 0
    while macht > 0:
        teller += 1
        if macht%2 == 0:
            macht = macht // 2
            getal = getal*getal

        else:
            macht -= 1
            m = m *getal

    return teller

print(machtv3(2,1000))
print(machtv3(2,10000))

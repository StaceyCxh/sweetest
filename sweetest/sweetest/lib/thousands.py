def thousands(num):
    return format(float(num), '0,.2f')


def antiThousands(num):
    return num.replace(',', '')
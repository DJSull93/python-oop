def bmi_function(hei, wei):
    hei = hei
    wei = wei
    return round(hei/wei**2 * 10000, 2)

class Bmi(object):
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

    def get_bmi(self):
        return round(self.weight/(self.height)**2 * 10000, 2)

if __name__ == '__main__':
    #b = Bmi(183, 85)
    #print(b.get_bmi())
    print(bmi_function(82, 180))



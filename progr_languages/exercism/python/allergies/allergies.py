class Allergies:

    def __init__(self, score):
        self.score = score % 256

    def allergic_to(self, item):
        return True if item in self.lst else False

    @property
    def lst(self):
        items = {
            1: "eggs",
            2: "peanuts",
            4: "shellfish",
            8: "strawberries",
            16: "tomatoes",
            32: "chocolate",
            64: "pollen",
            128: "cats"
        }
        allergies = []
        if self.score == 0:
            return allergies
        if self.score in items.keys():
            return [items[self.score]]
        else:
            al_codes = [key for key in items.keys() if key <= self.score]
            score = self.score

            code = al_codes.pop()  # last element is always an allergy
            allergies.append(items[code])  # append last element
            score -= code  # subtract from score
            while True:
                if score in items.keys():
                    allergies.append(items[score])
                    break
                code = al_codes.pop()
                allergies.append(items[code])
                score -= code

        return allergies


if __name__ == '__main__':
    print(Allergies(255).lst)

class Allergies:

    def __init__(self, score):
        self.score = score

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
        if self.score == 0:
            allergies = []
        else:
            allergies = [allergy for key, allergy in items.items() if key <= (self.score % 128)]
        return allergies

"""  Tasks: подключить модуль time чтобы была точка отсчета даты и времени
     # 6 Сниженное количество фермента алкогольдегидрогеназа – есть люди, у которых он полностью отсутствует, тогда их будет валить с ног даже глоток вина
     #  Отсутствие закуски – чем жирнее пища, тем медленнее человек пьянеет: кто закусывает огурцами или кусочком лайма, гарантировано будут пьянее любителей хорошо поесть.
     # 4 Телосложение – жировая прослойка частично впитывает алкоголь, и люди с лишним весом пьянеют медленнее стройных, однако и похмелье у них длится дольше.
     # 5 Скорость поглощения спиртного – если давать печени время для переработки этанола, опьянение будет наступать медленнее, так что пару тостов можно и пропустить, если хотите веселиться дольше.
     # 2 Возраст - чем старше человек, тем ниже скорость переработки и вывода этанола, потому даже здоровый и крепкий пожилой мужчина будет пьянеть быстрее, чем он же в юности.
     # 3 Крепость - чем крепче алкоголь, тем быстрее наступает опьянение. Однако газированные и шипучие напитки существенно ускоряют процесс, так как пузырьки воздуха способствуют быстрому всасыванию алкоголя в кровь. Так что тот, кто запивает газировкой, при прочих равных гарантировано напьется раньше остальных. Как и дама с шампанским, любитель пригубить пиво между крепкими шотами.
     # 1 Пол - (женщины пьянеют быстрее чем мужчины)"""


class Alcogolik:
    stadii_drinking = {
        0: "Все окей",
        0.29: "I стадия.\nВ целом адекватное поведение, без очевидных признаков опьянения",
        0.59: "II стадия.\nСлегка нарушается координация и концентрация внимания. В поведение\
просматривается снижение сдержанности и излишняя разговорчивость.Внутренне ощущается чувство эйфории и раскрепощения.\
Снижается ощущение реальности и пределов дозволенности",
        0.9: "III стадия.\nОслабевает переферийное зрение, теряется логика мышления, углубляется потеря \
ощущения реальности. Появляется очевидный дискомфорт к яркому свету, расторможенность, сильное притупление ощущений,\
потеря контроля над собой с последующим отсутствием воспоминаний о совершенных действиях",
        1.9: "IV стадия\nСильное нарушение рефлексов, замедленная и неправильная реакция, абсолютно \
непонятное изъяснение. В подобном состоянии мужчины сталкиваются с нарушением эрекции и даже временной потерей \
потенции. Могут проявлятся сильные симптомы отравления. Повышенная агрессивность, проявляющаяся в неконтроируемых и \
резких выпадах гнева, смене настроения и снижении либидо",
        2.9: "V стадия\nСопровождается потерей сознания, памяти и сильного нарушения моторики.\
Полная потеря ориентиров в пространстве, непонимание происходящего с ним и объектами вокруг него",
        3.9: "VI стадия.\nНарушается ритм дыхания человека, наблюдается учащенное биение или даже\
остановка сердца. Неконтролруемый рвотный инстинкт и потеря контроля над мочеиспусканием. Коррдинация передвижения \
полностью нарушена, после падения, человек, не в состоянии поднятся. Уход в ступор и потеря сознания.",
        4: "VII стадия.\nДвижение зрачков, как и сердцибиение с дыханием неконтролируемые. Чаще всего \
отсутствие сознания и абсолютно неконтролируемое поведение. Велика вероятность смерти"
    }

    def __init__(self, speed_drinking=None, count_ferment=None):
        sex = {"1": 0.55, "2": 0.68}
        self.sex = sex[input("Enter your sex. If you woman input 1, man - 2 ").strip()]
        self.age = input("Enter your age: ").strip()
        self.weight = int(input("Enter your weight: ").strip())
        self.height = int(input("Enter your height: ").strip())
        self.body_type = self.BMI(self.weight, self.height)
        self.count_ferment = count_ferment  # input("Enter your enzyme number (if you don't know, then skip): ").strip()
        self.speed_drinking = speed_drinking
        self.inside = {"drinks": {}, "foods": {}}
        self.count_aib = 0  # free alco in blood

    def drink(self, alco, turnovers, gramm):
        self.inside["drinks"][alco] = turnovers
        self._clean_alco_in_blood(turnovers, gramm)
        return self.inside

    def eat_food(self, snack, fats):
        self.inside["foods"][snack] = fats

    def _clean_alco_in_blood(self, turnovers, gramm):
        aib = (gramm * (turnovers * self.sex) / 100)  # расчет выпитого чистого алкоголя попавшего в кровь
        free_aib = aib - (aib * 10 / 100)  # расчет выпитого чистого алкоголя попавшего в кровь без 10% рассосавшихся
        f_Vidmarka = round(free_aib / (self.weight * 0.7), 2)
        print(f"{f_Vidmarka} промилли")
        self.count_aib += f_Vidmarka

    def info(self):
        print(
            f"""Sex: {self.sex}
Age: {self.age}
Body_type: {self.body_type}
Speed_drink{self.speed_drinking}
Count_ferment: {self.count_ferment}
Inside: {self.inside}
Promille: {self.count_aib}"""
        )


    def BMI(self,weight, height):  # Body mass index
        categ = {"Critical less weight": 16.5,
                 "Less weight": 18.4,
                 "Normal weight": 24.9,
                 "More weight": 30,
                 "Fat I": 34.9,
                 "Fat II": 40,
                 "Fat III": 40.01}

        ind = weight / ((height ** 2) / (10**3))
        for value in categ:
            if ind <= categ[value]:
                return categ[value]


    def rezult(self):
        for i, base_promille in enumerate(self.stadii_drinking.keys()):
            try:
                if base_promille < self.count_aib < list(self.stadii_drinking.keys())[i + 1]:
                    print(self.stadii_drinking[base_promille])
                    break
            except IndexError:
                print(self.stadii_drinking[base_promille])

        print(
            f"{(self.count_aib // 0.15)} hours {round((self.count_aib % 0.15), 2) * 60 / 0.15} minutes untill normal ")


def main():
    individ = Alcogolik()
    while True:
        var = input("Enter the number:\n"
                    "1-drink\n"
                    "2-eat_food\n"
                    "3-info\n"
                    "q-end_programm\n").strip()
        if var == "1":
            individ.drink(input("Enter the name of alco: "), int(input("Enter the number turnovers of alco: ")),
                          int(input("Enter the number gramm alco: ")))
        elif var == "2":
            #individ.eat_food(input("Enter the name of food: "), input("Enter the number fats of food: "))
            pass
        elif var == "3":
            individ.info()
        elif var == "q":
            individ.rezult()
            break
    input("Enter the any key: ")

if __name__ == "__main__":
    main()

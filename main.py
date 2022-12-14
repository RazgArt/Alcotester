"""  Tasks: подключить модуль time чтобы была точка отсчета даты и времени
            использовать BMI
     # 6 Сниженное количество фермента алкогольдегидрогеназа – есть люди, у которых он полностью отсутствует, тогда их будет валить с ног даже глоток вина
     #  Отсутствие закуски – чем жирнее пища, тем медленнее человек пьянеет: кто закусывает огурцами или кусочком лайма, гарантировано будут пьянее любителей хорошо поесть.
     # 4 Телосложение – жировая прослойка частично впитывает алкоголь, и люди с лишним весом пьянеют медленнее стройных, однако и похмелье у них длится дольше.
     # 5 Скорость поглощения спиртного – если давать печени время для переработки этанола, опьянение будет наступать медленнее, так что пару тостов можно и пропустить, если хотите веселиться дольше.
     # 2 Возраст - чем старше человек, тем ниже скорость переработки и вывода этанола, потому даже здоровый и крепкий пожилой мужчина будет пьянеть быстрее, чем он же в юности.
     # 3 Крепость - чем крепче алкоголь, тем быстрее наступает опьянение. Однако газированные и шипучие напитки существенно ускоряют процесс, так как пузырьки воздуха способствуют быстрому всасыванию алкоголя в кровь. Так что тот, кто запивает газировкой, при прочих равных гарантировано напьется раньше остальных. Как и дама с шампанским, любитель пригубить пиво между крепкими шотами.
     # 1 Пол - (женщины пьянеют быстрее чем мужчины)"""

import time


class Alcoholic:
    stage_of_intoxication = {
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
        self.sex = sex[input("Enter your sex. If you are a woman input 1, a man - 2\n").strip()]
        self.age = input("Enter your age\n").strip()
        self.weight = int(input("Enter your weight\n").strip())
        self.height = int(input("Enter your height:\n").strip())
        self.body_type = self.__bmi(self.weight, self.height)
        self.count_ferment = count_ferment  # input("Enter your enzyme number (if you don't know, then skip): ").strip()
        self.speed_drinking = speed_drinking
        self.inside = {"drinks": {}, "foods": {}}
        self.count_aib = 0  # free alco in blood

    def drink(self) -> dict:
        self.alco = input("Enter the name of alco:\n")
        self.turnovers = int(input("Enter the number turnovers of alco:\n"))
        self.gramm = int(input("Enter the number gramm alco:\n"))
        self.inside["drinks"][self.alco] = self.turnovers
        self.__clean_alco_in_blood(self.turnovers, self.gramm)
        return self.inside

    # def eat_food(self, snack, fats):
    #     self.inside["foods"][snack] = fats

    def __clean_alco_in_blood(self, turnovers: int, gram: int) -> str:
        aib = (gram * (turnovers * self.sex) / 100)  # расчет выпитого чистого алкоголя попавшего в кровь
        clear_aib = aib - (aib * 10 / 100)  # расчет выпитого чистого алкоголя попавшего в кровь без 10% рассосавшихся
        f_Vidmarka = round(clear_aib / (self.weight * 0.7), 2)
        self.count_aib += f_Vidmarka
        return f"{f_Vidmarka} ppm"

    def info(self):
        self.info = {
            "Sex": "men" if self.sex == 0.68 else "girl",
            "Age": self.age,
            "Body_type": self.body_type,
            "Speed_drink": self.speed_drinking,
            "Count_ferment": self.count_ferment,
            "Inside": self.inside,
            "Ppm": self.count_aib
        }
        print("\n".join([f"{k}:{v}" for k, v in self.info.items()]))

        # переделать Inside: {'drinks': {'asa': 20}, 'foods': {}} может быть загнать в список и с помощью Join вытаскивать 2 списка один слов другой значений и с помощью zip

    def __bmi(self, weight: int, height: int) -> str:  # Body mass index
        category = {"Critical less weight": 16.5,
                    "Less weight": 18.4,
                    "Normal weight": 24.9,
                    "More weight": 30,
                    "Fat I": 34.9,
                    "Fat II": 40,
                    "Fat III": 40.01}
        ind = weight / ((height ** 2) / (10 ** 3))
        for value in category:
            if ind <= category[value]:
                return category[value]

    def result(self):
        for i, base_ppm in enumerate(self.stage_of_intoxication.keys()):
            try:
                if base_ppm < self.count_aib < list(self.stage_of_intoxication.keys())[i + 1]:
                    print(self.stage_of_intoxication[base_ppm])
                    break
            except IndexError:
                print(self.stage_of_intoxication[base_ppm])
        print(
            f"{(self.count_aib // 0.15)} hours {round((self.count_aib % 0.15), 2) * 60 / 0.15} minutes until normal ")
        # print(time.ctime((time.time() + self.count_aib))) подставить и проверить !!!!!!!!!!!!!!!!!!!!!!!!


def main():
    person = Alcoholic()
    info_alco = {
        "1": person.drink,
        "2": "",
        # person.eat_food(input("Enter the name of food: "),  input("Enter the number fats of food: "))
        "3": person.info,
        "q": person.result
    }
    while True:
        action_option = input("Enter the number:\n"
                              "1-drink\n"
                              "2-eat_food\n"
                              "3-info\n"
                              "q-end_program\n").strip()
        info_alco.get(action_option)()
        if action_option == "q":
            break


if __name__ == "__main__":
    main()
    input("Enter the any key: ")

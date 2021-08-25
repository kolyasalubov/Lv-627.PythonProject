import volodymyr_solutions
import sofiia_kovalchuk
import mykhailo_solutuions
import oleh_solutions
import tadey_kushnir
import vladyslav_kriuchkovskyi
import ruslan_liska


class ConsoleSolver:
    def __init__(self):
        self.tasks = {
            "088a": sofiia_kovalchuk.Task088a(),
            "088b": sofiia_kovalchuk.Task088b(),
            "088v": vladyslav_kriuchkovskyi.Task088v(),
            "088g": vladyslav_kriuchkovskyi.Task088g(),
            "108": volodymyr_solutions.Task108(),
            "322": sofiia_kovalchuk.Task322(),
            "331": volodymyr_solutions.Task331(),
            "332": vladyslav_kriuchkovskyi.Task332(),
            "87": mykhailo_solutuions.Task87(),
            "226": mykhailo_solutuions.Task226(),
            "559": mykhailo_solutuions.Task559(),
            "086a": oleh_solutions.Task086a(),
            "086b": oleh_solutions.Task086b(),
            "330": oleh_solutions.Task330(),
            "107": tadey_kushnir.Task107(),
            "243a": tadey_kushnir.Task243a(),
            "243b": tadey_kushnir.Task243b(),
            "555": ruslan_liska.Task555(),
            "178d": ruslan_liska.Task178d(),
            "178e": ruslan_liska.Task178e(),
            "243b": tadey_kushnir.Task243b()
        }

    @property
    def active_task(self):
        return self.__active_task

    @active_task.setter
    def active_task(self, task):
        self.__active_task = task

    def work_with_task(self):
        print(self.active_task.description)
        inp = input("Provide input value/s ").split()
        try:
            self.active_task.change_arguments(*map(lambda x: int(x), inp))
        except (TypeError, ValueError):
            print("Your value/s is/are incorrect. Try again.")
            self.work_with_task()
        else:
            if self.active_task.validate():
                print(f"Solution is {self.active_task.solve()}")
            else:
                print("Your value/s is/are incorrect. Try again.")
                self.work_with_task()

    def run(self):
        task = input("Hello! This is the console solver for many mathematical tasks. "
                     "Which task would you like to view? " )
        if task in self.tasks:
            self.active_task = self.tasks[task]
            self.work_with_task()
            self.run()
        else:
            print("There's no such task :/")
            self.run()


if __name__ == "__main__":
    ConsoleSolver().run()

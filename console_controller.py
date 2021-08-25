import volodymyr_solutions
import sofiia_kovalchuk
import mykhailo_solutuions
import oleh_solutions
import tadey_kushnir
import roman_levytskyi
import artem_prokhvatylov
import ruslan_liska

class ConsoleController:
    def __init__(self):
        self.tasks = {
            "88a": sofiia_kovalchuk.Task088a(),
            "88b": sofiia_kovalchuk.Task088b(),
            "108": volodymyr_solutions.Task108(),
            "187b": roman_levytskyi.Task187b(),
            "187c": roman_levytskyi.Task187c(),
            "322": sofiia_kovalchuk.Task322(),
            "331": volodymyr_solutions.Task331(),
            "87": mykhailo_solutuions.Task87(),
            "226": mykhailo_solutuions.Task226(),
            "554": roman_levytskyi.Task554(),
            "559": mykhailo_solutuions.Task559(),
            "86a": oleh_solutions.Task086a(),
            "86b": oleh_solutions.Task086b(),
            "330": oleh_solutions.Task330(),
            "107": tadey_kushnir.Task107(),
            "243a": tadey_kushnir.Task243a(),
            "243b": tadey_kushnir.Task243b(),
            "182": artem_prokhvatylov.Task182(),
            "560": artem_prokhvatylov.Task560(),
            "323": artem_prokhvatylov.Task323(),
            "555": ruslan_liska.Task555(),
            "178d": ruslan_liska.Task178d(),
            "178e": ruslan_liska.Task178e(),
        }
        self.tasks = {x: self.tasks[x] for x in sorted(self.tasks.keys(), key=lambda x: int(x.rstrip('abcde')))}


    def work_with_task(self, task):
        print(task.description)
        if task.require_input:
            inp = input("Provide input value/s ").split()
            try:
                task.change_arguments(*map(lambda x: int(x), inp))
            except (TypeError, ValueError):
                print("Your value/s is/are incorrect. Try again.")
                self.work_with_task(task)
            else:
                if task.validate():
                    print(f"Solution is {task.solve()}")
                else:
                    print("Your value/s is/are incorrect. Try again.")
                    self.work_with_task(task)
        else:
            print(f"Solution is {task.solve()}")


    def run(self):
        print(f"Hello! This is the console solver for many mathematical tasks.\nHere is the list of available tasks:")
        print('    '.join(self.tasks.keys()))
        task = input("Which task would you like to view? ")
        if task in self.tasks:
            self.work_with_task(self.tasks[task])
            self.run()
        else:
            print("There's no such task :/")
            self.run()


if __name__ == "__main__":
    ConsoleController().run()
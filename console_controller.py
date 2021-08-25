from string import ascii_letters

import volodymyr_solutions
import sofiia_kovalchuk
import mykhailo_solutuions
import oleh_solutions
import tadey_kushnir
import roman_levytskyi
import artem_prokhvatylov
import ruslan_liska

class ConsoleController:

    def close(self):
        print("Closed")
        self.exit = 1

    def __init__(self):
        self.up = 0
        self.exit = 0
        self.commands = {'exit': self.close}
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
        


    def repeat(self):
        options = ['y', 'n']
        command = None
        while command not in options:
            command = input('Run that task again?(y/n): ')
        self.up = [1,0][command == 'y']

    def show_tasks(self):
        tasks_list = sorted(self.tasks.keys(), key=lambda x: int(x.rstrip(ascii_letters)))
        return tasks_list
          

    def work_with_task(self, task):
        while not self.up:
            if task.description:
                print(task.description)
            if task.require_input:
                inp = input("Provide input value/s ").split()
                try:
                    task.change_arguments(*map(lambda x: int(x), inp))
                except (TypeError, ValueError):
                    print("Your value/s is/are incorrect.")
                else:
                    if task.validate():
                        print(f"Solution is {task.solve()}")
                    else:
                        print("Your value/s is/are incorrect.")
            else:
                print(f"Solution is {task.solve()}")
            
            self.repeat()
 

    def run(self):
        while not self.exit:
            print('Hello! This is the console solver for many mathematical tasks.' +
                   '\nEnter "exit" to exit.\nHere is the list of available tasks:')
            print('  '.join(self.show_tasks()))
            task = input("Which task would you like to view? ")
            if task in self.tasks:
                self.work_with_task(self.tasks[task])
            elif task in self.commands:
                self.commands.get(task)()
            else:
                print("There's no such task :/")
            


if __name__ == "__main__":
    ConsoleController().run()
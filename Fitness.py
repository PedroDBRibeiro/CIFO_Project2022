
class Fitness(object):

    fitness_score = 0;

    def calculate_fitness(self) :

        self.row_evaluation()
        self.column_evaluation()
        self.block_evaluation()


    def row_evaluation(self):
        min_current_index = 0;
        max_current_index = 8;

        while max_current_index<= len(object):
            row = set(object[min_current_index:max_current_index])
            if(len(row)==9):
                self.fitness_score =+1

            min_current_index =+ 9
            max_current_index =+ 9

    def column_evaluation(self):
        columns = [0,9,18,27,36,45,54,63,72]

        for i in range(9):
            column = set([object[index] for index in columns])
            if (len(column) == 9):
                self.fitness_score = +1

            columns = [x + 1 for x in columns]

    def block_evaluation(self):
        blocks = [0,1,2,9,10,11,54,63,72]

        for i in range(9):
            block = set([object[index] for index in blocks])
            if (len(block) == 9):
                self.fitness_score = +1

            blocks = [x + 1 for x in blocks]

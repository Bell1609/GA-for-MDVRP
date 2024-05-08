#GA FOR MDVRP
##Find the best solution for the given problem
import sys
from time import time
import trainer

generations = 500
crossover_rate = 0.05
heuristic_mutate_rate = 0.05
inversion_mutate_rate = 0.05
depot_move_mutate_rate = 0
best_insertion_mutate_rate = 0.1
route_merge_rate = 0.05

if __name__ == '__main__':
    t1 = time()

    #input file: test.txt #output file: output.csv
    # Đảm bảo rằng có đủ tham số dòng lệnh, nếu không thì sử dụng giá trị mặc định
    input_file = sys.argv[1] if len(sys.argv) > 1 else 'data/problems/2'
    output_csv = sys.argv[2] if len(sys.argv) > 2 else 'src/output.csv'

    trainer.load_problem(input_file)
    trainer.initialize()

    #Cần truyền input_file thay vì sys.argv[2] vào hàm train để đảm bảo đúng vị trí của tham số
    best_solution = trainer.train(generations, crossover_rate, heuristic_mutate_rate, inversion_mutate_rate,
                                  depot_move_mutate_rate, best_insertion_mutate_rate, route_merge_rate, t1,
                                  intermediate_plots=True, write_csv=output_csv)

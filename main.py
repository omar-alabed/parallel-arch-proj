import random
import sys
import time
import multiprocessing
from sorting_algorithms.bitonic_merge_sort import bitonicSort
from sorting_algorithms.parallel_merge_sort import parallel_sort, merge_sort
import csv  

if __name__ == "__main__":
    size = int(sys.argv[-1]) if sys.argv[-1].isdigit() else False

    if not size:
        size = 1024

        individual_header = ['bitonic sort', 'merge sort']
        parallel_sort_header = [f'parallel merge sort - {num} cores' for num in range(1, multiprocessing.cpu_count()+1)]
        header = individual_header + parallel_sort_header


        with open('algo_comparison_result.csv', 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header)

        # print('SIZE\t\t' ,'USED ALGORITHM\t\t\t\t\t', 'IS THE RESULT SORTED?\t\t', 'TIME')
            for i in range(20):
                print('iteration: ', i)
                data = []
                data_unsorted = [random.randint(0, size) for _ in range(size)]
                for sort in bitonicSort, merge_sort:
                    start = time.time()
                    data_sorted = sort(data_unsorted)
                    end = time.time() - start
                    # print (f'{size}\t\t', f'{sort.__name__}\t\t\t\t\t\t', sorted(data_unsorted) == data_sorted, '\t\t', end)
                    data.append(end)
                
                for proc_no in range(1, multiprocessing.cpu_count()+1):
                    start = time.time()
                    data_sorted = parallel_sort(data_unsorted, proc_no)
                    end = time.time() - start
                    # print (f'{size}\t\t', f'{parallel_sort.__name__} using {proc_no} processessors\t\t\t', sorted(data_unsorted) == data_sorted, '\t\t', end)
                    data.append(end)

                writer.writerow(data)
            # start = time.time()
            # data_sorted = bitonicSort(data_unsorted)
            # end = time.time() - start
            # print(f'{size}\t\t', 'bitonic_sort\t\t',sorted(data_unsorted) == data_sorted, '\t\t', end, '\n')

                size = size * 2
    else:
        print('SIZE\t\t' ,'USED ALGORITHM\t\t', 'IS THE RESULT SORTED?\t\t', 'TIME')
        data_unsorted = [random.randint(0, size) for _ in range(size)]
        for sort in merge_sort, parallel_sort:
            start = time.time()
            data_sorted = sort(data_unsorted)
            end = time.time() - start
            print (f'{size}\t\t', f'{sort.__name__}\t\t', sorted(data_unsorted) == data_sorted, '\t\t', end,)

        start = time.time()
        data_sorted = bitonicSort(True, data_unsorted)
        end = time.time() - start
        print(f'{size}\t\t', 'bitonic_sort\t\t', sorted(data_unsorted) == data_sorted, '\t\t', end, '\n')
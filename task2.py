import heapq
from typing import List

def merge_k_lists(lists: List[List[int]]) -> List[int]:
    """
    Об'єднує k відсортованих списків в один відсортований список за допомогою Min Heap.
    
    Часова складність: O(N log k), де N — загальна кількість елементів, 
    а k — кількість списків.
    
    :param lists: Список відсортованих списків цілих чисел.
    :return: Об'єднаний та відсортований список.
    """
    
    # Використовуємо вбудовану в Python heapq.
    min_heap = []
    
    # 1. Ініціалізація: Додаємо перший елемент з кожного списку до купи.
    # Елемент купи: (значення, індекс_списку, індекс_елемента_у_списку)
    for list_index, current_list in enumerate(lists):
        if current_list:
            # current_list[0] - перший елемент
            # list_index - індекс списку (з якого взяли елемент)
            # 0 - індекс елемента в цьому списку
            heapq.heappush(min_heap, (current_list[0], list_index, 0))
            
    merged_list = []
    
    # 2. Основний цикл: Об'єднання
    while min_heap:
        
        # Вилучаємо найменший елемент
        value, list_index, element_index = heapq.heappop(min_heap)
        
        # Додаємо його до результуючого списку
        merged_list.append(value)
        
        # Перевіряємо, чи є наступний елемент у вихідному списку
        next_element_index = element_index + 1
        current_list = lists[list_index]
        
        if next_element_index < len(current_list):
            # Якщо наступний елемент існує, додаємо його в купу
            next_value = current_list[next_element_index]
            heapq.heappush(min_heap, (next_value, list_index, next_element_index))
            
    return merged_list

# --- Тестування ---
if __name__ == "__main__":
    
    # Тест 1:
    lists_1 = [[1, 4, 5], [1, 3, 4], [2, 6]]
    merged_list_1 = merge_k_lists(lists_1)
    
    print("--- Тест 1: Злиття 3 списків ---")
    print("Вхідні списки:", lists_1)
    print("Відсортований список:", merged_list_1) # Очікується: [1, 1, 2, 3, 4, 4, 5, 6]
    
    
    # Тест 2:
    lists_2 = [[10, 20], [5, 15, 25], [100], [0, 30]]
    merged_list_2 = merge_k_lists(lists_2)
    
    print("\n--- Тест 2: Злиття 4 списків ---")
    print("Вхідні списки:", lists_2)
    print("Відсортований список:", merged_list_2) # Очікується: [0, 5, 10, 15, 20, 25, 30, 100]
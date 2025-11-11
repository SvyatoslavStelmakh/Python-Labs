import numpy as np

def calculate_journey(lengths, speeds, start, end):
    
    if len(lengths) != len(speeds):
        print("Ошибка: количество участков дороги и скоростей не совпадает.")
        return
    
    if start < 1 or end < 1 or start > len(lengths) or end > len(lengths) or start > end:
        print("Ошибка: некорректные номера участков!")
        return
    
    start_index = start - 1
    end_index = end - 1
    
    selected_lengths = lengths[start_index:(end_index + 1)]
    selected_speeds = speeds[start_index:(end_index + 1)]
    
    distance = np.sum(selected_lengths)
    time_per_sections = selected_lengths / selected_speeds
    total_time = np.sum(time_per_sections)
    average_speed = distance / total_time if total_time > 0 else 0
    

    print(f"Длины: {selected_lengths}")
    print(f"Скорости: {selected_speeds}")
    
    print(f"\nS = {distance:.2f} км")
    print(f"T = {total_time:.2f} час")
    print(f"<V> {average_speed:.2f} км/ч")
    

if __name__ == "__main__":

    lengths_input = input("Введите длины участков через пробел: ")
    lengths = np.array(list(map(float, lengths_input.split())))
        
    speeds_input = input("Введите скорости на участках через пробел: ")
    speeds = np.array(list(map(float, speeds_input.split())))
        
    start = int(input("Номер участка въезда (k): "))
    end = int(input("Номер участка съезда (p): "))
   
    calculate_journey(lengths, speeds, start, end)
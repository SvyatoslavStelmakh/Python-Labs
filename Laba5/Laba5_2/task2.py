def find_unique(elements):
    unique_elements = []
    
    for item in elements:
        if elements.count(item) == 1:
            unique_elements.append(item)
            
    return unique_elements


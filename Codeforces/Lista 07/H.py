def calculate_max_score(num_boxes):
    current_score = 100
    max_score = 100

    for i in range(num_boxes):
        box_value = int(input())
        current_score += box_value
        
        if current_score > max_score:
            max_score = current_score

    return max_score


total_boxes = int(input())
final_score = calculate_max_score(total_boxes)
print(final_score)
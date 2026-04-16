"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    rounded_list = []
    for score in student_scores:
        rounded_list.append(round(score))
    
    # Return the full list AFTER the loop finishes
    return rounded_list
        
    pass


def count_failed_students(student_scores):
    exam_passed = 0
    
    for score in student_scores:
        if score <= 40:
            exam_passed = exam_passed +1
    return exam_passed

    pass


def above_threshold(student_scores, threshold):
    threshold_list = []
    for score in student_scores:
        if score >= threshold:
            threshold_list.append(score)

    return threshold_list
    pass


def letter_grades(highest):
    step = (highest - 40) // 4
    return [41 + (step * i) for i in range(4)]

    pass


def student_ranking(student_scores, student_names):
    rankings = []
    for index, (name, score) in enumerate(zip(student_names, student_scores), 1):
        rankings.append(f"{index}. {name}: {score}")

    return rankings
    
    pass


def perfect_score(student_info):
    for name, score in student_info:
        if score == 100:
            return [name, score]
        
    return []
    
    pass

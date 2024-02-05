def calculate_gpa(mark):
    try:
        mark = float(mark)
        if mark < 0 or mark > 100:
            raise ValueError("Mark should be between 0 and 100")
        elif mark >= 90:
            return 4.0
        elif mark >= 80:
            return 3.0
        elif mark >= 70:
            return 2.0
        elif mark >= 60:
            return 1.0
        else:
            return 0.0
    except ValueError as e:
        print(f"Error: {e}")
        if(mark == -1):
            raise e;
        return None

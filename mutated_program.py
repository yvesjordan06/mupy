# Original Program
def calculate_gpa(mark):
    haspass = mark > 50
    extramark = 10
    mark = mark + extramark
    extramark -= 5
    try:
        mark = float(mark)
        if mark < 0 or mark > 100:
            raise ValueError('Mark should be between 0 and 100')
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
        print(f'Error: {e}')
        return None

# Arith Op Mutation 0
def calculate_gpa(mark):
    haspass = mark > 50
    extramark = 10
    mark = mark + extramark
    extramark -= 5
    try:
        mark = float(mark)
        if mark < 0 or mark > 100:
            raise ValueError('Mark should be between 0 and 100')
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
        print(f'Error: {e}')
        return None

# Differences0
"""  def calculate_gpa(mark):
      haspass = mark > 50
      extramark = 10
      mark = mark + extramark
      extramark -= 5
      try:
          mark = float(mark)
          if mark < 0 or mark > 100:
              raise ValueError('Mark should be between 0 and 100')
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
          print(f'Error: {e}')
          return None"""


# Arith Op Mutation 1
def calculate_gpa(mark):
    haspass = mark > 50
    extramark = 10
    mark = mark - extramark
    extramark -= 5
    try:
        mark = float(mark)
        if mark < 0 or mark > 100:
            raise ValueError('Mark should be between 0 and 100')
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
        print(f'Error: {e}')
        return None

# Differences1
"""  def calculate_gpa(mark):
      haspass = mark > 50
      extramark = 10
-     mark = mark + extramark
?                 ^

+     mark = mark - extramark
?                 ^

      extramark -= 5
      try:
          mark = float(mark)
          if mark < 0 or mark > 100:
              raise ValueError('Mark should be between 0 and 100')
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
          print(f'Error: {e}')
          return None"""


# Arith Op Mutation 2
def calculate_gpa(mark):
    haspass = mark > 50
    extramark = 10
    mark = mark * extramark
    extramark -= 5
    try:
        mark = float(mark)
        if mark < 0 or mark > 100:
            raise ValueError('Mark should be between 0 and 100')
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
        print(f'Error: {e}')
        return None

# Differences2
"""  def calculate_gpa(mark):
      haspass = mark > 50
      extramark = 10
-     mark = mark + extramark
?                 ^

+     mark = mark * extramark
?                 ^

      extramark -= 5
      try:
          mark = float(mark)
          if mark < 0 or mark > 100:
              raise ValueError('Mark should be between 0 and 100')
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
          print(f'Error: {e}')
          return None"""


# Arith Op Mutation 3
def calculate_gpa(mark):
    haspass = mark > 50
    extramark = 10
    mark = mark / extramark
    extramark -= 5
    try:
        mark = float(mark)
        if mark < 0 or mark > 100:
            raise ValueError('Mark should be between 0 and 100')
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
        print(f'Error: {e}')
        return None

# Differences3
"""  def calculate_gpa(mark):
      haspass = mark > 50
      extramark = 10
-     mark = mark + extramark
?                 ^

+     mark = mark / extramark
?                 ^

      extramark -= 5
      try:
          mark = float(mark)
          if mark < 0 or mark > 100:
              raise ValueError('Mark should be between 0 and 100')
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
          print(f'Error: {e}')
          return None"""


# Arith Op Mutation 4
def calculate_gpa(mark):
    haspass = mark > 50
    extramark = 10
    mark = mark % extramark
    extramark -= 5
    try:
        mark = float(mark)
        if mark < 0 or mark > 100:
            raise ValueError('Mark should be between 0 and 100')
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
        print(f'Error: {e}')
        return None

# Differences4
"""  def calculate_gpa(mark):
      haspass = mark > 50
      extramark = 10
-     mark = mark + extramark
?                 ^

+     mark = mark % extramark
?                 ^

      extramark -= 5
      try:
          mark = float(mark)
          if mark < 0 or mark > 100:
              raise ValueError('Mark should be between 0 and 100')
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
          print(f'Error: {e}')
          return None"""


# Arith Op Mutation 5
def calculate_gpa(mark):
    haspass = mark > 50
    extramark = 10
    mark = mark + 0
    extramark -= 5
    try:
        mark = float(mark)
        if mark < 0 or mark > 100:
            raise ValueError('Mark should be between 0 and 100')
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
        print(f'Error: {e}')
        return None

# Differences5
"""  def calculate_gpa(mark):
      haspass = mark > 50
      extramark = 10
-     mark = mark + extramark
?                   ^^^^^^^^^

+     mark = mark + 0
?                   ^

      extramark -= 5
      try:
          mark = float(mark)
          if mark < 0 or mark > 100:
              raise ValueError('Mark should be between 0 and 100')
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
          print(f'Error: {e}')
          return None"""


# Arith Op Mutation 6
def calculate_gpa(mark):
    haspass = mark > 50
    extramark = 10
    mark = mark + extramark
    extramark += 5
    try:
        mark = float(mark)
        if mark < 0 or mark > 100:
            raise ValueError('Mark should be between 0 and 100')
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
        print(f'Error: {e}')
        return None

# Differences6
"""  def calculate_gpa(mark):
      haspass = mark > 50
      extramark = 10
      mark = mark + extramark
-     extramark -= 5
?               ^

+     extramark += 5
?               ^

      try:
          mark = float(mark)
          if mark < 0 or mark > 100:
              raise ValueError('Mark should be between 0 and 100')
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
          print(f'Error: {e}')
          return None"""


# Arith Op Mutation 7
def calculate_gpa(mark):
    haspass = mark > 50
    extramark = 10
    mark = mark + extramark
    extramark -= 5
    try:
        mark = float(mark)
        if mark < 0 or mark > 100:
            raise ValueError('Mark should be between 0 and 100')
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
        print(f'Error: {e}')
        return None

# Differences7
"""  def calculate_gpa(mark):
      haspass = mark > 50
      extramark = 10
      mark = mark + extramark
      extramark -= 5
      try:
          mark = float(mark)
          if mark < 0 or mark > 100:
              raise ValueError('Mark should be between 0 and 100')
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
          print(f'Error: {e}')
          return None"""


# Arith Op Mutation 8
def calculate_gpa(mark):
    haspass = mark > 50
    extramark = 10
    mark = mark + extramark
    extramark *= 5
    try:
        mark = float(mark)
        if mark < 0 or mark > 100:
            raise ValueError('Mark should be between 0 and 100')
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
        print(f'Error: {e}')
        return None

# Differences8
"""  def calculate_gpa(mark):
      haspass = mark > 50
      extramark = 10
      mark = mark + extramark
-     extramark -= 5
?               ^

+     extramark *= 5
?               ^

      try:
          mark = float(mark)
          if mark < 0 or mark > 100:
              raise ValueError('Mark should be between 0 and 100')
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
          print(f'Error: {e}')
          return None"""


# Arith Op Mutation 9
def calculate_gpa(mark):
    haspass = mark > 50
    extramark = 10
    mark = mark + extramark
    extramark /= 5
    try:
        mark = float(mark)
        if mark < 0 or mark > 100:
            raise ValueError('Mark should be between 0 and 100')
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
        print(f'Error: {e}')
        return None

# Differences9
"""  def calculate_gpa(mark):
      haspass = mark > 50
      extramark = 10
      mark = mark + extramark
-     extramark -= 5
?               ^

+     extramark /= 5
?               ^

      try:
          mark = float(mark)
          if mark < 0 or mark > 100:
              raise ValueError('Mark should be between 0 and 100')
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
          print(f'Error: {e}')
          return None"""


# Arith Op Mutation 10
def calculate_gpa(mark):
    haspass = mark > 50
    extramark = 10
    mark = mark + extramark
    extramark %= 5
    try:
        mark = float(mark)
        if mark < 0 or mark > 100:
            raise ValueError('Mark should be between 0 and 100')
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
        print(f'Error: {e}')
        return None

# Differences10
"""  def calculate_gpa(mark):
      haspass = mark > 50
      extramark = 10
      mark = mark + extramark
-     extramark -= 5
?               ^

+     extramark %= 5
?               ^

      try:
          mark = float(mark)
          if mark < 0 or mark > 100:
              raise ValueError('Mark should be between 0 and 100')
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
          print(f'Error: {e}')
          return None"""



# http://practice.geeksforgeeks.org/problems/x-total-shapes/0

class Element:
    def __init__(self, value):
        self.value = value
        self.visit = False

    def __repr__(self):
        return "(%s,%s)"%(self.value, self.visit)

class Terrain:
    def __init__(self, shape, string_input):
        self.height = shape[0]
        self.width = shape[1]
        self.terrain = string_input.split(' ')

    def find_bunker(self):
        visit_map = []
        for line in self.terrain:
            row = []
            for x in line:
                # (value, visited)
                row.append(Element(x))
            visit_map.append(row)

        def bunker_recurse(row, col):
            elem = visit_map[row][col]
            if elem.visit:
                return False
            elem.visit = True
            if elem.value == 'O':
                return False

            def should_visit(element):
                return not element.visit and element.value == 'X'

            # search left, right, down, up
            if col > 0:
                left = visit_map[row][col-1]
                if should_visit(left):
                    bunker_recurse(row, col-1)
            if col + 1 != self.width:
                right = visit_map[row][col+1]
                if should_visit(right):
                    bunker_recurse(row, col+1)
            if row > 0:
                up = visit_map[row-1][col]
                if should_visit(up):
                    bunker_recurse(row-1, col)
            if row + 1 != self.height:
                down = visit_map[row+1][col]
                if should_visit(down):
                    bunker_recurse(row+1, col)

            return True

        count = 0
        for y in range(self.height):
            line = visit_map[y]
            for x in range(self.width):
                if bunker_recurse(y, x):
                    count += 1
        return count


if __name__ == "__main__":
    num_cases = int(input())
    results = []
    for _ in range(num_cases):
        str_input = input()
        shapes = str_input.split(' ')
        height = int(shapes[0])
        width = int(shapes[1])
        str_input = input()
        terrain = Terrain((height, width), str_input)
        results.append(terrain.find_bunker())
    
    for value in results:
        print(value)

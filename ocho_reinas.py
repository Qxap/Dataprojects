def solucion():

    solutions = []

    def backtrack(row, cols, d1, d2, board):
       # Condición inicial de probamiento
        if row == 8:
            solutions.append(board.copy())
            return

        for col in range(8):

            if col in cols or (row + col) in d1 or (row - col) in d2:
                continue
            # Por cada columna haces el probamiento de filas
            backtrack(
                row + 1,
                cols | {col},
                d1 | {row + col},
                d2 | {row - col},
                board + [col]
            )

    backtrack(0, set(), set(), set(), [])

    return solutions


solutions = solucion()

print(f"numero de soluciones: {len(solutions)}")
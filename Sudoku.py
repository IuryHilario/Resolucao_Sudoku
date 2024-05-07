from tkinter import *
import tkinter.font as tkFont
from tkinter import messagebox


class Solver_Sudoku(Tk):
    def __init__(self):
        super().__init__()

        # Configurações da tela
        self.title('Resolver Tabela Sudoku')
        self['bg'] = 'black'
        self.resizable(0, 0)
        self.geometry('+500+0')

        self.font = tkFont.Font(family="Helvetica", size=50)
        self.pixel = PhotoImage(width=1, height=1)

        self.erase_mode = False

        self.Layout()

    def Layout(self):
        # Layout invisivel
        self.table = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0]]

        # Inicializa a matriz de entrada do usuário com zeros
        self.user_input = [[0 for _ in range(9)] for _ in range(9)]

        # Desenha a tabela na tela
        for row in range(9):
            for column in range(9):
                if row in (0, 1, 2, 6, 7, 8) and column in (3, 4, 5) or (
                        row in (3, 4, 5) and column in (0, 1, 2, 6, 7, 8)):
                    color_separation = 'light blue'

                else:
                    color_separation = 'white'

                self.square = Button(self, text=' ', bg=color_separation, font=self.font, image=self.pixel, width=50,
                                     height=50, compound="center",
                                     command=lambda L=row, C=column: self.Aumento_Dos_Numeros(L, C))
                self.square.grid(row=row, column=column, padx=1, pady=1)

        # Adicionando o Resolver, Reset e Apagar
        menu_widget = Menu(self)
        menu_widget.add_cascade(label='Resolver', command=self.Solve_Sudoku)
        menu_widget.add_cascade(label='Reset', command=self.Reset)
        menu_widget.add_cascade(label='Apagar', command=self.Erase)

        self.config(menu=menu_widget)

    def Aumento_Dos_Numeros(self, N1, N2):
        # Apagar tal número desejado
        if self.erase_mode:
            self.table[N1][N2] = 0
            self.erase_mode = False

        else:
            if self.table[N1][N2] >= 9:
                self.table[N1][N2] = -1

            # Cores de separação
            if N1 in (0, 1, 2, 6, 7, 8) and N2 in (3, 4, 5) or (N1 in (3, 4, 5) and N2 in (0, 1, 2, 6, 7, 8)):
                self.color_separation = 'light blue'
            else:
                self.color_separation = 'white'

            # Verifica se o número já existe na mesma linha, coluna ou quadrado 3x3
            num = self.table[N1][N2] + 1
            while num <= 9 and not self.solve(self.table, N1, N2, num):
                num += 1

            # Se nenhum número válido foi encontrado, define como 0
            if num > 9:
                num = 0
                messagebox.showerror("Erro", f"Há um erro na linha {N1 + 1}, coluna {N2 + 1}")

            self.table[N1][N2] = num

        # Se o número foi inserido pelo usuário, define a cor do texto como preto, se não, verde escuro
        if self.table[N1][N2] != 0 and self.table[N1][N2] != " ":
            self.user_input[N1][N2] = 1
            text_color = 'black'
        else:
            text_color = 'dark green'

        self.square = Button(self, font=self.font, image=self.pixel, width=50, height=50, compound="center",
                             text=self.table[N1][N2] if self.table[N1][N2] != 0 else ' ', bg=self.color_separation,
                             fg=text_color,
                             command=lambda L=N1, C=N2: self.Aumento_Dos_Numeros(L, C))
        self.square.grid(row=N1, column=N2, padx=1, pady=1)

    def Erase(self):
        # Ativar o modo apagar
        self.erase_mode = True

    # Verificação da tabela
    def solve(self, grid, row, column, num):
        # Verificar se existe números repetidos na horizontal e vertical
        for x in range(9):
            if grid[row][x] == num or grid[x][column] == num:
                return False

        Start_Row = row - row % 3
        Start_Column = column - column % 3

        # Verifica se existe números repitidos no quadrado 3 x 3
        for i in range(3):
            for j in range(3):
                if grid[i + Start_Row][j + Start_Column] == num:
                    return False

        return True

    # Resolver a tabela
    def Solve_Sudoku(self):
        sudoku = self.table
        sudoku_range = 9
        # Desenhando a nova tabela
        def puzzle(a):
            for N1 in range(9):
                for N2 in range(9):
                    if N1 in (0, 1, 2, 6, 7, 8) and N2 in (3, 4, 5) or (N1 in (3, 4, 5) and N2 in (0, 1, 2, 6, 7, 8)):
                        color_separation = 'light blue'

                    else:
                        color_separation = 'white'

                    # Se o número foi inserido pelo usuário, define a cor do texto como preto, se não, verde escuro
                    if self.user_input[N1][N2] == 1 and self.table[N1][N2] != ' ':
                        text_color = 'black'
                    else:
                        text_color = 'dark green'

                    self.square = Button(self, font=self.font, image=self.pixel, width=50, height=50,
                                         compound="center", text=self.table[N1][N2] if self.table[N1][N2] != 0 else ' ',
                                         bg=color_separation, fg=text_color)
                    self.square.grid(row=N1, column=N2, padx=1, pady=1)


        def Suduko(grid, row, column):
            # Verifica se passou pelas linhas e colunas
            if row == sudoku_range - 1 and column == sudoku_range:
                return True

            # Caso passe do range de colunas, ele reseta (= 0) e passa para próxima linha
            if column == sudoku_range:
                row += 1
                column = 0

            # Caso tenha número, ela passa para o próximo
            if grid[row][column] > 0:
                return Suduko(grid, row, column + 1)

            for num in range(1, sudoku_range + 1, 1):
                if self.solve(grid, row, column, num):
                    # Ela tenta preencher um número valido
                    grid[row][column] = num

                    if Suduko(grid, row, column + 1):
                        # Se tudo preenchido, então é True
                        return True

                # Apaga o número e tenta colocar outro
                grid[row][column] = 0

            return False

        if Suduko(sudoku, 0, 0):
            # Resolver
            puzzle(sudoku)

        else:
            # Caso falhe, imprimir error
            print('Error')

    def Reset(self):
        # Resetar a tela
        try:
            self.destroy()

        except:
            pass

        self.__init__()


if __name__ == '__main__':
    Solver_Sudoku().mainloop()

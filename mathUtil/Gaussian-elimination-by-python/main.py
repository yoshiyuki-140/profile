# coding:utf-8
# author : Yoshiyuki Kurose
# this code defined the 3x3 matrix's gaussian_ellimination by using python language

# import doctest


class Gaussian_ellimination:
    def __init__(self, dimension=3):
        """
        the dimension of matrix is defaultly three
        """
        self.dimension = dimension
        self.matrix = [[]]
        self.inverse_matrix = [[]]

    def ask_dimension(self):
        dimension = int(input("How many dimensions? : "))
        if dimension < 1:
            raise ValueError("The dimension must be more than 1")
        else:
            self.dimension = dimension

    def ask_matix(self):
        """
        """
        self.matrix = [[int(x) for x in input(f"Please input {i+1} row of the matrix >> ").split()]
                       for i in range(self.dimension)]

    def print_inverse_matrix(self):
        for i in range(self.dimension):
            print(self.matrix[i][self.dimension:])

    def make_augumented_matrix(self):
        for n in range(self.dimension):
            for m in range(self.dimension):
                if n == m:
                    self.matrix[n].append(1)
                else:
                    self.matrix[n].append(0)

    def change_matrix(self, n, m):
        """
        XxY matrix
        """
        z = self.matrix[n-1][m-1]
        if z == 0:
            raise ValueError("this matrix haven't the inverse matrix")
        tmp_matrix = self.get_matrix()
        self.matrix[n-1] = [tmp_matrix[n-1][y] /
                            z for y in range(self.dimension*2)]

    def change_matrix2(self, n1, n2, m2):
        """
        matrix = [
        [a,b,c],
        [d,e,f],
        [g,h,i]
        ]
        n1 is 1, n2 is 2, m2 is 1, then "d - a * d" is expressed like this
        ###
        pass

        """
        tmp_matrix = self.get_matrix()
        n = tmp_matrix[n2-1][m2-1]
        self.matrix[n2-1] = [tmp_matrix[n2-1][i] -
                             (tmp_matrix[n1-1][i] * n) for i in range(self.dimension * 2)]

    def main_3x3_algolithm(self):
        """
        下の main_algolithm の内容がわかりやすいように3x3の時のアルゴリズムを残しておく。
        """
        self.ask_matix()
        self.make_augumented_matrix()
        self.change_matrix(1, 1)
        self.change_matrix2(1, 2, 1)
        self.change_matrix2(1, 3, 1)
        self.change_matrix(2, 2)
        self.change_matrix2(2, 1, 2)
        self.change_matrix2(2, 3, 2)
        self.change_matrix(3, 3)
        self.change_matrix2(3, 1, 3)
        self.change_matrix2(3, 2, 3)

    def main_algolithm(self):
        """
        this code is main algorithm
        """
        self.ask_dimension()
        self.ask_matix()
        self.make_augumented_matrix()
        for i in range(1, self.dimension+1):
            self.change_matrix(i, i)
            for k in range(1, self.dimension+1):
                if i != k:
                    self.change_matrix2(i, k, i)

        self.print_inverse_matrix()

    def get_matrix(self):
        return self.matrix

    def only_algolithm(self):
        self.make_augumented_matrix()
        for i in range(1, self.dimension+1):
            self.change_matrix(i, i)
            # In tmp_list, It contain other than i.
            # tmp_list = [x for x in range(1, self.dimension+1) if i != x]
            # for k in [x for x in range(1,self.dimension+1) if i != x]:
            #     self.change_matrix2(i, k, i)

            for k in range(1, self.dimension+1):
                if i != k:
                    self.change_matrix2(i, k, i)


def main():
    G = Gaussian_ellimination()
    G.main_algolithm()


if __name__ == "__main__":
    main()

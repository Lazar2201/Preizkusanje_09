import sys
import random
from unittest.mock import patch


class Node:
    def __init__(self):
        self.prev = -1
        self.distance = 0


class BF:
    def __init__(self):
        self.node_matrix = []
        self.paths = []

    def readGraph(self, filename):
        with open(filename, 'r') as graph:
            N = int(graph.readline())
            if N > 0:
                self.clearMatrix()
            for _ in range(N):
                row = list(map(int, graph.readline().split()))
                self.node_matrix.append(row)

    def startAlgorithm(self, source):
        if not self.node_matrix:
            return -1
        self.paths.clear()
        N = len(self.node_matrix)
        for i in range(N):
            temp = Node()
            if i != source:
                temp.distance = sys.maxsize // 2 - 1
            self.paths.append(temp)
        for _ in range(N - 1):
            for i in range(N):
                for j in range(N):
                    if (self.paths[i].distance + self.node_matrix[i][j] <
                            self.paths[j].distance):
                        self.paths[j].distance = (
                            self.paths[i].distance + self.node_matrix[i][j]
                        )
                        self.paths[j].prev = i
        for i in range(N):
            for j in range(N):
                if (self.paths[i].distance + self.node_matrix[i][j] <
                        self.paths[j].distance):
                    print("GREŠKA: Negativan ciklus.")
                    return 0
        return 0

    def printAttribute(self, node_num):
        if not self.node_matrix:
            return -1
        elif not self.paths:
            return -2
        print("Cena poti:", self.paths[node_num].distance)
        print("Predhodnik:", self.paths[node_num].prev)
        return 0

    def printShortestPath(self, destination):
        if not self.node_matrix:
            return -1
        elif not self.paths:
            return -2
        if destination > len(self.paths) - 1:
            print("Node doesn't exist")
            return 0
        path = [destination]
        cnt = destination
        while self.paths[cnt].prev != -1:
            path.append(self.paths[cnt].prev)
            cnt = self.paths[cnt].prev
        path.reverse()
        print("Najkraća putanja:", ' -> '.join(map(str, path)))
        return 0

    def generateRandGraph(self, N, lower_lim, upper_lim):
        self.clearMatrix()
        for _ in range(N):
            row = []
            for _ in range(N):
                temp = random.randint(lower_lim, upper_lim)
                row.append(temp)
            self.node_matrix.append(row)

    def clearMatrix(self):
        self.node_matrix = []


def printMenu():
    print("Bellman-Fordov algoritem - izbira:")
    print("1) Preberi graf iz datoteke")
    print("2) Generiraj nakljucni graf z n vozlisci")
    print("3) Poženi algoritem")
    print("4) Ispisi seznam vozlisc")
    print("5) Ispisi najkrajso pot")
    print("6) Konec")


def initGraph():
    print(
        "Greška: graf nije inicijalizovan! Izaberite opciju 1 ili 2, "
        "a zatim 3, pre nego što pokušate 4!"
    )


def BF_app():
    print(
        "Greška: Bellman-Ford algoritam nije primenjen! Izaberite opciju 3 "
        "pre nego što pokušate 4!"
    )


def main():
    select = 0
    program = BF()

    while True:
        printMenu()
        select = int(input())
        if select == 1:
            file_name = input("Ime datoteke:\n")
            program.readGraph(file_name)
        elif select == 2:
            N = int(input("N:\n"))
            a = int(input("a:\n"))
            b = int(input("b:\n"))
            program.generateRandGraph(N, a, b)
        elif select == 3:
            source = int(input("Izvor:\n"))
            error = program.startAlgorithm(source)
            if error == -1:
                initGraph()
        elif select == 4:
            node = int(input("Broj čvora:\n"))
            error = program.printAttribute(node)
            if error == -1:
                initGraph()
            elif error == -2:
                BF_app()
        elif select == 5:
            destination = int(input("Destinacija:\n"))
            error = program.printShortestPath(destination)
            if error == -1:
                initGraph()
            elif error == -2:
                BF_app()
        elif select == 6:
            break


if __name__ == "__main__":
    # Define the sequence of inputs to simulate user interaction
    inputs = iter([
        '2', '5', '1', '10',  
        '3', '0',              # Run algorithm starting from node 0
        '4', '2',              # Print attributes of node 2
        '5', '4',              # Print shortest path to node 4
        '6'                    # Exit
    ])

    with patch('builtins.input', lambda _: next(inputs)):
        main()

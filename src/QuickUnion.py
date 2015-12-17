# encoding: utf-8
# module Union-Find

"""
 This is the second algorithm of three algorithms that about how
 to resolve the union-find problem.

 The contents of the three file include in file directory:

     10sites, 11 connected                file/tinyUF.txt
     625sites, 900 connected              file/mediumUF.txt
     1 million sites, 2 million sites     file/largeUF.txt

"""
# import time
# class


import time


class QuickUnion:
    ids = []
    """ The id of each component """
    levels = []
    """ The level of each component """
    weights = []
    """ The count of sites in each component """

    @classmethod
    def find(cls, site):
        """
        To find the root id of each site's component
        :param site: The site that want to find
                its component's number
        :return: The id of the special site's
                component.

        """

        while site != cls.ids[site]:
            site = cls.ids[site]
        return cls.ids[site]

    @classmethod
    def connected(cls, p, q):
        """
        To test if those two site is in the same component
        :param p: The parameter in left.
        :param q: The parameter in right.
        :return: A bool value.
        """
        return cls.find(p) == cls.find(q)

    @classmethod
    def union(cls, p, q):
        """
        To union the two site if they have not union before
        :param p: The parameter in left.
        :param q: The parameter in right.
        :return: none
        """
        proot = cls.find(p)
        qroot = cls.find(q)
        cls.ids[proot] = qroot
        cls.weights[qroot] += cls.weights[proot]

        levelp = cls.levels[proot]
        levelq = cls.levels[qroot]
        if levelq < levelp:
            cls.levels[q] = levelp + 1
        elif levelq == levelp:
            cls.levels[q] += 1
        else:
            return

    @classmethod
    def iter_tree(cls, scale):
        total = 0
        for i in range(int(scale)):
            if i == cls.ids[i]:
                print("The component which id is:", i, ",having ", cls.weights[i], "sites")
                total += 1
        print("Total have ", total, "component.")

    # Initialize
    """
    * Reads in a an integer N and a sequence of pairs of integers
    * (between 0 and N-1) from standard input, where each integer
    * in the pair represents some site;
    * if the sites are in different components, merge the two components
    * and print the pair to standard output.
    """

    def __init__(self):

        inputscale = input("Please input the scale of input file(Tiny, Medium, Large)\n Please type: T, M, L ?  ")
        """ Input the scale of input file. """
        scale = 0
        pathname = ""
        if "T".__eq__(inputscale):
            scale = 10
            pathname = "../file/tinyUF.txt"
        elif "M".__eq__(inputscale):
            scale = 625
            pathname = "../file/mediumUF.txt"
        elif "L".__eq__(inputscale):
            scale = 1000000
            pathname = "../file/largeUF.txt"
        else:
            print("Input error! Please input T、M or L!")
            exit()

        for i in range(scale):
            self.ids.append(i)
            self.levels.append(1)
            self.weights.append(1)

        f = open(pathname)
        for line in f:
            data = line.split()
            p = int(data[0])
            q = int(data[1])
            if self.connected(p, q):
                continue
            self.union(p, q)
            print(p, q)

        f.close()
        self.iter_tree(scale)


quickFind = QuickUnion()
print("The max level is:", max(quickFind.levels), "\n",
      "The max weight is", max(quickFind.weights), "\n",
      "Time elapsed: ", time.process_time(), "seconds")

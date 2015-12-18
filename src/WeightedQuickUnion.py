# encoding: utf-8
# module Union-Find
# License: GPL v2
# Author: andersion.v@gmail.com
"""
 This is the third algorithm of three algorithms that about how
 to resolve the union-find problem.

 The contents of the three file include in file directory:

     10sites, 11 connected                file/tinyUF.txt
     625sites, 900 connected              file/mediumUF.txt
     1 million sites, 2 million sites     file/largeUF.txt

"""
# import time
# class

import time
import sys

class WeightedQuickUnion:
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

        levelp = cls.levels[proot]
        levelq = cls.levels[qroot]

        weight_p = cls.weights[proot]
        weight_q = cls.weights[qroot]

        if weight_p < weight_q:
            cls.ids[proot] = qroot
            cls.weights[qroot] += weight_p
            if levelq > levelp:
                return
            elif levelq == levelp:
                cls.levels[qroot] += 1
            else:
                cls.levels[qroot] = levelp + 1

        else:
            cls.ids[qroot] = proot;
            cls.weights[proot] += weight_q
            if levelq > levelp:
                cls.levels[proot] = levelq + 1
            elif levelq == levelp:
                cls.levels[proot] += 1
            else:
                return


    @classmethod
    def iter_tree(cls, scale):
        """

        :param scale: The scale of input file
        :return: None.Just print each component's weight.
        """
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
        group = 0
        pathname = ""
        if "T".__eq__(inputscale):
            scale = 10
            group = 11
            pathname = "../file/tinyUF.txt"
        elif "M".__eq__(inputscale):
            scale = 625
            group = 900
            pathname = "../file/mediumUF.txt"
        elif "L".__eq__(inputscale):
            scale = 1000000
            group = 2000000
            pathname = "../file/largeUF.txt"
        else:
            print("Input error! Please input T、M or L!")
            exit()

        for i in range(scale):
            self.ids.append(i)
            self.levels.append(1)
            self.weights.append(1)
        """
        self.ids = [x for x in range(scale)]
        self.levels = [1 for x in range(scale)]
        self.weights= [1 for x in range(scale)]
        """

        readed = 0
        elapsed = 0

        j = "#"
        i = 0.01
        f = open(pathname)
        for line in f:
            data = line.split()
            p = int(data[0])
            q = int(data[1])
            if self.connected(p, q):
                continue
            self.union(p, q)
            # print(p, q)

            readed += 1

            j += '#'
            # sys.stdout.write(str(int((readed / scale) * 100)) + '%  ||' + j + '->' + "\r")
            test = float(readed / group)
            if float(readed / group) > i:
                sys.stdout.write(str(int((readed / scale) * 100)) + '%  ||' + j + '->' + "\r")
                i = ("%.2f" % test)
                print()
                sys.stdout.flush()


        f.close()
        self.iter_tree(scale)


weightedquickFind = WeightedQuickUnion()
print("The max level is:", max(weightedquickFind.levels), "\n",
      "The max weight is", max(weightedquickFind.weights), "\n",
      "Time elapsed: ", time.process_time(), "seconds")

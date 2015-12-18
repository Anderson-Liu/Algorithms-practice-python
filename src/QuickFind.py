# encoding: utf-8
# module Union-Find
# License: GPL v2
# Author: andersion.v@gmail.com
"""
 This is the first algorithm of three algorithms that about how
 to resolve the union-find problem.

 The contents of the three file include in file directory:

     10sites, 11 connected                file/tinyUF.txt
     625sites, 900 connected              file/mediumUF.txt
     1 million sites, 2 million sites     file/largeUF.txt

"""
# import time
# class

import time


class QuickFind:

    ids = []
    """ The id of each component """

    @classmethod
    def find(cls, site):
        """
        To find the id of each site's component
        :param site: The site that want to find
                its component's number
        :return:
        """
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
        pid = cls.ids[p]
        for num in range(len(cls.ids)):
            if cls.ids[num] == pid:
                cls.ids[num] = cls.ids[q]

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
            return

        for i in range(scale):
            self.ids.append(i)

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

quickFind = QuickFind()
print("Time elapsed: ", time.process_time(), "seconds")
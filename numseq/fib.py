#!/usr/local/env/ python
# -*- coding: utf-8 -*-

__author__ = 'Tiffany McLean with the help of a lot of googling'


def fib(n):
    """
    should return the nth Fibonacci number
    """

    a, b = 0, 1
    num = 0
    while num < n:
        a, b = b, a + b
        num += 1
    return a
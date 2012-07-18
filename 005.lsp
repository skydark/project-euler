#!/usr/bin/newlisp

(define NUM 20)

(load "math.lsp")

(println (apply lcm (sequence 1 NUM)))

(exit)

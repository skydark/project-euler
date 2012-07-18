#!/usr/bin/newlisp

(define NUM 100)

(load "math.lsp")

(define seq (sequence 1 NUM))

(println
  (-
    (square (apply + seq))
    (apply + (map square seq))))

(exit)

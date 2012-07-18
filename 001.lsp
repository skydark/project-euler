#!/usr/bin/newlisp

(define MAX 1000)

(define (test x)
  (or
    (= (% x 3) 0)
    (= (% x 5) 0)))

(println
  (apply + (filter test (sequence 1 (- MAX 1))))
  )

(exit)

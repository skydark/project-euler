#lang racket

(define n 64000000)
(define pool
  (for/vector #:length n
              ([k (in-range n)])
              (+ (* k k) 1)))
(vector-set! pool 1 1)
(for ([k (in-range 2 (quotient (+ n 1) 2))])
     (let ((k2 (* k k)))
       (for ([m (in-range (* k 2) n k)])
            (vector-set! pool m
                         (+ (vector-ref pool m) k2)))))
(define (quad? n)
  (= (- n (expt (integer-sqrt n) 2)) 0))
(define sum
  (for/fold ([s 0])
            ([i (in-naturals 0)]
             [m (in-vector pool)]
             #:when (quad? m))
            (+ s i)))
(display sum)

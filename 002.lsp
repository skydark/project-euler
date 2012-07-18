#!/usr/bin/newlisp

(define LIMIT 4000000)

(load "stream.lsp")

(define fibs
  (begin
    (define (fib a b)
      (expand (cons-stream a (fib b (+ a b))) 'a 'b))
    (fib 1 2)))

(define (pe2 limit)
  (apply + (stream-to-list 
             (filter-stream
               even?
               (takewhile-stream (curry > limit) fibs)))))

(println (pe2 LIMIT))

(exit)

; (define (pe2-normal limit)
;   (let ((a 1) (b 2) (s 0))
;     (begin
;       (until
;         (> a limit)
;         (if (even? a) (setf s (+ s a)))
;         (map set '(a b) (list b (+ a b)))
;         )
;       s)))

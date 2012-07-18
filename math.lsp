
(define (lcm)
  (letn (lst (args) len (length lst))
    (cond
      ((= len 0) (throw-error "ERR: missing argument in function lcm"))
      ((= len 1) (first lst))
      (true (begin
              (define (lcm2 a b)
                (/ (* a b) (gcd a b)))
              (apply lcm2 lst 2))))))

(define (square x) (* x x))


(load "stream.lsp")


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

; (define (enum-interval low high)
;    (if (> low high)
;       the-empty-stream
;       (expand (cons-stream low (enum-interval (+ low 1) high)) 'low 'high)
;    )
; )
; 
(define (integers-from n)
   (expand (cons-stream n (integers-from (+ n 1))) 'n)
)

(set 'integers (integers-from 1))

(define (divisible?)
  (letn (lst (args) len (length lst))
        (cond
          ((= len 0) (throw-error "ERR: missing argument in function `divisible?`"))
          ((= len 1)
           (letex (p (first lst))
             (lambda (x) (= (% x p)))))
          ((= len 2) (= (% (lst 0) (lst 1)) 0))
          ((> len 2) (throw-error "ERR: too many arguments in function `divisible?`")))
        )
  )

(define (not-divisible?)
  (letn (lst (args) len (length lst))
        (cond
          ((= len 0) (throw-error "ERR: missing argument in function `not-divisible?`"))
          ((= len 1)
           (letex (p (first lst))
             (lambda (x) (!= (% x p)))))
          ((= len 2) (!= (% (lst 0) (lst 1)) 0))
          ((> len 2) (throw-error "ERR: too many arguments in function `not-divisible?`")))
        )
  )

(define prime-stream
  (begin
    (define (sieve stream)
      (let (p (head stream))
        (expand 
          (cons-stream
            p
            (sieve (filter-stream
                     (not-divisible? p)
                     'stream)))
          'p 'stream)))
    (sieve (integers-from 2))
    )
  )

(define (primes)
  (begin
    (define (is-prime n known-primes)
      (catch
        (begin
          (let (sqrtn (int (sqrt n)))
            (dolist (p known-primes)
              (if
                (= 0 (% n p)) (throw nil)
                (> p sqrtn) (throw true))))
          true)))
    (define (_primes known-primes)
      (let (n (+ (last known-primes) 2))
        (until (is-prime n known-primes)
               (set 'n (+ n 2))
               )
        (push n known-primes -1)
        (list n _primes known-primes)
        )
      )
    (_primes '(3))
    )
  )
; (println "nth 20: " (nth-stream 20 integers))


(load "stream.lsp")
(load "math.lsp")

(define COUNT 10001)

; (println (nth-stream (- COUNT 1) prime-stream))

(map set '(p get-next-prime primes-pool) (primes))
;(set 'get-next-prime primes)

(for (i 4 COUNT)
     (map set '(p get-next-prime primes-pool) (get-next-prime primes-pool))
     ;(map set '(p get-next-prime) (get-next-prime))
     )

(println p)

(exit)

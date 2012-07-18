;; from http://newlispfanclub.alh.net/forum/viewtopic.php?t=2162


(set 'the-empty-stream '())

(define-macro (cons-stream)
   (letex (x (args 0) y (args 1))
      (cons x (list (delay y)))
   )
)

(define-macro (delay)
   (letex (x (args 0)) (fn () x))
   ;(letex (x (args 0)) (memo-proc (fn () x)))
)

(define (memo-proc)
   (letex (func (args 0))
      (fn ()
         (if (not already-run?)
            (begin
               (set 'result (func))
               (set 'already-run true)
            )
         )
         result
      )
   )
)

(define (head s)
   (first s)
)

(define (tail p)
   (force (last p))
)

(define (force func)
   (func)
)

(define (nth-stream n s)
   (if (= n 0)
      (head s)
      (nth-stream (- n 1) (tail s))
   )
)

(define (empty-stream? s)
   (empty? s)
)

(define (map-stream func s)
   (if (empty-stream? s)
      the-empty-stream
      (letex ((a (func (head s)))
            (b func)
            (c (tail s)))
         (cons-stream a (map-stream b c))
      )
   )
)

(define (filter-stream pred s)
   (cond
      ((empty-stream? s) the-empty-stream)
      ((pred (head s))
         (letex (a (head s)
               b pred
               c (tail s))
            (cons-stream a (filter-stream b 'c))
         )
      )
      (true (filter-stream pred (tail s)))
   )
)

(define (accumulate combiner init-val s)
   (if (empty-stream? s)
      init-val
      (combiner (head s) (accumulate combiner init-val (tail s)))
   )
)

(define (takewhile-stream pred s)
  (cond
    ((empty-stream? s) the-empty-stream)
    ((pred (head s))
     (letex (a (head s)
               b pred
               c (tail s))
            (cons-stream a (takewhile-stream b 'c))
            )
     )
    (true the-empty-stream)))

(define (stream-to-list s)
  (if (empty-stream? s)
    '()
    (cons (head s) (stream-to-list (tail s)))))

(define (print-stream s)
   (if (empty-stream? s)
      "done"
      (begin
         (print (head s) " ")
         (print-stream (tail s))
      )
   )
)

; (define (enum-interval low high)
;    (if (> low high)
;       the-empty-stream
;       (expand (cons-stream low (enum-interval (+ low 1) high)) 'low 'high)
;    )
; )
; 
; (define (integers-from n)
;    (expand (cons-stream n (integers-from (+ n 1))) 'n)
; )
; 
; (set 'integers (integers-from 1))
; (println "nth 20: " (nth-stream 20 integers))
; 
; (while true
;    (print "> ")
;    (read-line)
;    (if (= (current-line) "")
;       (exit)
;       (println (eval-string (current-line)))
;    )
; )
;
; (set 'ones (cons-stream 1 ones))

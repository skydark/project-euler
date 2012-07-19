
(define M 2000000)

(load "math.lsp")

(define uplimit (int (sqrt M)))

(define sum 2)

(define seq (array M '(true)))

(for (i 3 uplimit 2)
     (if
       (seq i)
       (begin
         (for (j (* i 3) M (* i 2))
              (setf (seq j) nil))
         (setq sum (+ sum i)))))

(setq uplimit (+ (* (/ uplimit 2) 2) 1))
(for (i uplimit M 2)
     (if (seq i)
       (setq sum (+ sum i))))

(println sum)

(exit)

; (define seq (sequence 3 M 2))

; (until
;   (> i uplimit)
;   (set 'i (first seq))
;   (set 'sum (+ sum i))
;   (set 'seq (filter (not-divisible? i) (rest seq)))
;   )

; (println (+ sum (apply + seq)))


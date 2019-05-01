(defun countt (lista listb)
  (cond 
    ((null lista) 0)
    ((char= (car lista) (car listb)) (+ 1 (countt (cdr lista) (cdr listb))) )
    (t (countt (cdr lista) (cdr listb)))))
    

(defvar right (read))
(defvar list1 (coerce (read-line) 'list))
(defvar list2 (coerce (read-line) 'list))
(defvar wrong (- (list-length list1) right))
(defvar same (countt list1 list2))
(defvar diff (- (list-length list1) same))
(format t "~d" (+ (min diff wrong) (min same right)))

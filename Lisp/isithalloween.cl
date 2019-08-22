(defvar x (read-line))
(cond ((string= x "OCT 31") (print 'yup))
      ((string= x "DEC 25") (print 'yup))
      (t (format t "~A" 'nope)))

(defvar out 0)
(defun count-cd(line)
  (cond ((null (cadr line)) nil)
        ((and (char= (car line) #\C) (char= (cadr line) #\D)) t)
        (t (count-cd (cdr line)))))

(loop for x from 1 to (read) do
      (if (not (count-cd (coerce (read-line) 'list))) (set 'out (1+ out)))) 
(format t "~d" out)


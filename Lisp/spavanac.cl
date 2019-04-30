(defvar x (- (+ (* 60 (read)) (read)) 45))
(defvar hour (mod (floor x 60) 24))
(defvar minute (mod x 60))
(format t "~d ~d" hour minute)

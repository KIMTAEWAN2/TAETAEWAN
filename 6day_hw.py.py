import turtle as t

t.bgcolor("black")
t.speed(0)

for x in range(100):
    
    if x%2 == 0:
        t.color("white")
    if x%2 == 1:
        t.color("pink")
    t.left(59)    
    
    
    for y in range(6):
        t.forward(x*2)
        t.rt(60)
        

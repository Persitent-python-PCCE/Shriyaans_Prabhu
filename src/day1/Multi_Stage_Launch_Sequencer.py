def launch(*stages,thresh_hold=5000):
    sum=0
    stage=1
    for i in range(len(stages)):
        sum+=stages[i]
        if sum<=thresh_hold:
            print(f"Sage {stage} armed --> cumulative {sum}kg")
            stage+=1
        else:
            print(f"Sage {stage} armed --> cumulative {sum}kg")
            print(f"[ABORT] at stage {stage}: threshold {thresh_hold} kg exceeded.")
            break
    
launch(1200, 1800, 2500, 200,3000)
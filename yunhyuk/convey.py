

level=[2,1,1]
person=[2,1,1]

start_plans=[]
end_plans=[]

for i in range(len(level)):
    s_plan=[]
    e_plan=[]
    p_time=0

    for j in range(len(person)):
        
        if i == 0:
            if j == 0:
                p_time = 0 
            else: 
                p_time = e_plan[j-1]
        else:
            if j == 0 :
                p_time =  end_plans[i-1][j] 
            else:    
                p_time = max( e_plan[j-1], end_plans[i-1][j])   
            
        s_plan.append(p_time)
        e_plan.append(p_time+ level[i]*person[j] )
    print( i, e_plan )    
    start_plans.append(s_plan)
    end_plans.append(e_plan)

print("start time :: ", start_plans)
print("end time :: ", end_plans)
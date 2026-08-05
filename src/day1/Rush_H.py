Cup_Quantity=[12, 5, 8, 20, 3, 15, 22]
Hrs=[8,9,10,11,12,1,2,3,4,5,6,7,8]
def rush(CQ,Hr):
    sm=sum(CQ)
    avg=sm/len(CQ)
    print(f"Total:{sm} Cups | Average: {avg:.1f}/hr Rushing Hours (above average):",end=" ")
    for i in range(len(CQ)):
        if CQ[i]>avg:
            print(f"{Hr[i]}{'AM' if i<=3 else 'PM'}",end=" ")
rush(Cup_Quantity,Hrs)


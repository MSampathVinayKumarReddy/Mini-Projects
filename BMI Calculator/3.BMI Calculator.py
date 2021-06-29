from pywebio.input import *
from pywebio.output import *

def bmi_calculator():
    height=input('enter height: ',type=FLOAT)
    weight=input('enter weigth: ',type=FLOAT)
    
    bmi=weight/(height/100)**2
    
    bmi_output=[(16, 'Severely underweight'), (18.5, 'Underweight'),
                  (25, 'Normal'), (30, 'Overweight'),
                  (35, 'Moderately obese'), (float('inf'), 'Severely obese')]
    
    for i,j in bmi_output:
        if bmi<=i:
            put_text('BMI is :%.1f and the person is :%s'%(bmi,j))
            break

if __name__=='__main__':
    bmi_calculator()        
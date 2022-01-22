#!/usr/bin/env python
# coding: utf-8

# In[1]:


JsonData  = [{"Gender":"Male", "HeightCm":171, "WeightKg":96},
             {"Gender":"Male", "HeightCm":161, "WeightKg":85},
             {"Gender":"Male", "HeightCm":180, "WeightKg":77},
             {"Gender":"Female", "HeightCm":166, "WeightKg":62},
             {"Gender":"Female", "HeightCm":150, "WeightKg":70},
             {"Gender":"Female", "HeightCm":167, "WeightKg":82}]

def CalculateBMI():
    global JsonData
    for i, data in enumerate(JsonData):
        BMI = data["WeightKg"]/(data["HeightCm"]/100)
        BMI = round(BMI, 1) # round of BMI till one decimal place
        if BMI< 18.4:
            BMICategory = 'Underweight'
            HealthRisk = 'Malnutrition risk'
        elif BMI>=18.5 and BMI<= 24.9:
            BMICategory = 'Normal weight'
            HealthRisk = 'Low risk'
        elif BMI>=25 and BMI<= 29.9:
            BMICategory = 'Overweight'
            HealthRisk = 'Enhanced risk'
        elif BMI>=30 and BMI<= 34.9:
            BMICategory = 'Moderately obese'
            HealthRisk = 'Mdedim risk'
        elif BMI>=35 and BMI<= 39.9:
            BMICategory = 'Severely obese'
            HealthRisk = 'High risk'
        else:                                           # weight greater than or equal to 40kg
            BMICategory = 'very severely obese'
            HealthRisk = 'Very high risk'
        data["BMI"]= BMI
        data["BMI Category"]= BMICategory
        data["Health risk"]= HealthRisk
        JsonData[i]=data
        
CalculateBMI()    
print(JsonData)


# In[ ]:





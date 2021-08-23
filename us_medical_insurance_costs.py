import csv
import statistics

with open("insurance.csv", "r+") as insurance_file:
    insurance_data = csv.DictReader(insurance_file)

    age_data = []
    sex_data = []
    bmi_data = []
    children_data = []
    smoker_data = []
    region_data = []
    insurance_cost = []
    
    for row in insurance_data:
        age_data.append(row["age"])
        sex_data.append(row["sex"])
        bmi_data.append(row["bmi"])
        children_data.append(row["children"])
        smoker_data.append(row["smoker"])
        region_data.append(row["region"])
        insurance_cost.append(row["charges"])

        
class Info:

    def __init__(self, age, sex, num_of_children, region, insurance_costs, bmi, smoker):
        self.age = age
        self.sex = sex
        self.num_of_children = num_of_children
        self.region = region
        self.insurance_costs = insurance_costs
        self.bmi = bmi
        self.smoker = smoker

    def where_majority_from(self):
        areas_dict = dict()
        areas_dict["Southwest"] = self.region.count("southwest")
        areas_dict["Northwest"] = self.region.count("northwest")
        areas_dict["Southeast"] = self.region.count("southeast")
        areas_dict["Northeast"] = self.region.count("northeast")
        majority = max(areas_dict.values())
        for area, num_people in areas_dict.items():
            if num_people == majority:
                print("The majority of individuals are from {}. {} people on average.".format(area, num_people))
        print("Distribution in other regions:", areas_dict)

    def average_age(self):
        women_with_children = list()
        men_with_children = list()
        for index, child in enumerate(self.num_of_children, start=0):
            if child != "0":
                if self.sex[index] == "female":
                    women_with_children.append(self.age[index])
                elif self.sex[index] == "male":
                    men_with_children.append(self.age[index])
        women_ages = [int(ages) for ages in women_with_children]
        men_ages = [int(ages) for ages in men_with_children]
        average_age_men = statistics.mean(men_ages)
        average_age_women = statistics.mean(women_ages)
        print("The average age for women who have children is {}.".format(int(average_age_women)))
        print("The average age for men who have children is {}.".format(int(average_age_men)))

    def num_of_smokers(self):
        smoke = 0
        non_smoke = 0
        for data in self.smoker:
            if data == "yes":
                smoke += 1
            else:
                non_smoke += 1
        print("Number of smoker:", smoke, "\nNumber of non-smoker:", non_smoke)

    def bmi_by_smoke(self):
        smoke = []
        non_smoke = []
        for index, smoke_status in enumerate(self.smoker, start=0):
            if smoke_status == "yes":
                smoke.append(float(self.bmi[index]))
            else:
                non_smoke.append(float(self.bmi[index]))

        non_smoke_average_bmi = statistics.mean(non_smoke)
        smoke_average_bmi = statistics.mean(smoke)
        return "Smokers average BMI: " + str(smoke_average_bmi) + "\nNon-smokers average BMI: " + str(
            non_smoke_average_bmi)

    def region_by_sex(self):
        sw = []
        se = []
        nw = []
        ne = []
        for area, s in zip(self.region, self.sex):
            if area == "southwest":
                sw.append(s)
            elif area == "southeast":
                se.append(s)
            elif area == "northwest":
                nw.append(s)
            elif area == "northeast":
                ne.append(s)

        print("Patients from southwest are mostly {}.".format(statistics.mode(sw)))
        print("Patients from northwest are mostly {}.".format(statistics.mode(nw)))
        print("Patients from southeast are mostly {}.".format(statistics.mode(ne)))
        print("Patients from northeast are mostly {}.".format(statistics.mode(se)))

    def costs_by_sex(self):
        female_costs = []
        male_costs = []
        for data in self.sex:
            index = self.sex.index(data)
            if data == "female":
                female_costs.append(float(self.insurance_costs[index]))
            else:
                male_costs.append(float(self.insurance_costs[index]))

        return "Average insurance cost for female is " + str(statistics.mean(female_costs)) \
               + "$" + "\nAverage insurance cost for male is " + str(statistics.mean(male_costs)) + "$"

    def dictionary(self):
        insurance_dict = {"Age": self.age, "Sex": self.sex, "BMI": self.bmi, "Number of children": self.num_of_children,
                          "Smoker": self.smoker, "Region": self.region, "Insurance_costs": self.insurance_costs}
        return insurance_dict



info = Info(age_data, sex_data, children_data, region_data, insurance_cost, bmi_data, smoker_data)

info.where_majority_from()
info.average_age()
info.num_of_smokers()
print(info.bmi_by_smoke())
info.region_by_sex()
print(info.costs_by_sex())
print(info.dictionary())

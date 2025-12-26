import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from faker import Faker


class AdmissionDataGenerator:
    def __init__(self):
        self.fake = Faker('ru_RU')
        
        # Специальности и соответствующие предметы ЦТ
        self.specialties = {
            'Информатика': ['математика', 'физика', 'русский/белорусский'],
            'Экономика': ['математика', 'иностранный язык', 'русский/белорусский'],
            'Медицина': ['биология', 'химия', 'русский/белорусский'],
            'Юриспруденция': ['обществоведение', 'иностранный язык', 'русский/белорусский'],
            'Филология': ['история', 'иностранный язык', 'русский/белорусский'],
            'Психология': ['биология', 'математика', 'русский/белорусский']
        }
                
        # Операторы мобильной связи
        self.operators = ['29', '33', '44', '25']

    def generate_phone_number(self):
        operator = np.random.choice(self.operators)
        number = ''.join([str(np.random.randint(0, 11)) for _ in range(7)])
        return f"+375{operator}{number}"

    def generate_ct_scores(self, specialty):
    
        subjects = self.specialties[specialty]
        scores = {}
        
        for subject in subjects:
            if subject in ['математика', 'физика']:
                scores[subject] = np.random.randint(60, 100)
            elif subject in ['биология', 'химия']:
                scores[subject] = np.random.randint(60, 95)
            else:
                scores[subject] = np.random.randint(60, 100)
                
        return scores

    def generate_certificate_grade(self):
        grade = np.random.uniform(6, 10)
        return round(grade, 1)

    def calculate_total_score(self, ct_scores, certificate_grade):
        ct_total = sum(ct_scores.values())
        certificate_grade = certificate_grade * 10 
        return ct_total + certificate_grade

    def generate_student_data(self, n_students=1001):
        students = []
        years = [2020, 2021, 2022, 2023, 2024, 2025]
        
        for year in years:
            for _ in range(n_students):
                specialty = np.random.choice(list(self.specialties.keys()))
            
                # Генерация данных
                full_name = self.fake.name()
                study_form = np.random.choice(['бесплатная', 'платная'])
                ct_scores = self.generate_ct_scores(specialty)
                certificate_grade = self.generate_certificate_grade()
                total_score = self.calculate_total_score(ct_scores, certificate_grade)
            
            
                address = f"{self.fake.city()}, {self.fake.street_address()}"
                phone = self.generate_phone_number()
            
                student_data = {
                    'ФИО': full_name,
                    'Год поступления': year,
                    'Форма обучения': study_form,
                    'Баллы ЦЭ/ЦТ': ct_scores,
                    'Средний балл аттестата': certificate_grade,
                    'Общий балл': total_score,
                    'Специальность': specialty,
                    'Адрес регистрации': address,
                    'Телефон': phone
                }
            
            
                students.append(student_data)
        
            
        return students

def data_visualizations(students_df):

    fig1, axes1 = plt.subplots(2, 2, figsize=(15, 15))
    fig1.suptitle('Динамика показателей вступительной кампании 2020-2025', fontsize=16, fontweight='bold')
    
    # Динамика среднего балла за ЦТ/ЦЭ по предметам (линейная диаграмма)
    ax1 = axes1[0][0]
    subjects_data = {}
    
    for year in sorted(students_df['Год поступления'].unique()):
        year_data = students_df[students_df['Год поступления'] == year]
        for student in year_data.itertuples():
            for subject, score in student[4].items():  # Баллы ЦЭ/ЦТ
                if subject not in subjects_data:
                    subjects_data[subject] = {}
                if year not in subjects_data[subject]:
                    subjects_data[subject][year] = []
                subjects_data[subject][year].append(score)
    
    for subject, years_data in subjects_data.items():
        years = sorted(years_data.keys())
        avg_scores = [np.mean(years_data[year]) for year in years]
        ax1.plot(years, avg_scores, marker='o', linewidth=2, label=subject)
    
    ax1.set_title('Динамика среднего балла за ЦТ/ЦЭ по предметам', fontweight='bold')
    ax1.set_xlabel('Год')
    ax1.set_ylabel('Средний балл')
    ax1.legend(loc='upper left')
    ax1.grid(True, alpha=0.3)
    
    # Динамика среднего балла аттестата (столбчатая диаграмма)
    ax2 = axes1[0][1]
    certificate_avg = students_df.groupby('Год поступления')['Средний балл аттестата'].mean()
    years = certificate_avg.index
    scores = certificate_avg.values
    
    ax2.bar(years, scores, color="purple")
    ax2.set_title('Динамика среднего балла аттестата', fontweight='bold')
    ax2.set_xlabel('Год')
    ax2.set_ylabel('Средний балл аттестата')
  
      
    # Динамика проходного балла по специальностям (линейная диаграмма)
    ax3 = axes1[1][1]
    passing_scores = students_df.groupby(['Год поступления', 'Специальность'])['Общий балл'].min().unstack()
    
    for specialty in passing_scores.columns:
        ax3.plot(passing_scores.index, passing_scores[specialty], 
                marker='s', linewidth=2, label=specialty)
    
    ax3.set_title('Динамика проходного балла по специальностям', fontweight='bold')
    ax3.set_xlabel('Год')
    ax3.set_ylabel('Проходной балл')
    ax3.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    ax3.grid(True, alpha=0.3)

    fig2, axes2 = plt.subplots(1, 2, figsize=(10, 10))
    fig2.suptitle('Статистика вступительной кампании 2020-2025', fontsize=16, fontweight='bold')
    
    # Количество поступивших студентов по специальностям
    ax4 = axes2[0]
    specialty_counts = students_df['Специальность'].value_counts()
    
    ax4.bar(list(specialty_counts.index), specialty_counts.values, color="purple")
    ax4.set_title('Количество поступивших по специальностям', fontweight='bold')
    ax4.set_ylabel('Количество студентов')
    
    ax4.yaxis.set_major_locator(MultipleLocator(100))

    
    # Статистика по формам обучения (круговая диаграмма)
    ax5 = axes2[1]
    study_form_counts = students_df['Форма обучения'].value_counts()
    colors = ['#ff9999', '#66b3ff']
    
    ax5.pie(study_form_counts.values, labels=study_form_counts.index, autopct='%1.1f%%', colors=colors, startangle=90)
    
    ax5.set_title('Распределение по формам обучения', fontweight='bold')

    plt.tight_layout()
    plt.show()

    
def main():
    print("Генерация данных о вступительной кампании...")
    
    generator = AdmissionDataGenerator()
    students_data = generator.generate_student_data(n_students=1200)
    
    df = pd.DataFrame(students_data)
    data_visualizations(df)
   
if __name__ == "__main__":
    main()
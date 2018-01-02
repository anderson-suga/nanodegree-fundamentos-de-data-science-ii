import pandas as pd

def age_group(x):
    if x >=1 and x<= 11:
        return 'Child'
    elif x >=12 and x <=17:
        return 'Teenage'
    elif x>=18 and x<=44:
        return 'Adult'
    elif x>=45 and x<=59:
        return 'Middle'
    elif x>=60:
        return 'Elderly'
    else:
        return 'Unknown'

def status(x):
    if x == 0:
        return 'Perished'
    else:
        return 'Survived'

def status_description(x):
    if x == 0:
        return 'No'
    else:
        return 'Yes'

def description_sex(x):
    return x.title()

def description_class(x):
    if x == 1:
        return 'First'
    elif x == 2:
        return 'Second'
    elif x == 3:
        return 'Third'

filename = "titanic-data.csv"
output = 'clean_titanic_data.csv'

df = pd.read_csv(filename, sep=',')

df['LastName'] = df['Name'].apply(lambda x : pd.Series(x.split(',')))[0]
df['FirstName'] = df['Name'].apply(lambda x : pd.Series(x.split('.')))[1]
df['Title'] = df['Name'].apply(lambda x : pd.Series(x.split(',')))[1].apply(lambda x : pd.Series(x.split('.')))[0]
df['AgeGroup'] = df['Age'].apply(lambda x : age_group(x))
df['Status'] = df['Survived'].apply(lambda x : status(x))
df['Survived'] = df['Survived'].apply(lambda x : status_description(x))
df['Gender'] = df['Sex'].apply(lambda x : description_sex(x))
df['Class'] = df['Pclass'].apply(lambda x : description_class(x))

cols = ['PassengerId','Survived','Status','Pclass','Class','Title','LastName','FirstName','Sex','Gender','Age','AgeGroup','SibSp','Parch']
list_name = df[cols]

## Write DataFrame to CSV
list_name.to_csv(output, sep='\t', encoding='utf-8',index=False)


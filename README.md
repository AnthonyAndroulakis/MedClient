# MedClient
simple client for https://projectmeded.org
python versions 3.0+ supported

```py
from medclient import MedClient

m = MedClient()
opportunities = m.search(categories=['research', 'program'], area_of_study='cancer')
for o in opportunities:
    print(o['name'])
```

## some docs
```MedClient.search```
#### Parameters (all optional):
- categories (list of strs) - can be 'research', 'program', 'volunteering', and/or 'shadowing'
- query (str)
- area_of_study (str) - can be 'Cancer', 'Medicine', 'Mental Health', 'Disaster Health', 'Basic Science', 'Research', 'Rehabilitation', 'Public Health', 'Biomedical Research', 'Pharmacology and Neuroscience', 'Molecular Sciences', 'Quantitative Biology', 'Materials Research Science', 'Synthetic Biology', 'Neuroscience', and/or 'Sexual Assault Prevention'. case-insensitive, spaces ignored
- institution (str) - can be 'University of Chicago', 'Northwestern Medicine', 'Project SEARCH', 'Active Minds', 'American Red Cross', 'The Leadership Alliance', 'Various', 'University of Illinois Urbana-Champaign', 'Shirley Ryan AbilityLab', 'Illinois Department of Public Health', 'University of Illinois Chicago', 'CommunityHealth', 'Loyola University', 'ScribeAmerica', 'Robert H. Lurie Comprehensive Cancer Center', 'Northwestern University', 'American Institutes for Research', 'NSF-Simons Center for Quantitative Biology', 'Northwestern University Materials Research Science & Engineering Center', 'Rush University', "Lurie Children's Hospital", 'Weiss Memorial Hospital', 'Swedish Hospital', 'AMITA Saint Joseph Chicago', 'Sinai Chicago', 'Rush University Medical Center', 'AMITA Health Saints Mary and Elizabeth Medical Center Chicago', 'Chicago Shriners Hospital', 'Norwegian American Hospital', 'University of Illinois Hospital', 'Old Irving Park Community Clinic', 'Howard Brown Health', 'Asian Human Services', 'Illinois Area Health Education Centers', 'University of California, Los Angeles', 'Zacharias Sexual Abuse Center', 'The Catholic Charities Archdiocese of Chicago', 'Christ Church', and/or 'Lake County Medical Reserve Corps'. case-insensitive, spaces and punctuation ignored
- location (str) - can be 'Chicago, IL', 'Various', 'Urbana, IL', 'Wheaton, IL', 'Evanston, IL', 'Downtown', 'Northside', 'Southside', 'West side', 'Lake County', and/or 'Los Angeles, CA'. case-insensitive, spaces and punctuation ignored
- dates (list of strs) - can be 'all year', 'summer', and/or 'academic year'
- eligibility (list of strs) - can be '9th', '10th', '11th', '12th', 'freshman', 'sophomore', 'junior', and/or 'senior'
- stipend (bool) - aka funding
- page (int)

#### Returns:
list of dictionaries      
the important keys in each dictionary are: ['dates', 'age', 'name', 'email', 'stipend', 'description', 'requirements', 'area', 'institution', 'location', 'eligibility', 'experience']
